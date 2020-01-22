from flask import render_template,url_for,request,flash,redirect,abort
from app.main  import main
from app.models import User,Recommedation
from .. import db, photos
from flask_login import login_required,current_user
import secrets
import os
from .forms import UpdateProfile,CreateBlog,Recommendation

# from ..email import mail_message

@main.route('/')
def index():


    return render_template('index.html')

@main.route('/profile',methods=['GET','POST'])
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.profile_pic.data:
            picture_file= save_pic(form.profile_pic.data)
            current_user.profile_pic_path = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Profile Updated Successfully')
        return redirect(url_for('main.profile'))
    elif request.method =='GET':
        form.bio.data = current_user.bio
    profile_pic_path = url_for('static',filename='photos' + current_user.profile_pic_path)
    return render_template('profile/profile.html',form=form)

# @main.route('/commic/recommed/<int:id>')
# @loginrequired
# def recommed(id):
#     commic=Commic.query.get(id)
#     form=RecommedationForm()

#     if form.validate_on_submit():
#         new_recommedtaion=Recommedation(heading=form.heading.data,content=form.content.data)
#         new_recommedataion.recommedation_saves()

#         return redirect('index.html',commic=commic)
#         title=f'make a new recommedation to |commic.id '

#     return ('recommend.html',form=form)
