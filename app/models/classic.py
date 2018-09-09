"""
Created on 2018/8/1 23:44

"""
from sqlalchemy import Column, Integer, String

from app.models.base import Base, db

__Author__ = '阿强'


class Classic(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(50))
    fav_nums = Column(Integer, default=0)
    image = Column(String(100))
    index = Column(Integer)
    pubdate = Column(String(24))
    title = Column(String(50), default="未名")
    url = Column(String(100), default="no")
    type = Column(Integer)

    def keys(self):
        return ['id', 'content', 'fav_nums', 'image',
                'index', 'pubdate', 'title', 'url', 'type', 'like_status']

    @staticmethod
    def give_like(cid):
        with db.auto_commit():
            classic = Classic.query.filter_by(id=cid).first()
            classic.fav_nums += 1

    @staticmethod
    def cancel_like(cid):
        with db.auto_commit():
            classic = Classic.query.filter_by(id=cid).first()
            classic.fav_nums -= 1
