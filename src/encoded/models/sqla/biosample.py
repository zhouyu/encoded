'''
Created on Dec 18, 2012
Adopted from sgd2 Biorelation by kpaskov
@author: hitz
'''
from . import Base, ENCODEdTableMixin, CommonEqualityMixin
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table, Column, ForeignKey
from sqlalchemy.types import Integer, String, Date, Float, Enum


class Biosample(Base, ENCODEdTableMixin, CommonEqualityMixin):
    ''' doc string for lintness'''

    __tablename__ = "biosample"

    id = Column('biosample_no', Integer, primary_key=True)
    accession = Column('biosample_acc', String, nullable=False)
    type = Column('biosample_type', Enum('Tissue', 'Cell Line', 'Single Cell',
        'Primary Cell Culture', 'Induced Pluripotent Stem Cell Line',
         name='biosample_types'), nullable=False)

    source_no = Column('source_no', Integer, ForeignKey('source.source_no'),
        nullable=False)
    product_no = Column('product_no', String, nullable=False)
    lot_no = Column('lot_no', String)

    submitted_by = Column('submitted_by', String, nullable=False)
    treatment_no = Column('treatment_no', Integer,
        ForeignKey('treatment.treatment_no'))

    ''' should below be CV tables?  Don't have to load the whole thing '''
    ontology = Column('ontology', Enum('UBERON', 'CL', 'EFO',
        name='biosample_ontologies'), nullable=False)
    ontology_id = Column('ontology_id', String, nullable=False)
    ontology_term = Column('ontology_term', String, nullable=False)

    source = relationship('Source', uselist=False)

    treatment = relationship('Treatment', uselist=False)
    ## any Biosample can be chemically treated

    related_biosamples = relationship('BiosampleRel',
        primaryjoin="BiosampleRelbiosample_id==Biosample.id"
    )

    derived_from = relationship('BiosampleRelation',
        primaryjoin="and_(BiosampleRel.related_biosample_id==Biosample.id, "
        "BiosampleRel.type.equals('derived_from'))", backref='derivatives')

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

    gender = Column(Enum('Male', 'Female', 'Unknown', name='genders'))
    # the above is a denormalization of data in an ontology

    growth_protocol_no = Column(Integer, ForeignKey('protocol.protocol_no'))
    growth_protocol = relationship('Protocol',
        primaryjoin="and_(CellLine.growth_protocol_id==Protocol.id, "
        "Protocol.type.equals('growth'))", backref='cell_lines')

    __mapper_args__ = {'polymorphic_identity': "Cell Line"}


class Tissue(Biosample):
    ''' includes "whole mouse" which will typically have transfection construct/treatment'''
    __tablename__ = 'tissue'
    id = Column('biosample_no', Integer, ForeignKey('biosample.biosample_no'), primary_key=True)

    date_obtained = Column('date_obtained', Date, nullable=False)
    donors = relationship("Donor",
                    secondary='tissue_donor',
                    backref="tissues")

    excision_protocol_no = Column(Integer, ForeignKey('protocol.protocol_no'))
    excision_protocol = relationship('Protocol',
        primaryjoin="and_(Tissue.extraction_protocol_id==Protocol.id, "
        "Protocol.type.equals('excision'))", backref='tissues')

    __mapper_args__ = {'polymorphic_identity': "Tissue"}


class SingleCell(Tissue):

    __tablename__ = 'single_cell'
    id = Column('biosample_no', Integer, ForeignKey('tissue.biosample_no'),
        primary_key=True)

    validation_documents = relationship('Document')  # unspec'd many-to-many!

    purification_protocol_no = Column(Integer, ForeignKey('protocol.protocol_no'))
    purification_protocol = relationship('Protocol',
        primaryjoin="and_(SingleCell.purification_protocol_no==Protocol.id, "
        "Protocol.type.equals('purification'))", backref='single_cells')

    __mapper_args__ = {'polymorphic_identity': "Single Cell"}


