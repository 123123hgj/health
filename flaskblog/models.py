from datetime import datetime
from ext import db
from flaskblog import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    _password = db.Column(db.String(60), nullable=False)

    position = db.Column(db.String(50))
    office = db.Column(db.String(50))
    age = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    salary = db.Column(db.String(50))

    posts = db.relationship('Post', backref='author', lazy=True)
    symptoms = db.relationship('Symptom', backref='user')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


# class Symptom(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     duration = db.Column(db.String(50))
#     pain_degree = db.Column(db.Integer)
#     add_time = db.Column(db.Date, default=datetime.today)
#
#     users = db.relationship('User', backref='symptom')
#
#     def __repr__(self):
#         return f"Symptom('{self.name}', '{self.duration}', '{self.pain_degree}')"

class Symptom(db.Model):
    __tablename__ = 'symptom'
    # __table_args__ = {'schema': 'schema_any'}
    # __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date)
    time = db.Column(db.Integer)
    parts = db.Column(db.String(100))
    degree = db.Column(db.Integer)
    user_id = db.Column(db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Symptom('{self.name}','{self.date}','{self.time}','{self.parts}', '{self.degree}')"
