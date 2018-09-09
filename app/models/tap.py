"""
Created on 2018/8/3 0:12

"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.libs.error_code import RepeatError
from app.models.base import Base, db

__Author__ = '阿强'


class Tap(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    # classic = relationship('Classic')
    uid = Column(Integer, ForeignKey('user.id'))
    cid = Column(Integer)
    type = Column(Integer)

    @staticmethod
    def check_like_status(uid, cid, type):
        tap = Tap.query.filter_by(uid=uid, cid=cid, type=type).first()
        if tap:
            return 1
        else:
            return 0

    @staticmethod
    def tap_like(uid, cid, type):
        tap = Tap.query.filter_by(uid=uid, cid=cid, type=type).first()
        if tap:
            raise RepeatError()
        else:
            tap = Tap.query.filter_by(uid=uid, cid=cid, type=type, status=0).first()
            if tap:
                with db.auto_commit():
                    tap.status = 1
            else:
                with db.auto_commit():
                    tap = Tap()
                    tap.uid = uid
                    tap.cid = cid
                    tap.type = type
                    db.session.add(tap)

    @staticmethod
    def cancel_like(uid, cid, type):
        tap = Tap.query.filter_by(uid=uid, cid=cid, type=type).first()
        if tap:
            with db.auto_commit():
                tap.status = 0
        else:
            tap = Tap.query.filter_by(uid=uid, cid=cid, type=type, status=0).first()
            if tap:
                raise RepeatError(msg='you have already cancel like the art')
            else:
                raise RepeatError(msg='you never like the art')
