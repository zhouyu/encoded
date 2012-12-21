'''
Created on Dec 18, 2012
Adopted from sgd2 Biorelation by kpaskov
@author: hitz
'''
from models.sqla import ENCODEdTable, CommonEqualityMixin
import models.sqla.protocol
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Date, Float, Enum, Boolean


class Biosample(ENCODEdTable, CommonEqualityMixin):
    ''' doc string for lintness'''

    __tablename__ = "biosample"

    id = Column('biosample_id', Integer, primary_key=True)
    type = Column('biosample_type', String, nullable=False)
    source_id = Column('source_id', Integer, ForeignKey('source.source_id'))
    product_id = Column('product_id', String, nullable=False)
    lot_id = Column('lot_id', String)
    submitted_by = Column('submitted_by', String, nullable=False)

    ''' should below be CV tables?  Don't have to load the whole thing '''
    ontology = Column('ontology', Enum('UBERON', 'CLO', 'EFO'),
        nullable=False)
    ontology_id = Column('ontology_id', String, nullable=False)
    ontology_term = Column('ontology_term', String, nullable=False)

    source = relationship('Source', uselist=False)

    treatments = relationship('Treatment', secondary=biosample_treatment,
        backref='biosamples')
    ## any Biosample can be chemically treated

    related_biosamples = relationship('BiosampleRel',
        primaryjoin="BiosampleRelbiosample_id==Biosample.id"
    )

    '''should be a list of Biosmaple_rel.related_biosample_id
       could this be broken up by type:
       derived_from = BiosampleRel(related) where type=derived?
       derivatives = BiosampleRel(id) where type=derived
    '''

    __mapper_args__ = {'polymorphic_on': type,
                       'polymorphic_identity': "Biosample",
                       'with_polymorphic': '*'}

    def __init__(self):
        pass

    def __repr__(self):
        pass


class CellLine(Biosample):
    __tablename__ = 'cell_line'
    id = Column(Integer, ForeignKey('biosample.biosample_id'), primaryKey=True)

    organism_id = Column(Integer, ForeignKey('organism.organism_id'))
    organism = relationship('Organism', uselist=False, backref='cell_line')

    growth_protocol_id = Column(Integer, ForeignKey('protocol.protocol_id'))
    growth_protocol = relationship('Protocol', primaryjoin=
        "and_(CellLine.growth_protocol_id==Protocol.id, "
        "Protocol.type.equals('growth'))", backref='cellines')

    is_stable = Column('is_stable', Boolean, nullable=False)
    construct = relationship('Construct', backref='cellines')

    ''' otherwise add "Primary Cell Line" subtype '''

    __mapper_args__ = {'polymorphic_identity': "Cell Line"}


class Tissue(Biosample):
    ''' includes "whole mouse" which will typically have transfection construct/treatment'''
    __tablename__ = 'tissue'
    id = Column(Integer, ForeignKey('biosample.biosample_id'), primaryKey=True)

    date_obtained = Column('date_obtained', Date, nullable=False)
    donor_id = Column(Integer, ForeignKey('human_donor.id'))
    donor = relationship('HumanDonor', useList=False, backref='tissues')
    ''' this doesn't handle mouse right at all!!! '''

    extraction_protocol_id = Column(Integer, ForeignKey('protocol.protocol_id'))
    extraction_protocol = relationship('Protocol', primaryjoin=
        "and_(Tissue.extraction_protocol_id==Protocol.id, "
        "Protocol.type.equals('extraction'))", backref='tissues')

    __mapper_args__ = {'polymorphic_identity': "Tissue"}


