'''
Created on Dec 20, 2012
@author: hitz
'''
from models.sqla import ENCODEdTable
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, LargeBinary, Enum


class Protocol(ENCODEdTable):
    ''' currently only biosample related protocols are mapped, there may be
        software, treatment, or other protocols added '''

    __tablename__ = 'protocol'
    id = Column('protocol_id', Integer, PrimaryKey=True)
    name = Column('protocol_name', String, nullable=False)
    type = Column('protocol_type',
        Enum('growth', 'extraction', 'excision', 'purification'),
        nullable=False)
    description = Column('protocol_description', String)
    document_id = Column('document_id', Integer,
        ForeignKey='document.document_id', nullable=False)
    document = relationship('Document', useList=False)
    submitted_by = Column('submitted_by', String, nullable=False)


class Document(ENCODEdTable):

    __tablename__ = 'document'
    id = Column('document_id', Integer, PrimaryKey=True)
    type = Column('document_type',
        Enum('pdf', 'doc', 'docx', 'rtf', 'txt', 'rst'),
        nullable=False)
    submitted_by = Column('submitted_by', String, nullable=False)

    ## either file_location or documment blob != null but both?
    file_location = Column('file_location', String)
    document = Column('document', LargeBinary)
