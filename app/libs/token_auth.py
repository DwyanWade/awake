"""
Created on 2018/6/11 22:43

"""
from collections import namedtuple
from functools import wraps

from flask import current_app, g, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed
from app.libs.scope import is_in_scope

__Author__ = '阿强'

User = namedtuple('User', ['uid'])


def token_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("token")
        user_info = verify_auth_token(token)
        if not user_info:
            return False
        else:
            g.user = user_info
        return func(*args, **kwargs)
    return wrapper


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='invalid token', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expiration', error_code=1003)
    uid = data['uid']
    return User(uid)
