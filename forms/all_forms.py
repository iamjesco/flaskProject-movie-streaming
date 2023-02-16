from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email
# from wtforms.fields.html5 import EmailField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MovieForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(message='Please the fuckin title...')])
	genre = StringField('Genre', validators=[DataRequired(message='Please the fuckin genre...')])
	thumbnail = StringField('Thumbnail', validators=[DataRequired(message='Please the fuckin thumbnail...')])
	trailer = StringField('Trailer', validators=[DataRequired(message='Please the fuckin trailer...')])
	starring = StringField('Starring', validators=[DataRequired(message='Please the fuckin actor...')])
	released = StringField('Released', validators=[DataRequired(message='Please the fuckin release date...')])
	filepath = StringField('File Path', validators=[DataRequired(message='Please the fuckin file path...')])


class Login(FlaskForm):
	email = EmailField('Email', validators=[DataRequired(message='Yena bo email, lolo...'), Email()])
	password = PasswordField('Password', validators=[DataRequired(message='Bo ke login sin password, lul!')])


class Register(FlaskForm):
	username = StringField('Username', validators=[DataRequired(message='Registra sin nomber? Lolo...')])
	email = EmailField('Email', validators=[DataRequired(message='Registra sin email? Lolo...'), Email()])
	password = PasswordField('Password', validators=[DataRequired(message='Bo ke registra sin password, lul!')])
