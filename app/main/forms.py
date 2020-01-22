from ..models import Recommedation
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField


class RecommedationForm(FlaskForm):

    heading= StringField('title',validators=[Required()])
    content = TextAreaField('content body', validators=[Required()])
    submit = SubmitField('Submit')
