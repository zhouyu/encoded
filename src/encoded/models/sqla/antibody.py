'''
Created on Jan 24, 2013
@author: hitz
'''

from . import Base, ENCODEdTable
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Enum


class Antibody(Base, ENCODEdTable):

    __tablename__ = 'antibody'

    id = Column('antibody_id', Integer, primary_key=True)
    accession = Column('antibody_accession', String, nullable=False)
    source_id = Column('source_id', Integer, ForeignKey('source.source_id'))
    product_id = Column('product_id', String, nullable=False)
    lot_id = Column('lot_id', String)
    submitted_by = Column('submitted_by', String, nullable=False)
    isotype = Column('isotype', String)
    clonality = Column('clonality',
        Enum('monoclonal', 'polyclonal', name='antibody_clonality'))
    purification = Column('purification', String)
    antigen_description = Column('antigen_description', String)
    epitope = Column('epitope', String)
    host_organism_id = Column('host_organism_id',
        ForeignKey('organism.organism_id'))


class Target(Base, ENCODEdTable):

    __tablename__ = 'target'

    id = Column('target_id', Integer, primary_key=True)
    label = Column('target_label', String, nullable=False)
    label_stem = Column('lable_stem', String)
    symbol = Column('symbol', String, nullable=False)
    organism_id = Column('organism_id', ForeignKey('organism.organism_id'),
        nullable=False)
    target_class = Column('target_class', String)  # GO Molecular Function SLIM
    modification_id = Column('modification_id', Integer,
        ForeignKey('modification.modification_id'))  # nullable FK

    modification = relationship('Modification', uselist=False)


class Modification(Base, ENCODEdTable):

    __tablename__ = 'modification'

    id = Column('modification_id', Integer, primary_key=True)
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


class Validation(Base, ENCODEdTable):

    __tablename__ = 'validation'

    id = Column('validation_id', Integer, primary_key=True)
    antibody_id = Column('antibody_id', ForeignKey('antibody.antibody_id'),
        nullable=False)
    target_id = Column('target_id', Integer, ForeignKey('target.target_id'),
        nullable=False)
    status = Column('validation_status', Enum('validated', 'not validated',
        'invalid', name='validation_states'))

    documents = relationship('ValidationDocument', backref='validation')


class ValidationDocument(Base, ENCODEdTable):

    __tablename__ = 'validation_document'

    id = Column('validation_document_id', Integer, primary_key=True)
    method = Column('method',
        Enum('ENCODE2', 'To be added',  # special autovalidation)
        'Immunoflurescense', 'Immunoprecipitation', 'Western Blot',
        'Correlation', 'Mass-Spec', name='antibody_validation_methods'),
        nullable=False)
    document_id = Column('document_id', ForeignKey('document.document_id'))
    status = Column('review_status',
        Enum('submitted', 'change_request', 'approved', 'rejected',
        name='review_states'), nullable=False)
    reviewed_by = Column('reviewed_by', String)  # FK to Colleague????