class PrimaryCellCulture(Tissue):

    __tablename__ = 'primary_cell_culture'
    id = Column('biosample_no', Integer, ForeignKey('tissue.biosample_no'),
        primary_key=True)

    ''' this assumes that PCCs have only 1 donor, that might not be the case
    it would have to be split off into a direct subclass of Biosample then
    '''

    purification_protocol_no = Column(Integer, ForeignKey('protocol.protocol_no'))
    purification_protocol = relationship('Protocol',
        primaryjoin="and_(PrimaryCellCulture.purification_protocol_no==Protocol.id, "
        "Protocol.type.equals('purification'))", backref='primary_cell_cultures')

    growth_protocol_no = Column(Integer, ForeignKey('protocol.protocol_no'))
    growth_protocol = relationship('Protocol',
        primaryjoin="and_(PrimaryCellCulture.growth_protocol_no==Protocol.id, "
        "Protocol.type.equals('growth'))", backref='primary_cell_cultures')

    __mapper_args_ = {'polymorphic_identity': "Primary Cell Culture"}


class IPStemCellLine(Tissue):

    __tablename__ = 'ipstemcell_line'
    id = Column('biosample_no', Integer, ForeignKey('tissue.biosample_no'), primary_key=True)

    purification_protocol_no = Column(Integer, ForeignKey('protocol.protocol_no'))
    purification_protocol = relationship('Protocol',
        primaryjoin="and_(IPStemCellLine.purification_protocol_no==Protocol.id, "
        "Protocol.type.equals('purification'))", backref='single_cells')

    growth_protocol_no = Column(Integer, ForeignKey('protocol.protocol_no'))
    growth_protocol = relationship('Protocol',
        primaryjoin="and_(IPStemCellLine.growth_protocol_no==Protocol.id, "
        "Protocol.type.equals('growth'))", backref='IPstemcell_lines')

    __mapper_args__ = {'polymorphic_identity': "Induced Pluripotent Stem Cell Line"}


class BiosampleRel(Base, ENCODEdTableMixin):

    __tablename__ = 'biosample_relationship'
    id = Column('biosample_rel_no', Integer, primary_key=True)
    type = Column('relationship_type',
        Enum('derived_from', 'develops_from', 'contains',
        'has_a', 'is_a', 'part_of', name='relationship_types'), nullable=False)
    biosample_no = Column(Integer, ForeignKey('biosample.biosample_no'))
    related_biosample_no = Column(Integer, ForeignKey('biosample.biosample_no'))


class Treatment(Base, ENCODEdTableMixin):

    __tablename__ = 'treatment'
    id = Column('treatment_no', Integer, primary_key=True)
    name = Column('treatment_name', String, nullable=False)
    description = Column('treatment_description', String)
    submitted_by = Column('submitted_by', String, nullable=False)

    details = relationship("TreatmentDetail",
                    secondary='treat_treat_detail',
                    backref="treatments")


class TreatmentDetail(Base):

    __tablename__ = 'treatment_detail'
    ''' should below be CV tables?  Don't have to load the whole thing '''
    id = Column('treatment_detail_no', Integer, primary_key=True)
    ontology = Column('ontology', Enum('ChEBI', 'Protein', 'Cocktail',
        'Transfection Construct', name='treatment_ontologies'), nullable=False)
    ontology_id = Column('ontology_id', String, nullable=False)
    ontology_term = Column('ontology_term', String, nullable=False)

    concentration = Column('concentration', Float)
    concentration_units = Column('concentration_units', Enum(
        'mM', 'uM', 'nM', 'pm', 'mg/ml', 'ug/ml', 'ng/ml', 'U/ml', 'percent',
        name='conc_units'))
    duration = Column('duration', Float)
    duration_units = Column('duration_units', Enum('s', 'm', 'hr', 'd',
        name='time_units'))
    # duration/duration_units could also be a DateTime or Interval obj.

tissue_donor = Table('tissue_donor', Base.metadata,
    Column('tissue_donor_no', Integer, primary_key=True),
    Column('tissue_no', Integer, ForeignKey('tissue.biosample_no')),
    Column('donor_no', Integer, ForeignKey('donor.donor_no')))

## these could also use the Association object pattern from SQLA
treat_treat_detail = Table('treat_treat_detail', Base.metadata,
    Column('treat_treat_detail_no', Integer, primary_key=True),
    Column('detail_no', Integer, ForeignKey('treatment_detail.treatment_detail_no')),
    Column('treatment_no', Integer, ForeignKey('treatment.treatment_no')))

biosample_document = Table('biosample_document', Base.metadata,
    Column('biosample_document_no', Integer, primary_key=True),
    Column('biosample_no', Integer, ForeignKey('biosample.biosample_no')),
    Column('document_no', Integer, ForeignKey('document.document_no')))
