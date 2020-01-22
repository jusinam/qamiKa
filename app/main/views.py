from . import RecommedationForm


@main.route('/commic/recommed/<int:id>')
@loginrequired
def recommed(id):
    
form=RecommedationForm()
