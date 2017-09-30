# coding: utf-8
from flask_wtf import Form
from wtforms import HiddenField, StringField, PasswordField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class LoginForm(Form):
    identity = StringField('Your email',
                        [DataRequired(), Length(3, 254)])
    password = PasswordField('Password', [DataRequired(), Length(8, 128)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')