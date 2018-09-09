"""
Created on 2018/8/16 22:25

"""
import requests

from flask import json, jsonify

__Author__ = '阿强'


class Http:
    base_url = "http://bl.7yue.pro/v1/book/"
    headers = {
        'Content-Type': 'application/json',
        'appkey': '6ywqG4caNqUBoLaG'
    }

    def book_comment(self, book_id, content):
        data = {
            'book_id': book_id,
            'content': content
        }
        url = self.base_url + 'add/short_comment'
        data = json.dumps(data)
        res = requests.post(url, data=data, headers=self.headers)
        res = res.content
        res = json.loads(res)
        return res

    def get_hot_list(self):
        res = self.public_request('hot_list')
        return res

    def get_book_comment(self, book_id):
        url = str(book_id) + '/short_comment'
        res = self.public_request(url)
        return res

    def get_like_info(self, book_id):
        url = str(book_id) + '/favor'
        res = self.public_request(url)
        return res['fav_nums']

    def get_hot_keyword(self):
        res = self.public_request('hot_keyword')
        return res

    def get_detail(self, id):
        url = str(id) + '/detail'
        res = self.public_request(url)
        return res

    def book_search(self, start, count, summary, q):
        params = {
            'start': start,
            'count': count,
            'summary': summary,
            'q': q
        }
        res = self.public_request('search', params)
        return res

    def public_request(self, url, params=None):
        url = self.base_url + url
        res = requests.get(url, params=params, headers=self.headers)
        res = res.content
        res = json.loads(res)
        return res

