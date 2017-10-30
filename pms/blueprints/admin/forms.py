# coding: utf-8
from flask_wtf import Form

from pms.blueprints.user.models import User, db
from wtforms import StringField, SelectField, BooleanField, IntegerField, FloatField
from lib.util_wtforms import ModelForm, choices_from_dict

from wtforms.validators import DataRequired, Length, Optional, Regexp, NumberRange
from wtforms_components import Unique


class BulkDeleteForm(Form):
    pass


class UserForm(ModelForm):
    username_message = '仅限字母，数字，中文和下划线组合'

    username = StringField(validators=[
        Unique(
            User.username,
            get_session=lambda: db.session
        ),
        DataRequired(),
        Length(1, 16),
        Regexp('^\w+$', message=username_message)
    ])

    role = SelectField('角色', [DataRequired()],
                       choices=choices_from_dict(User.ROLE,
                                                 prepend_blank=False))

    email = StringField('E-mail', [DataRequired()])
    phone = StringField('手机', [DataRequired()])


class SearchForm(Form):
    q = StringField('搜索', [Optional(), Length(1, 256)])

