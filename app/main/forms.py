from ..models import Recommedation
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,DateField


class RecommedationForm(FlaskForm):

    heading= StringField('title',validators=[Required()])
    content = TextAreaField('content body', validators=[Required()])
    time= start = DateField('Date', format='%m/%d/%Y')
    submit = SubmitField('Submit')
