'''
Created on Dec 20, 2012
@author: hitz
'''
from . import Base, ENCODEdTableMixin
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, LargeBinary, Enum


class Protocol(Base, ENCODEdTableMixin):
    ''' currently only biosample related protocols are mapped, there may be
        software, treatment, or other protocols added '''

    __tablename__ = 'protocol'
    id = Column('protocol_no', Integer, primary_key=True)
    name = Column('protocol_name', String, nullable=False)
    type = Column('protocol_type',
        Enum('growth', 'extraction', 'excision', 'purification',
        name='protocol_types'), nullable=False)
    description = Column('protocol_description', String)
    document_no = Column('document_no', Integer,
        ForeignKey('document.document_no'), nullable=False)
    document = relationship('Document', uselist=False)
    submitted_by = Column('submitted_by', String, nullable=False)


class Document(Base, ENCODEdTableMixin):

    __tablename__ = 'document'
    id = Column('document_no', Integer, primary_key=True)
    type = Column('document_type',
        Enum('pdf', 'doc', 'docx', 'rtf', 'txt', 'rst',
        name='document_file_types'), nullable=False)

    ## either file_location or documment blob != null but both?
    file_location = Column('file_location', String)
    document = Column('document', LargeBinary)
