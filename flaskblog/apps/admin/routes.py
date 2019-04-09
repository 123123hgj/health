from flask import (Blueprint, render_template,
                   request, session, redirect,
                   url_for, g)
from flaskblog.models import User, Symptom
from .forms import AddSymptomForm, RegisterForm, LoginForm
# from flaskblog.apps.admin.models import Admin

from ext import db
from functools import wraps
import time
import datetime
from restful import success, param_error

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        g.user = user


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if g.get('user'):
            return f(*args, **kwargs)
        return redirect(url_for('front.login'))

    return wrapper


@bp.route('/tables/')
def tables():
    users = User.query.all()
    return render_template('admin/tables.html', users=users)


@bp.route('/patient/', methods=['get', 'post'])
def patient():
    # if request.method == 'POST':
    #     form = AddSymptomForm(request.form)
    #     print(request.form)
    #     print(request.form.getlist('symptom'))
    #     if form.validate():
    #         print('pass validation')
    #         symptom = form.symptom.data
    #         duration = form.duration.data
    #         degree = form.degree.data
    #         parts = form.parts.data
    #         sym = Symptom(name=symptom, duration=duration, degree=degree, parts=parts)
    #         db.session.add(sym)
    #         db.session.commit()
    #         return 'Symptom added successfully! '
    #     else:
    #         print(form.get_error())
    return render_template('admin/patient.html')


@bp.route('/patientlist/')
def patientlist():
    # users = User.query.all()
    from_date = (datetime.datetime.today() - datetime.timedelta(days=14)).date()
    to_date = datetime.datetime.today().date()
    from sqlalchemy import func
    syms = db.session.query(Symptom).filter_by(
        user_id=g.user.id).\
        filter(Symptom.date.between(from_date, to_date)).\
        order_by(Symptom.date).all()
    return render_template('admin/patientlist.html', syms=syms)


@bp.add_app_template_filter
def format(v):
    if v == 1:
        return [1, 0, 0, 0]
    elif v == 2:
        return [0, 2, 0, 0]
    elif v == 3:
        return [0, 0, 3, 0]
    else:
        return [0, 0, 0, 4]


@bp.route('/symptom/', methods=['get', 'post'])
def symptom():
    if request.method == 'POST':
        if not request.form:
            return param_error('Please click Add button to add some new symptoms !')
        date = request.args.get('date')
        duration = request.args.get('time')
        time_array = time.localtime(float(int(date) / 1000))
        date = time.strftime("%Y-%m-%d", time_array)
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        values = [x for x in request.form.values()]
        values_group = [values[i:i + 3] for i in range(0, len(values), 3)]
        for value in values_group:
            name = value[0]
            parts = value[1]
            degree = value[2]
            if not name:
                return param_error('Please input the symptom !')
            sym = Symptom.query.filter_by(name=name).first()
            if sym:
                return param_error('The symptom already exists !')
            sym = Symptom(name=name, date=date, time=int(duration), parts=parts, degree=int(degree), user_id=g.user.id)
            db.session.add(sym)
        db.session.commit()
        return success()
    return render_template('admin/symptom.html')


# @bp.route('/register/', methods=['get', 'post'])
# def register():
#     if request.method == 'POST':
#         form = RegisterForm(request.form)
#         if form.validate():
#             first_name = form.first_name.data
#             last_name = form.last_name.data
#             email = form.email.data
#             if User.query.filter_by(email=email).first():
#                 return 'The email already exists ！'
#             password = form.password.data
#             user = User(first_name=first_name, last_name=last_name, email=email, password=password)
#             db.session.add(user)
#             db.session.commit()
#             session['user_id'] = user.id
#             return redirect(url_for('admin.patient'))
#         return form.get_error()
#     return render_template('register.html')
#
#
# @bp.route('/login/', methods=['get', 'post'])
# def login():
#     if request.method == 'GET':
#         if g.get('user'):
#             return redirect(url_for('admin.patient'))
#         global next_to
#         next_to = request.referrer
#         return render_template('login.html')
#     form = LoginForm(request.form)
#     if form.validate():
#         email = form.email.data
#         password = form.password.data
#         remember = request.form.get('remember')
#         user = User.query.filter_by(email=email).first()
#         if not user:
#             return 'The account is not registered !'
#         if not user.check_password(password):
#             return 'The password is not correct !'
#         session['user_id'] = user.id
#         if remember:
#             session.permanent = True
#         return redirect(next_to) if next_to else redirect(url_for('admin.patient'))
#     return form.get_error()
#
#
# @bp.route('/logout/')
# def logout():
#     session.pop('user_id')
#     return redirect(url_for('front.login'))


@bp.route('/')
@login_required
def index():
    return render_template('admin/index.html')
