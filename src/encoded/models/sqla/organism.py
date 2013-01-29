'''
Created on Dec 18, 2012
@author: hitz
'''
from . import Base, ENCODEdTableMixin, CommonEqualityMixin
from sqlalchemy import select
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Enum


class Organism(Base, ENCODEdTableMixin):

    __tablename__ = 'organism'
    id = Column('organism_no', Integer, primary_key=True)
    name = Column('organism_name', String, nullable=False)
    taxon_no = Column('taxon_no', Integer, nullable=False)


class Donor(Base, ENCODEdTableMixin, CommonEqualityMixin):

    __tablename__ = 'donor'
    id = Column('donor_no', Integer, primary_key=True)
    organism_no = Column('organism_no', Integer,
        ForeignKey('organism.organism_no'), nullable=False)
    organism = relationship(Organism, uselist=False, backref='donors')

    organism_name = column_property(
        select([Organism.name]).where(Organism.id == organism_no).as_scalar())

    age = Column('age', String)
    gender = Column('gender', Enum('Male', 'Female', 'Unknown', name="genders"))

    __mapper_args__ = {'polymorphic_on': organism_name,
                       'polymorphic_identity': "Donor",
                       'with_polymorphic': '*'}


class MouseDonor(Donor):
    __tablename__ = 'mouse_donor'
    id = Column('donor_no', Integer, ForeignKey('donor.donor_no'), primary_key=True)
    strain = Column('strain', String)

    __mapper_args__ = {'polymorphic_identity': "Mus Musculus"}


class HumanDonor(Donor):

    __tablename__ = 'human_donor'
    id = Column('donor_no', Integer, ForeignKey('donor.donor_no'), primary_key=True)
    ethnicity = Column('ethnicity', String)  # Should be coded or Enum
    health_status = Column('health_status', String)
    external_no = Column('external_donor_no', Integer)

    __mapper_args__ = {'polymorphic_identity': "Homo Sapiens"}