class SingleCell(Tissue):

    ''' is this too deep? '''
    __tablename__ = 'single_cell'
    id = Column(Integer, ForeignKey('tissue.id'), primaryKey=True)

    validation_documents = relationship('Document')  ## unspec'd many-to-many!

    purification_protocol_id = Column(Integer, ForeignKey('protocol.protocol_id'))
    purification_protocol = relationship('Protocol', primaryjoin=
        "and_(SingleCell.purification_protocol_id==Protocol.id, "
        "Protocol.type.equals('purification'))", backref='singlecells')

    excision_protocol_id = Column(Integer, ForeignKey('protocol.protocol_id'))
    excision_protocol = relationship('Protocol', primaryjoin=
        "and_(SingleCell.excision_protocol_id==Protocol.id, "
        "Protocol.type.equals('excision'))", backref='singlecells')

    __mapper_args__ = {'polymorphic_identity': "Single Cell"}


class IPStemCellLine(CellLine):

    __tablename__ = 'ipstemcell_line'
    id = Column(Integer, ForeignKey('cell_line.id'), primaryKey=True)

    derived_from = relationship('BiosampleRelation',
        primaryJoin=BiosampleRel.related_biosample_id==Biosample.id,
        useList=False,
        )

    __mapper_args__ = {'polymorphic_identity': "Induced Pluripotent Stem Cell"}

    ''' must be derived from Biosample where type='Tissue', inherits growth
        protocol from CellLine, inherits donor '''


class Organism(ENCODEdTable):

    __tablename__ = 'organism'
    id = Column('organism_id', Integer, PrimaryKey=True)
    name = Column('organism_name', String, nullable=False)
    taxon_id = Column('taxon_id', Integer, nullable=False)


class Donor(ENCODEdTable):

    __tablename__ = 'donor'
    id = Column('donor_id', Integer, PrimaryKey=True)
    organism_id = Column('organism_id', Integer,
        ForeignKey('organism.organism_id'))
    organism = relationship(Organism, useList=False, backref='donors')
    age = Column('age', String)
    gender = Column('gender', Enum('Male', 'Female', 'Unknown'))

    __mapper_args__ = {'polymorphic_on': organism.name,
                       'polymorphic_identity': "Donor",
                       'with_polymorphic': '*'}


class MouseDonor(Donor):
    __tablename__ = 'mouse_donor'
    id = Column(Integer, ForeignKey('donor.donor_id'), primaryKey=True)
    strain = Column('strain', String)

    __mapper_args__ = {'polymorphic_identity': "Mus musculus"}


class HumanDonor(Donor):

    __tablename__ = 'human_donor'
    id = Column(Integer, ForeignKey('donor.donor_id'), PrimaryKey=True)
    ethnicity = Column('ethnicity', Enum)
    health_status = Column('health_status', String)
    external_id = Column('external_donor_id', Integer)

    __mapper_args__ = {'polymorphic_identity': "Homo sapiens"}


class BiosampleRel(ENCODEdTable):

    __tablename__ = 'biosample_relationship'
    id = Column('biosample_rel_id', Integer, PrimaryKey=True)
    type = Column('biosample_type', String)
    biosample_id = Column(Integer, ForeignKey('biosample.id'))
    related_biosample_id = Column(Integer, ForeignKey('biosample.id'))


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


## this could also use the Association object pattern from SQLA
biosample_treatment = Table('biosample_treatment', Base.metadata,
    Column('biosample_id', Integer, ForeignKey('biosample.biosample_id')),
    Column('treatment_id', Integer, ForeignKey('treatment.treatment_id')))
)

class Treatment(ENCODEdTable):
    ''' Assuming we are only using Chemical treatments in ChEBI
        This may be an unwarrented assumptions in which case we will
        have to add an Ontology/CV foreign key instead, or else break
        this into "chemical" treatments and "other" treatments '''

    __tablename__ = 'treatment'
    id = Column('treatment_id', Integer, PrimaryKey=true)
    name = Column('treatment_name', String, nullable=False)
    chebi_id = Column('chebi_id', String, nullable=False)
    concentration = Column('concentration', Float)
    concentration_units = Column('concentration_units', Enum)
    duration = Column('duration', Float)
    duration_units = Column('duration_units', Enum)

    submitted_by = Column('submitted_by', String, nullable=False)

