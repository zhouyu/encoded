'''
Created on Dec 20, 2012
@author: hitz
'''
from models.sqla import ENCODEdTable, CommonEqualityMixin
import models.sqla.biosample
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Date, Float, Enum, Boolean


class Protocol(ENCODEdTable):
    ''' currently only biosample related protocols are mapped, there may be
        software, treatment, or other protocols added '''

    __tablename__ = 'protocol'
    id = Column('protocol_id', Integer, PrimaryKey=True)
    name = Column('protocol_name', String, nullable=False)
    type = Column('protocol_type', Enum(
        'growth', 'extraction', 'excision', 'purification'), nullable=False)
    description = Column('protocol_description', String)
    document_id = Column('document_id', Integer,
        ForeignKey='document.document_id', nullable=False)
    document = relationship('Document', useList=False)
    submitted_by = Column('submitted_by', String)


class Document(ENCODEdTable):

    __tablename__ = 'document'