from ext import db
from werkzeug.security import generate_password_hash, check_password_hash
#
#
# class Admin(db.Model):
#     __tablename__ = 'admin'
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(50), unique=True)
#     _password = db.Column(db.String(100))
#
#     symptoms = db.relationship('symptom', backref='admin')
#
#     def __repr__(self):
#         return f"User('{self.first_name}', '{self.last_name}')"
#
#     @property
#     def password(self):
#         return self._password
#
#     @password.setter
#     def password(self, pwd):
#         self._password = generate_password_hash(pwd)
#
#     def check_password(self, pwd):
#         return check_password_hash(self.password, pwd)


# class Symptom(db.Model):
#     __tablename__ = 'symptom'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     date = db.Column(db.Date)
#     time = db.Column(db.Integer)
#     parts = db.Column(db.String(100))
#     degree = db.Column(db.Integer)
#     admin_id = db.Column(db.ForeignKey('admin.id'))
#
#     def __repr__(self):
#         return f"Symptom('{self.name}', '{self.pain_degree}')"
