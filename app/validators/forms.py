"""
Created on 2018/6/6 23:04

"""
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError, NumberRange

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form

__Author__ = '阿强'


class ClientForm(Form):
    code = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=60)])
    secret = StringField()
    # type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')])
    secret = StringField(validators=[DataRequired(), Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()


class BookSearchForm(Form):
    start = IntegerField(default=0)
    count = IntegerField(default=20)
    summary = IntegerField(default=0)
    q = StringField(validators=[DataRequired()])


class IndexForm(Form):
    index = IntegerField(validators=[DataRequired()])


class LikeForm(Form):
    art_id = IntegerField(validators=[DataRequired()])
    type = IntegerField(validators=[DataRequired()])


class CommentForm(Form):
    book_id = IntegerField(validators=[DataRequired()])
    content = StringField(validators=[DataRequired(), length(min=2, max=22)])
