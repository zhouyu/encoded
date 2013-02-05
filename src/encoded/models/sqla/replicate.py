'''
Created on Jan 30, 2012
@author: hitz
'''
from . import Base, ENCODEdTableMixin
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table, Column, ForeignKey
from sqlalchemy.types import Integer, String, Date, Float, Enum


class Replicate(Base, ENCODEdTableMixin):
    __tablename__ = 'replicate'
    id = Column('replicate_no', Integer, primary_key=True)

    type = Column(assay_type, Enum('ChIP-seq', 'RNA-seq', 'RIP-seq', 'ChIA-PET',
        '5C', 'shRNA-RNA-seq', 'DNase-DGF', 'Whole-genome bisulfite sequencing',
        'RAMPAGE', 'Methyl-RRBS', 'Methyl-450', 'in vitro SELEX', 'Enhancer',
        name='assay_types'), nullable=False)

    library_no = Column(Integer, ForeignKey('library.library_no'), nullable=False)
    file_no = Column(Integer, ForeignKey('file.file_no'), nullable=False)

    antibody_no = Column(Integer, ForeignKey('antibody.antibody_no'))
    '''IP experiments only'''
    target_no = Column(Integer, ForeignKey('target.target_no'))
    ''' IP or shRNA experiments only'''

    platform_no = Column(Integer, ForeignKey('platform.platform_no'))
    ''' would be nullable except for Enhancer!'''

    biological_replicate_no = Column(Integer, nullable=False)
    technical_replicate_no = Column(Integer, nullable=False)
    ''' usually 1 or 2 '''

    submitted_by = Column(String, nullable=False)
    ''' foreign key to submitter table? '''


class Library(Base, ENCODEdTableMixin):
    ''' a nucleic acid library for sequencing '''
    __tablename__ = 'library'
    id = Column('library_no', Integer, primary_key=True)

    type = Column('library_type', Enum('DNA', 'RNA', name='library_types'),
        nullable=False)

    biosample_no = Column(Integer, ForeignKey('biosample.biosample_no'),
        nullable=False)
    '''  asssumes libraries are not pooled after extraction '''

    ''' needs dbxrefs for LIMS like functionality'''



