from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, EqualTo, InputRequired, Email


class BaseForm(Form):
    def get_error(self):
        err = ''
        for v in self.errors.values():
            err += v[0]
        return err


class AddSymptomForm(BaseForm):
    date = StringField(validators=[Length(13, 13, 'Timestamp needed !')])
    time = StringField(validators=[Length(1, 1, 'Pain time needed !')])
    name = StringField(validators=[InputRequired('Please input symptoms! ')])
    parts = StringField(validators=[InputRequired('Please input pain part! ')])
    degree = IntegerField(validators=[InputRequired('Please input pain degree! ')])


class RegisterForm(BaseForm):
    first_name = StringField(validators=[InputRequired('Please input your first name !')])
    last_name = StringField(validators=[InputRequired('Please input your last name !')])
    email = StringField(validators=[Email(message='Please input a correct email address !')])
    password = StringField(validators=[Length(6, 18, 'Please set a 6-18 digits password !')])
    confirm = StringField(validators=[EqualTo('password', 'Password and confirm password not consistent !')])


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='Please input a correct email address !')])
    password = StringField(validators=[Length(6, 18, 'Please input a 6-18 digits password !')])

