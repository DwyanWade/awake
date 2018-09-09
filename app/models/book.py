"""
Created on 2018/8/15 23:15

"""
from sqlalchemy import PickleType, Column, Integer

from app.models.base import Base

__Author__ = '阿强'


class Book(Base):
    id = Column(Integer, primary_key=True)
    test_list = Column(PickleType)
    test_dict = Column(PickleType)

    def keys(self):
        return ['id', 'test_list', 'test_dict', 'create_time', 'status']