'''
Created on Dec 18, 2012
Adopted from sgd2 Biorelation by kpaskov
@author: hitz
'''
from . import Base, ENCODEdTableMixin, CommonEqualityMixin
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table, Column, ForeignKey
from sqlalchemy.types import Integer, String, Date, Float, Enum, Boolean


class Biosample(Base, ENCODEdTableMixin, CommonEqualityMixin):
    ''' doc string for lintness'''

    __tablename__ = "biosample"

    id = Column('biosample_no', Integer, primary_key=True)
    accession = Column('biosample_acc', String, nullable=False)
    type = Column('biosample_type', String, nullable=False)
    source_no = Column('source_no', Integer, ForeignKey('source.source_no'),
        nullable=False)
    product_no = Column('product_no', String, nullable=False)
    lot_no = Column('lot_no', String)
    submitted_by = Column('submitted_by', String, nullable=False)
    treatment_no = Column('treatment_no', Integer,
        ForeignKey('treatment.treatment_no'))

    ''' should below be CV tables?  Don't have to load the whole thing '''
    ontology = Column('ontology', Enum('UBERON', 'CLO', 'EFO',
        name='biosample_ontologies'), nullable=False)
    ontology_no = Column('ontology_no', String, nullable=False)
    ontology_term = Column('ontology_term', String, nullable=False)

    source = relationship('Source', uselist=False)

    treatment = relationship('Treatment', uselist=False)
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
    id = Column('biosample_no', Integer, ForeignKey('biosample.biosample_no'), primary_key=True)

    organism_no = Column(Integer, ForeignKey('organism.organism_no'))
    organism = relationship('Organism', uselist=False, backref='cell_line')

    growth_protocol_no = Column(Integer, ForeignKey('protocol.protocol_no'))
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
    id = Column('biosample_no', Integer, ForeignKey('biosample.biosample_no'), primary_key=True)

    date_obtained = Column('date_obtained', Date, nullable=False)
    donor_no = Column(Integer, ForeignKey('donor.donor_no'))
    donor = relationship('Donor', uselist=False, backref='tissues')

    extraction_protocol_no = Column(Integer, ForeignKey('protocol.protocol_no'))
    extraction_protocol = relationship('Protocol', primaryjoin=
        "and_(Tissue.extraction_protocol_id==Protocol.id, "
        "Protocol.type.equals('extraction'))", backref='tissues')

    __mapper_args__ = {'polymorphic_identity': "Tissue"}


class SingleCell(Tissue):

    ''' is this too deep? '''
    __tablename__ = 'single_cell'
    id = Column('biosample_no', Integer, ForeignKey('tissue.biosample_no'), primary_key=True)

    validation_documents = relationship('Document')  # unspec'd many-to-many!

    purification_protocol_no = Column(Integer, ForeignKey('protocol.protocol_no'))
    purification_protocol = relationship('Protocol', primaryjoin=
        "and_(SingleCell.purification_protocol_id==Protocol.id, "
        "Protocol.type.equals('purification'))", backref='singlecells')

    excision_protocol_no = Column(Integer, ForeignKey('protocol.protocol_no'))
    excision_protocol = relationship('Protocol', primaryjoin=
        "and_(SingleCell.excision_protocol_id==Protocol.id, "
        "Protocol.type.equals('excision'))", backref='singlecells')

    __mapper_args__ = {'polymorphic_identity': "Single Cell"}


class IPStemCellLine(CellLine):

    __tablename__ = 'ipstemcell_line'
    id = Column('biosample_no', Integer, ForeignKey('cell_line.biosample_no'), primary_key=True)

    derived_from = relationship('BiosampleRelation',
        primaryjoin='BiosampleRel.related_biosample_id==Biosample.id',
        uselist=False,
        )

    __mapper_args__ = {'polymorphic_identity': "Induced Pluripotent Stem Cell"}

    ''' must be derived from Biosample where type='Tissue', inherits growth
        protocol from CellLine, inherits donor '''


class BiosampleRel(Base, ENCODEdTableMixin):

    __tablename__ = 'biosample_relationship'
    id = Column('biosample_rel_no', Integer, primary_key=True)
    type = Column('biosample_type', String)
    biosample_no = Column(Integer, ForeignKey('biosample.biosample_no'))
    related_biosample_no = Column(Integer, ForeignKey('biosample.biosample_no'))


class Treatment(Base, ENCODEdTableMixin):

    __tablename__ = 'treatment'
    id = Column('treatment_no', Integer, primary_key=True)
    name = Column('treatment_name', String, nullable=False)
    description = Column('treatment_description', String)
    submitted_by = Column('submitted_by', String, nullable=False)

    details = relationship("TreatmentDetails",
                    secondary='treat_treat_details',
                    backref="treatments")


class TreatmentDetails(Base):

    __tablename__ = 'treatment_details'
    ''' should below be CV tables?  Don't have to load the whole thing '''
    id = Column('treatment_details_no', Integer, primary_key=True)
    ontology = Column('ontology', Enum('ChEBI', 'Protein',
        name='treatment_ontologies'), nullable=False)
    ontology_no = Column('ontology_no', String, nullable=False)
    ontology_term = Column('ontology_term', String, nullable=False)

    concentration = Column('concentration', Float)
    concentration_units = Column('concentration_units', Enum(
        'mM', 'uM', 'nM', 'pm', 'mg/ml', 'ug/ml', 'ng/ml', 'U/ml', 'percent',
        name='conc_units'))
    duration = Column('duration', Float)
    duration_units = Column('duration_units', Enum('s', 'm', 'hr', 'd',
        name='time_units'))
    # duration/duration_units could also be a DateTime or Interval obj.


## this could also use the Association object pattern from SQLA
treat_treat_details = Table('treat_treat_details', Base.metadata,
    Column('treat_treat_details_no', Integer, primary_key=True),
    Column('details_no', Integer, ForeignKey('treatment_details.treatment_details_no')),
    Column('treatment_no', Integer, ForeignKey('treatment.treatment_no')))

