from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MovieForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(message='Please the fuckin title...')])
	genre = StringField('Genre', validators=[DataRequired(message='Please the fuckin genre...')])
	thumbnail = StringField('Thumbnail', validators=[DataRequired(message='Please the fuckin thumbnail...')])
	trailer = StringField('Trailer', validators=[DataRequired(message='Please the fuckin trailer...')])
	starring = StringField('Starring', validators=[DataRequired(message='Please the fuckin actor...')])
	released = StringField('Released', validators=[DataRequired(message='Please the fuckin release date...')])
	upload = FileField('Upload Movie', validators=[FileRequired()])
