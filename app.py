from flask import Flask, render_template, flash, redirect, url_for, session, g
from forms.all_forms import Login, Register
from database.dbase import Database as db
from database.models import Movie, User
from forms.all_forms import MovieForm
from flask_bcrypt import Bcrypt
import os
import boto3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wgswrg4623tgsgw4'
app.config['UPLOAD_FOLDER'] = 'static/media'
BUCKET = "jescoflix"
bcrypt = Bcrypt(app)


@app.before_request
def before_request():
	all_users = db.fetch_all_users()
	g.user = None
	if 'user_id' in session:
		user = [x for x in all_users if x['id'] == session['user_id']][0]
		g.user = user


@app.route('/')
def home():
	if not g.user:
		return redirect(url_for('login'))
	return redirect(url_for('movie'))


@app.route('/about/')
def about():
	return render_template('about.html')


@app.route('/movie/')
def movie():
	if not g.user:
		# flash('You need to be logged in to watch', 'danger')
		return redirect(url_for('login'))
	movies = db.fetch_all_movies()
	if movies:
		featured_movie = [a_movie for a_movie in movies][0]
		return render_template('movie.html', featured_movie=featured_movie)
	else:
		return render_template('nomovie.html')


@app.route('/trailer/')
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
	if not g.user:
		# flash('You need to be logged in to watch', 'danger')
		return redirect(url_for('login'))
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


# ====================================================================
#       DASHBOARD ENDPOINTS
# ====================================================================

@app.route("/login/", methods=['POST', 'GET'])
def login():
	if g.user:
		return redirect(url_for('home'))
	form = Login()
	if form.validate_on_submit():
		session.pop('user_id', None)
		email = form.email.data
		password = form.password.data
		user = db.fetch_user(email)
		if user and bcrypt.check_password_hash(user['password'], password):
			session['user_id'] = user['id']
			return redirect(url_for('movie'))
		flash('Please check Email or Password and try again', 'danger')
		return redirect(url_for('login'))
	return render_template('login.html', form=form)


@app.route('/logout/')
def logout():
	session.pop('user_id', None)
	return redirect(url_for('login'))


@app.route("/register/", methods=['POST', 'GET'])
def register():
	form = Register()
	if form.validate_on_submit():
		user = User(
			email=form.email.data,
			password=bcrypt.generate_password_hash(form.password.data)
			)
		db.create_user(user.json())
		flash('User created successfully', 'success')
		return redirect(url_for('register'))
	return render_template('register.html', form=form)


if __name__ == '__main__':
	app.run()
