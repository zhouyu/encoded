'''
Created on Jan 24, 2013
@author: hitz
'''

from . import Base, ENCODEdTableMixin
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Enum


class Antibody(Base, ENCODEdTableMixin):

    __tablename__ = 'antibody'

    id = Column('antibody_no', Integer, primary_key=True)
    accession = Column('antibody_acc', String, nullable=False)
    source_no = Column('source_no', Integer, ForeignKey('source.source_no'))
    product_no = Column('product_no', String, nullable=False)
    lot_no = Column('lot_no', String)
    submitted_by = Column('submitted_by', String, nullable=False)
    isotype = Column('isotype', String)
    clonality = Column('clonality',
        Enum('monoclonal', 'polyclonal', name='antibody_clonality'))
    purification = Column('purification', String)
    antigen_description = Column('antigen_description', String)
    epitope = Column('epitope', String)
    host_organism_no = Column('host_organism_no',
        ForeignKey('organism.organism_no'))


class Target(Base, ENCODEdTableMixin):

    __tablename__ = 'target'

    id = Column('target_no', Integer, primary_key=True)
    label = Column('target_label', String, nullable=False)
    label_stem = Column('lable_stem', String)
    symbol = Column('symbol', String, nullable=False)
    organism_no = Column('organism_no', ForeignKey('organism.organism_no'),
        nullable=False)
    target_class = Column('target_class', String)  # GO Molecular Function SLIM
    modification_no = Column('modification_no', Integer,
        ForeignKey('modification.modification_no'))  # nullable FK

    modification = relationship('Modification', uselist=False)


class Modification(Base, ENCODEdTableMixin):

    __tablename__ = 'modification'

    id = Column('modification_no', Integer, primary_key=True)
    type = Column('modification_type',
        Enum('GFP-fusion', 'acetylation', 'phosphoryation', 'ubiquitinylation',
        'monomethlyation', 'dimethylation', 'trimethlyation',
        name='modification_types'), nullable=False)
    ''' should fusion be specific or general '''
    position = Column('position', Integer)
    residue = Column('residue', Enum('E', 'K', 'R', 'D', 'S', 'T', 'C', 'H',
        name='modifiable_amino_acids'))

    def _create_label(self):

        short_types = {
            'GFP-fusion': '-GFP',
            'acetylation': 'ac',
            'phosphorylation': 'P',
            'ubquitnylation': '-Ubi',
            'monomethylation': 'me',
            'dimethylation': 'me2',
            'trimethylation': 'me3'
        }

        return str(self.position + self.residue + short_types[self.type])


class Validation(Base, ENCODEdTableMixin):

    __tablename__ = 'validation'

    id = Column('validation_no', Integer, primary_key=True)
    antibody_no = Column('antibody_no', ForeignKey('antibody.antibody_no'),
        nullable=False)
    target_no = Column('target_no', Integer, ForeignKey('target.target_no'),
        nullable=False)
    status = Column('validation_status', Enum('validated', 'not validated',
        'invalid', name='validation_states'))


class ValidationDocument(Base, ENCODEdTableMixin):

    __tablename__ = 'validation_document'

    id = Column('validation_document_no', Integer, primary_key=True)
    validation_no = Column('validation_no', Integer, ForeignKey('validation.validation_no'))
    method = Column('method',
        Enum('ENCODE2', 'To be added',  # special autovalidation)
        'Immunoflurescense', 'Immunoprecipitation', 'Western Blot',
        'Correlation', 'Mass-Spec', name='antibody_validation_methods'),
        nullable=False)
    document_no = Column('document_no', ForeignKey('document.document_no'))
    status = Column('review_status',
        Enum('submitted', 'change_request', 'approved', 'rejected',
        name='review_states'), nullable=False)
    reviewed_by = Column('reviewed_by', String)  # FK to Colleague????

    validation = relationship('Validation', uselist=False, backref='documents')


