from flask_script import Manager
from ext import db
from flaskblog import app
from flask_migrate import Migrate, MigrateCommand
from flaskblog.models import User, Symptom, Post
# from flaskblog.apps.admin.models import Admin
import random
import string


manager = Manager(app)
Migrate(app, db, render_as_batch=True)
manager.add_command('db', MigrateCommand)


@manager.command
def add_user():
    for x in range(50):
        username = ''.join(random.sample(string.ascii_letters + string.digits, 6))
        positon = random.choice(['CFO', 'CEO', 'CTO'])
        email = username+ '@qq.com'
        age = random.randint(18, 90)
        office = random.choice(['London', 'Beijing', 'Shanghai', 'NewYork'])
        user = User(username=username, password='123456', position=positon, email=email, age=age, office=office, salary='$100,000')
        db.session.add(user)
    db.session.commit()
    print('添加成功')


@manager.command
def add_symptom():
    user_id = 1
    import random
    import datetime
    for x in range(1):
        name = random.choice(['Numbness', 'Bruising', 'Skin changes', 'Pain'])
        date = datetime.datetime.strptime('2019-03-22', '%Y-%m-%d').date()
        time = random.randint(1, 5)
        parts = random.choice(['chest', 'back', 'arm', 'leg', 'other'])
        degree = random.randint(1, 11)
        sym = Symptom(name=name, date=date, time=time, parts=parts, degree=degree, user_id=user_id)
        db.session.add(sym)
    db.session.commit()
    print('success')


@manager.command
def start():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()


