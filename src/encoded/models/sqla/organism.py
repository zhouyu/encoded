'''
Created on Dec 18, 2012
@author: hitz
'''
from .import Base, ENCODEdTable, CommonEqualityMixin
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Enum


class Organism(Base, ENCODEdTable):

    __tablename__ = 'organism'
    id = Column('organism_id', Integer, primary_key=True)
    name = Column('organism_name', String, nullable=False)
    taxon_id = Column('taxon_id', Integer, nullable=False)


class Donor(Base, ENCODEdTable, CommonEqualityMixin):

    __tablename__ = 'donor'
    id = Column('donor_id', Integer, primary_key=True)
    organism_id = Column('organism_id', Integer,
        ForeignKey('organism.organism_id'), nullable=False)
    organism = relationship(Organism, uselist=False, backref='donors')

    @declared_attr
    def organism_name_(cls):
        return cls.organism.name

    age = Column('age', String)
    gender = Column('gender', Enum('Male', 'Female', 'Unknown', name="genders"))

    __mapper_args__ = {'polymorphic_on': :organism_name,
                       'polymorphic_identity': "Donor",
                       'with_polymorphic': '*'}


class MouseDonor(Donor):
    __tablename__ = 'mouse_donor'
    id = Column('donor_id', Integer, ForeignKey('donor.donor_id'), primary_key=True)
    strain = Column('strain', String)

    __mapper_args__ = {'polymorphic_identity': "Mus musculus"}


class HumanDonor(Donor):

    __tablename__ = 'human_donor'
    id = Column('donor_id', Integer, ForeignKey('donor.donor_id'), primary_key=True)
    ethnicity = Column('ethnicity', String)  # Should be coded or Enum
    health_status = Column('health_status', String)
    external_id = Column('external_donor_id', Integer)

    __mapper_args__ = {'polymorphic_identity': "Homo sapiens"}


