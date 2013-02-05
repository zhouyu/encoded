'''
Created on Dec 18, 2012
Adopted from sgd2 Biorelation by kpaskov
@author: hitz
'''
from . import Base, ENCODEdTableMixin
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table, Column, ForeignKey
from sqlalchemy.types import Integer, String, Date, Float, Enum


class Biosample(Base, ENCODEdTableMixin):
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

    date_obtained = Column('date_obtained', Date)
    donors = relationship("Donor",
                    secondary='tissue_donor',
                    backref="biosamples")

    related_biosamples = relationship('BiosampleRel',
        primaryjoin="BiosampleRelbiosample_id==Biosample.id"
    )

    derived_from = relationship('BiosampleRelation',
        primaryjoin="and_(BiosampleRel.related_biosample_id==Biosample.id, "
        "BiosampleRel.type.equals('derived_from'))", backref='derivatives')

    purification_protocol = relationship('Protocol', secondary='biosample_protocol',
        primaryjoin=
        "and_(biosample_protocol.protocol_no==Protocol.id, "
        "Protocol.type.equals('purification')), "
        "biosample_protocol.biosample_no==Biosample.id"
        ,backref='purified_biosamples')

    growth_protocol = relationship('Protocol', secondary='biosample_protocol',
        primaryjoin=
        "and_(biosample_protocol.protocol_no==Protocol.id, "
        "Protocol.type.equals('growth')), "
        "biosample_protocol.biosample_no==Biosample.id"
        ,backref='grown_biosamples')

    excision_protocol = relationship('Protocol', secondary='biosample_protocol',
        primaryjoin=
        "and_(biosample_protocol.protocol_no==Protocol.id, "
        "Protocol.type.equals('excision')), "
        "biosample_protocol.biosample_no==Biosample.id"
        ,backref='excised_biosamples')


    def __init__(self):
        pass

    def __repr__(self):
        pass


class StableCellLine(Biosample):
    ''' many donor fields are null '''
    ''' must have growth protocol '''
    pass


class Tissue(Biosample):
    ''' includes "whole mouse" which will typically have transfection construct/treatment'''

    ''' may be part_of another Tissue '''
    ''' may contain other biosamples (pooled)'''
    ''' must have excision protocol'''
    pass


class SingleCell(Tissue):

    ''' may be part_of another Tissue '''
    ''' must have purification protocol'''
    ''' may have valdiation images'''
    validation_images = relationship('Document')  # unspec'd many-to-many!


class PrimaryCellCulture(Tissue):

    ''' may be part_of another Tissue '''
    ''' may contain other biosamples (pooled) '''
    ''' must have growth protocol '''
    ''' may have purification protocol'''
    pass


class IPStemCellLine(Tissue):

    ''' must have derived_from relationship '''
    ''' must have growth protocol '''
    ''' may have purification protocol'''
    pass


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

biosample_protocol = Table('biosample_protocol', Base.metadata,
    Column('biosample_protocol_no', Integer, primary_key=True),
    Column('biosample_no', Integer, ForeignKey('biosample.biosample_no')),
    Column('protocol_no', Integer, ForeignKey('protocol.protocol_no')))


biosample_donor = Table('biosample_donor', Base.metadata,
    Column('biosample_donor_no', Integer, primary_key=True),
    Column('biosample_no', Integer, ForeignKey('biosample.biosample_no')),
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
