"""
Created on 2018/6/6 0:43

"""
from flask import jsonify, g

from app.libs.error_code import DeleteSuccess, AuthFailed
from app.libs.redprint import RedPrint
from app.libs.token_auth import token_decorator
from app.models.base import db
from app.models.user import User

__Author__ = '阿强'

api = RedPrint('user')


@api.route('/<int:uid>', methods=['GET'])
#@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass


@api.route('', methods=['GET'])
#@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['DELETE'])
#@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()




