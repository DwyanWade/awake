"""
Created on 2018/6/6 0:43

"""
from flask import request, jsonify, g

from app.libs.http_qiyue import Http
from app.libs.redprint import RedPrint
from app.libs.token_auth import token_decorator
from app.models.tap import Tap
from app.validators.forms import BookSearchForm, CommentForm

__Author__ = '阿强'

api = RedPrint('book')


@api.route('/hot_list', methods=['GET'])
def get_hot_list():
    http = Http()
    res = http.get_hot_list()
    return jsonify(res)


@api.route('/add/short_comment', methods=['POST'])
def book_comment():
    form = CommentForm().validate_for_api()
    book_id = form.data["book_id"]
    content = form.data["content"]
    http = Http()
    res = http.book_comment(book_id, content)
    return jsonify(res)


@api.route('/<int:book_id>/short_comment', methods=['GET'])
def get_book_comment(book_id):
    http = Http()
    res = http.get_book_comment(book_id)
    return jsonify(res)


@api.route('/favor/count', methods=['GET'])
@token_decorator
def get_book_favor():
    uid = g.user.uid
    book_list = Tap.query.filter(Tap.type == 400, Tap.uid == uid, Tap.status == 1).all()
    count = len(book_list)
    return jsonify({"count": count})


@api.route('/<int:book_id>/favor', methods=['GET'])
@token_decorator
def book_favor_info(book_id):
    uid = g.user.uid
    http = Http()
    fav_nums = http.get_like_info(book_id)
    book_like_info = Tap.query.filter_by(uid=uid, type=400, cid=book_id).first()
    if book_like_info is None:
        like_status = 0
    else:
        like_status = 1
    return jsonify({
        "fav_nums": fav_nums,
        "id": book_id,
        "like_status": like_status
    })


@api.route('/hot_keyword', methods=['GET'])
def get_hot_keyword():
    http = Http()
    res = http.get_hot_keyword()
    return jsonify(res)


@api.route('/<int:id>/detail', methods=['GET'])
def get_detail(id):
    http = Http()
    res = http.get_detail(id)
    return jsonify(res)


@api.route('/search', methods=['GET'])
def search():
    form = BookSearchForm().validate_for_api()
    start = form.start.data
    count = form.count.data
    summary = form.summary.data
    q = form.q.data
    http = Http()
    res = http.book_search(start, count, summary, q)
    return jsonify(res)
