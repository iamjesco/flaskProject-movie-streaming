from flask import Flask, render_template, flash, redirect, url_for, Response
from database.dbase import Database as db
from database.models import Movie
from forms.all_forms import MovieForm
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wgswrg4623tgsgw4'
app.config['UPLOAD_FOLDER'] = 'static/media'


@app.route('/')
def home():
	movies = db.fetch_all_movies()
	return render_template('trailer.html', movies=movies)


@app.route('/movie/')
def movie():
	movies = db.fetch_all_movies()
	movie = [a_movie for a_movie in movies][0]
	return render_template('movie.html', movie=movie)


@app.route('/trailer/')
def trailer():
	movies = db.fetch_all_movies()
	return render_template('trailer.html', movies=movies)


# ====================================================================
#       DASHBOARD ENDPOINTS
# ====================================================================

@app.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
	form = MovieForm()
	if form.validate_on_submit():
		filename = secure_filename(form.upload.data.filename)
		form.upload.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		payload = Movie(
			title=form.title.data,
			genre=form.genre.data,
			trailer=form.trailer.data,
			starring=form.starring.data,
			released=form.released.data,
			filename=filename,)
		db.add_movie(payload.create_json())
		flash('Movie uploaded successfully', 'success')
		return redirect(url_for('dashboard'))
	return render_template('dashboard.html', form=form)


@app.route('/blog/delete/<int:id>/', methods=['GET', 'POST'])
def delete(id):
	# if not g.user:
	#     flash('You need to be logged in to be able to delete posts', 'danger')
	#     return redirect(url_for('login'))
	movie = db.fetch_movie(id)
	os.remove(os.path.join(app.config['UPLOAD_FOLDER'], movie["filename"]))
	db.delete_movie(id)
	flash('Movie deleted successfully', 'success')
	return redirect(url_for('dashboard'))


if __name__ == '__main__':
	app.run()
