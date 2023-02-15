from flask import Flask, render_template, flash, redirect, url_for, Response
from database.dbase import Database as db
from database.models import Movie
from forms.all_forms import MovieForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wgswrg4623tgsgw4'


@app.route('/')
def home():
	movies = db.fetch_all_movies()
	return render_template('trailer.html', movies=movies)


@app.route('/movie/')
def movie():
	return render_template('movie.html')


@app.route('/trailer/')
def trailer():
	movies = db.fetch_all_movies()
	return render_template('trailer.html', movies=movies)


# ====================================================================
#       CRUD ENDPOINTS
# ====================================================================

@app.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
	form = MovieForm()
	if form.validate_on_submit():
		payload = Movie(
			title=form.title.data,
			genre=form.genre.data,
			trailer=form.trailer.data,)
		db.add_movie(payload.create_json())
		flash('Post created successfully', 'success')
		return redirect(url_for('dashboard'))
	return render_template('dashboard.html', form=form)


if __name__ == '__main__':
	app.run()
