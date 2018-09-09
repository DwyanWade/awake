"""
Created on 2018/6/6 0:45

"""
from flask import Blueprint
from app.api.v1 import user, book, client, classic, like

__Author__ = '阿强'


def create_blueprint_v1():
    bp_vi = Blueprint('v1', __name__)
    user.api.register(bp_vi)
    book.api.register(bp_vi)
    client.api.register(bp_vi)
    classic.api.register(bp_vi)
    like.api.register(bp_vi)
    return bp_vi
