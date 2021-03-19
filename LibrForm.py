from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, DateField, validators, BooleanField, DecimalField
from wtforms.validators import DataRequired

class LibrForm(FlaskForm):
    id = Decimalfield('id', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    year = DateField('year', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
    description = TextAreaField('description')
    image = FileField("image")
