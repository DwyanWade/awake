"""
Created on 2018/8/7 22:19

"""
from flask import jsonify, g, request
from sqlalchemy import desc

from app.libs.redprint import RedPrint
from app.libs.token_auth import token_decorator
from app.models.classic import Classic
from app.models.tap import Tap

__Author__ = '阿强'

api = RedPrint('classic')


@api.route('/latest', methods=['GET'])
@token_decorator
def get_latest():
    uid = g.user.uid
    classic = Classic.query.order_by(desc(Classic.index)).first()
    classic.like_status = Tap.check_like_status(uid, classic.id, classic.type)
    return jsonify(classic)


@api.route('/<int:index>/next', methods=['GET'])
@token_decorator
def get_next(index):
    uid = g.user.uid
    index = index + 1
    classic = Classic.query.filter_by(index=index).first()
    classic.like_status = Tap.check_like_status(uid, classic.id, classic.type)
    return jsonify(classic)


@api.route('/<int:type>/<int:id>', methods=['GET'])
@token_decorator
def get_classic_by_id(type, id):
    uid = g.user.uid
    classic = Classic.query.filter_by(id=id).first()
    classic.like_status = Tap.check_like_status(uid, classic.id, type)
    return jsonify(classic)


@api.route('/<int:index>/previous', methods=['GET'])
@token_decorator
def get_previous(index):
    uid = g.user.uid
    index = index - 1
    classic = Classic.query.filter_by(index=index).first()
    classic.like_status = Tap.check_like_status(uid, classic.id, classic.type)
    return jsonify(classic)


@api.route('/favor', methods=['GET'])
@token_decorator
def get_my_classic():
    uid = g.user.uid
    my_favor_classic = []
    tap_list = Tap.query.filter(Tap.type != 400, Tap.uid == uid, Tap.status == 1).all()
    for tap in tap_list:
        classic = Classic.query.filter_by(id=tap.cid).first()
        classic.like_status = 1
        my_favor_classic.append(classic)
    return jsonify(my_favor_classic)


@api.route('/<int:type>/<int:id>/favor', methods=['GET'])
@token_decorator
def get_like_info(type, id):
    uid = g.user.uid
    classic = Classic.query.filter_by(id=id).first()
    like_status = Tap.query.filter_by(uid=uid, type=type, cid=id).first()
    if like_status is None:
        like_status = 0
    else:
        like_status = 1
    return jsonify({
        "fav_nums": classic.fav_nums,
        "id": id,
        "like_status": like_status
    })
