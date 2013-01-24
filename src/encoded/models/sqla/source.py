'''
Created on Dec 20, 2012
@author: hitz
'''
from . import Base, ENCODEdTable
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Enum

class Source(Base, ENCODEdTable):

    __tablename__ = 'source'
    id = Column('source_id', Integer, primary_key=True)
    name = Column('source_name', String, nullable=False)
    url_id = Column('url_id', Integer, ForeignKey('url.url_id'))

    url = relationship('Url', uselist=False, backref='source')


class Url(Base, ENCODEdTable):

    __tablename__ = 'url'
    id = Column('url_id', Integer, primary_key=True)
    type = Column('url_type', String, nullable=False)
    url = Column('url', String, nullable=False)
