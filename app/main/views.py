from . import RecommedationForm
from ..models import Recommedation,Commic


@main.route('/commic/recommed/<int:id>')
@loginrequired
def recommed(id):
    commic=Commic.query.get(id)
    form=RecommedationForm()

    if form.validate_on_submit():
        new_recommedtaion=(heading=form.heading.data,content=form.content.data)

        new_recommedtaion.save()
