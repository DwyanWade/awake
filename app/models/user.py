"""
Created on 2018/6/6 23:25

"""
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base, db

__Author__ = '阿强'


class User(Base):
    id = Column(Integer, primary_key=True)
    openid = Column(String(64), unique=True, nullable=False)
    auth = Column(SmallInteger, default=1)
    # nickname = Column(String(24), unique=True)

    # def keys(self):
    #     return ['nickname', 'email', 'id', 'auth']

    # @property
    # def password(self):
    #     return self._password

    # @password.setter
    # def password(self, raw):
    #     self._password = generate_password_hash(raw)

    @staticmethod
    def register(openid):
        #先查询user是否已经存在openid
        user = User.query.filter_by(openid=openid).first()
        if not user:
            with db.auto_commit():
                user = User()
                user.openid = openid
                db.session.add(user)
            return user.id
        else:
            print("用户已存在")
            return user.id

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'scope': scope}

    # def check_password(self, raw):
    #     if not self._password:
    #         return False
    #     return check_password_hash(self._password, raw)
