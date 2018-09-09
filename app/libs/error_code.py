"""
Created on 2018/6/7 23:36

"""

from app.libs.error import APIException

__Author__ = '阿强'


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    msg = 'delete success'
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry, Newserver make a mistake'
    error_code = 990


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found ^0__0^……'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden not scope'


class RepeatError(APIException):
    code = 302
    error_code = 1007
    msg = 'you have already like the classic'
