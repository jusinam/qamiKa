from . import RecommedationForm
from ..models import Recommedation,Commic


@main.route('/commic/recommed/<int:id>')
@loginrequired
def recommed(id):
    commic=Commic.query.get(id)
    form=RecommedationForm()

    if form.validate_on_submit():
        new_recommedtaion=Recommedation(heading=form.heading.data,content=form.content.data)
        new_recommedataion.recommedation_saves()

        return redirect('index.html',commic=commic)
        title=f'make a new recommedation to |commic.id '

    return ('recommed.html',title=title,form=form)
