from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MovieForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(message='Please the fuckin title...')])
	genre = StringField('Genre', validators=[DataRequired(message='Please the fuckin genre...')])
	trailer = StringField('Trailer', validators=[DataRequired(message='Please the fuckin trailer...')])

