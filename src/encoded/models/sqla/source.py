'''
Created on Dec 20, 2012
@author: hitz
'''
from . import Base, ENCODEdTableMixin
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy import Sequence

class Source(Base, ENCODEdTableMixin):

    __tablename__ = 'source'
    id = Column('source_no', Integer, Sequence('source_no_seq'), primary_key=True)
    name = Column('source_name', String, nullable=False)
    url_no = Column('url_no', Integer, ForeignKey('url.url_no'))

    url = relationship('Url', uselist=False, backref='source')


class Url(Base, ENCODEdTableMixin):

    __tablename__ = 'url'
    id = Column('url_no', Integer, Sequence('url_no_seq'), primary_key=True)
    type = Column('url_type', String, nullable=False)
    url = Column('url', String, nullable=False)
