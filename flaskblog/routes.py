from flask import render_template, url_for, flash, redirect, request, Blueprint
from ext import db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


bp = Blueprint('front', __name__)
'''
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
'''


@bp.route("/")
@bp.route("/home/")
def home():
    return render_template('home.html', title='Home Page')


@bp.route("/symptom/")
def symptom():
    return render_template('symptom.html', title='Symptom')


@bp.route("/visualization/")
def visualization():
    return render_template('visualization.html', title='Visualization')


@bp.route("/register/", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('admin.patient'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(
        #     form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('front.login'))
    return render_template('register.html', title='Register', form=form)


@bp.add_app_template_filter
def arr(v):
    new_list = []
    for x in v:
        new_list.append([x.name, x.time, x.parts, x.degree, x.date])
    return new_list


@bp.route("/login/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.patient'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # if user and bcrypt.check_password_hash(user.password, form.password.data):
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin.patient'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@bp.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('front.login'))


@bp.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')




