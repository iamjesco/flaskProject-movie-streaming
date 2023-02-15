from flask import Flask, render_template, flash, redirect, url_for, Response
from database.dbase import Database as db
from database.models import Movie
from forms.all_forms import MovieForm
import os
import boto3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wgswrg4623tgsgw4'
app.config['UPLOAD_FOLDER'] = 'static/media'
BUCKET = "jescoflix"


@app.route('/')
def home():
	return redirect(url_for('alpha'))


@app.route('/alpha/')
def alpha():
	return render_template('home.html')


@app.route('/alpha/about/')
def about():
	return render_template('about.html')


@app.route('/alpha/movie/')
def movie():
	movies = db.fetch_all_movies()
	if movies:
		featured_movie = [a_movie for a_movie in movies][0]
		return render_template('movie.html', featured_movie=featured_movie)
	else:
		return render_template('nomovie.html')


@app.route('/alpha/trailer/')
def trailer():
	movies = db.fetch_all_movies()
	if movies:
		return render_template('trailer.html', movies=movies)
	else:
		return render_template('nomovie.html')


# ====================================================================
#       DASHBOARD ENDPOINTS
# ====================================================================

@app.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
	form = MovieForm()
	movies = db.fetch_all_movies()
	if form.validate_on_submit():
		payload = Movie(
			title=form.title.data,
			genre=form.genre.data,
			trailer=form.trailer.data,
			thumbnail=form.thumbnail.data,
			starring=form.starring.data,
			released=form.released.data,
			filepath=form.filepath.data,)
		db.add_movie(payload.create_json())
		flash('Movie uploaded successfully', 'success')
		return redirect(url_for('dashboard'))
	if movies:
		movie = [a_movie for a_movie in movies][0]
		return render_template('dashboard.html', form=form, movie=movie)
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
