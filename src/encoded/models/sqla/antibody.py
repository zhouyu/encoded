'''
Created on Jan 24, 2013
@author: hitz
'''

from . import Base, ENCODEdTable, CommonEqualityMixin
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table, Column, ForeignKey
from sqlalchemy.types import Integer, String, Date, Float, Enum, Boolean


class Antibody(Base, ENCODEdTable):

    __tablename__ = 'antibody'

    id = Column('antibody_id', Integer, primary_key=True)
    source_id = Column('source_id', Integer, ForeignKey('source.source_id'))
    product_id = Column('product_id', String, nullable=False)
    lot_id = Column('lot_id', String)
    submitted_by = Column('submitted_by', String, nullable=False)
    isotype = Column('isotype', String)
    clonality = Column('clonality',
        Enum('monoclonal', 'polyclonal', name=antibody_clonality))
    purification = Column('purification', String)
    antigen_description = Column('antigen_description', String)
    epitope = Column('epitope', String)
    host_organism_id = Column('host_organism_id',
        ForeignKey('organism.organism_id'))


class Target(Base, ENCODEdTable):

    __tablename__ = 'target'

    id = Column('target_id', Integer, primary_key=True)
    label = Column('target_label', String, nullable=False)
    symbol = Column('symbol', String, nullable=False)
    organism_id = Column('organism_id', ForeignKey('organism.organism_id'),
        nullable=False)
    target_class = Column('target_class', String)  ## GO Molecular Function SLIM


class Modification(Base, ENCODEdTable):

    __tablename__ = 'modification'

    id = Column('modification_id', Integer, primary_key=True)
    type = Column('modification_type', nullable=False,
        Enum('fusion', 'acetylation', 'phosphoryation', 'ubiquitinylation',
        'monomethlyation', 'dimethylation', 'trimethlyation'))
    ''' should fusion be specific or general '''
    position = Column('position', Integer)
    residue = Column('residue', Enum('E', 'K', 'R', 'D', 'S', 'T', 'C', 'H',
        name='modifiable_amino_acids'))


## this could also use the Association object pattern from SQLA
target_modification = Table('target_modification', Base.metadata,
    Column('target_id', Integer, ForeignKey('target.target_id')),
    Column('modification_id', Integer, ForeignKey('modification.modification_id')))


class Validation(Base, ENCODEdTable):

    __tablename__ = 'validation'

    id = Column('validation_id', Integer, primary_key=True)
    type = Column('validation_type', nullable=False,
        Enum('antibody'), name='validation_types')
    # above is a place holder for further validation types
    # this will require some subclassing

    method = Column('method', nullable=False,
        Enum('ENCODE2', 'To be added',  # special autovalidation)
        'Immunoflurescense', 'Immunoprecipitation', 'Western Blot',
        'Correlation', 'Mass-Spec', name='antibody_validation_methods'))
    document_id = Column('document_id', ForeignKey('document.document_id'))
    status = Column('validation_status', nullable=False,
        Enum('submitted', 'needs_review', 'approved', 'rejected'),
        name='validation_states')
    reviewer = Column('reviewer', String)  # FK to Colleague????
    antibody_id = Column('antibody_id', ForeignKey('antibody.antibody_id'))
    ## ug this would be shRNA by type unless we subclass
    target_id = Column('target_id', Integer, ForeignKey('target.target_id'))


