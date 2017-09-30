# coding: utf-8
from collections import OrderedDict
from hashlib import md5

from pms.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask_login import UserMixin, current_app

from lib.util_sqlalchemy import ResourceMixin


class User(UserMixin, ResourceMixin, db.Model):
    ROLE = OrderedDict([
        ('member', 'Member'),
        ('manager', 'Manager'),
        ('boss', 'Boss'),
        ('admin', 'Admin')
    ])

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    # Authentication.
    role = db.Column(db.Enum(*ROLE, name='role_types',
                             native_enum=False),
                     index=True, nullable=False,
                     server_default='member')
    username = db.Column(db.String(24), nullable=False, index=True)
    phone = db.Column(db.String(24), unique=True)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False, server_default='')
    password = db.Column(db.String(128), nullable=False, server_default='')
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(User, self).__init__(**kwargs)

        self.password = User.encrypt_password(kwargs.get('password', ''))

    def is_active(self):
        """
        按照flask-login实现的方法覆盖默认值。

        :return: bool
        """
        return self.active

    @classmethod
    def find_by_identity(cls, identity):
        """
        Find a user by their e-mail or username.

        :param identity: Email or username
        :type identity: str
        :return: User instance
        """
        return User.query.filter(
            (User.email == identity) | (User.username == identity)).first()

    @classmethod
    def encrypt_password(cls, plaintext_password):
        """
        Hash a plaintext string using PBKDF2. This is good enough according
        to the NIST (National Institute of Standards and Technology).

        In other words while bcrypt might be superior in practice, if you use
        PBKDF2 properly (which we are), then your passwords are safe.

        :param plaintext_password: Password in plain text
        :type plaintext_password: str
        :return: str
        """
        if plaintext_password:
            return generate_password_hash(plaintext_password)

        return None

    def authenticated(self, with_password=True, password=''):
        """
        确认用户是已授权的，检查密码可选。

        :param with_password: 可选是否检查密码
        :type with_password: bool
        :param password: 可选用于认证的密码
        :type password: str
        :return: bool
        """
        if with_password:
            return check_password_hash(self.password, password)

        return True

    def get_auth_token(self):
        """
        返回用户的授权token。用密码作为token的部分信息，是因为不希望用户在改变密码后仍然能
        使用设备信息登录，让旧的令牌时效。这里用md5是可以满足安全要求的。

        通过这种方法来创建token以满足Flask-Login。

        :return: str
        """
        private_key = current_app.config['SECRET_KEY']

        serializer = URLSafeTimedSerializer(private_key)
        data = [str(self.id), md5(self.password.encode('utf-8')).hexdigest()]

        return serializer.dumps(data)
