from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class Blog(FlaskForm):
    title = StringField('Title')
    author = StringField('Author')
    content = StringField('Content')
    submit = SubmitField('Post')

class Bloga():
    title = ""