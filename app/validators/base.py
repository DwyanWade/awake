"""
Created on 2018/6/8 22:34

"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__Author__ = '阿强'


class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
