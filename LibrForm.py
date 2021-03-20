from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, FileField, DateField, validators, BooleanField
from wtforms.validators import DataRequired

class LibrForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    year = DateField('year', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
    description = TextAreaField('description')
    