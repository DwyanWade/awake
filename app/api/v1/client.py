"""
Created on 2018/6/6 22:55

"""
from flask import request, app, jsonify, current_app, json
from urllib import request as _request
# from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError, Success, ServerError
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

__Author__ = '阿强'

api = RedPrint('client')


@api.route('/get', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    code = form.code.data
    token = __register(code)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def __register(code):
    appid = current_app.config['WX_APPID']
    app_secret = current_app.config['APP_SECRET']
    login_url = "https://api.weixin.qq.com/sns/jscode2session?appid=" + appid + "&secret=" + app_secret + "&js_code=" + \
                code + "&grant_type=authorization_code"
    # 向微信服务器发送请求
    token = __http_to_wx(login_url)
    return token


def __http_to_wx(url):
    res = _request.Request(url=url)
    res = _request.urlopen(res)
    res = res.read().decode('ascii')
    res = json.loads(res)
    if 'openid' in res.keys():
        uid = User.register(res['openid'])
        token = generate_auth_token(uid)
        return token
    else:
        raise ServerError(msg='获取openid时异，微信内部错误')


def generate_auth_token(uid, scope=None, expiration=3600):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'scope': scope
    })