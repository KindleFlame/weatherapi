from wtforms import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


from wtforms import Form, BooleanField, StringField, PasswordField, validators


class FormWeatherQuery(Form):
    username = StringField('Your Username')
    city = StringField('City')
