'''
Created on Dec 20, 2012
@author: hitz
'''
from models.sqla import ENCODEdTable
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Enum

class Source(ENCODEdTable):

    __tablename__ = 'source'
    id = Column('source_id', Integer, PrimaryKey=True)
    name = Column('source_name', String, nullable=False)
    url_id = Column('url_id', Integer, ForeignKey('url.url_id'))

    url = relationship('Url', useList=False, backref='source')


class Url(ENCODEdTable):

    __tablename__ = 'url'
    id = Column('url_id', Integer, PrimaryKey=True)
    type = Column('url_type', Enum, nullable=False)
    url = Column('url', String, nullable=False)
