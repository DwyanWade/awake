"""
Created on 2018/8/9 23:12

"""
from flask import jsonify, g

from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import token_decorator
from app.models.classic import Classic
from app.models.tap import Tap
from app.validators.forms import LikeForm

__Author__ = '阿强'


api = RedPrint('like')


@api.route('', methods=['POST'])
@token_decorator
def like():
    uid = g.user.uid
    form = LikeForm().validate_for_api()
    cid = form.data["art_id"]
    type = form.data["type"]
    Tap.tap_like(uid, cid, type)
    if type != 400:
        Classic.give_like(cid)
    return Success()


@api.route('/cancel', methods=['POST'])
@token_decorator
def cancel_like():
    uid = g.user.uid
    form = LikeForm().validate_for_api()
    cid = form.data["art_id"]
    type = form.data["type"]
    Tap.cancel_like(uid, cid, type)
    if type != 400:
        Classic.cancel_like(cid)
    return Success()
