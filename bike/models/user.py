from math import floor
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from bike import login_manager

from bike.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float

from flask_login import UserMixin


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))


class User(UserMixin, Base):
    # __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    sys_user_name = Column(String(24), nullable=False, unique=True)
    _password = Column('password', String(128), nullable=False)
    cadmin_name = Column(String(32))
    sex = Column(Integer)
    state = Column(Integer)
    birthday = Column(String(12))
    address = Column(String(50))
    phone_number = Column(String(18), unique=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        temp = s.dumps({'id': self.id}).decode('utf-8')
        return temp

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)    # 主键才可以用get
            user.password = new_password
        return True