'''
Created on Dec 18, 2012
@author: hitz
'''
from models.sqla import ENCODEdTable, CommonEqualityMixin
import models.sqla.biosample
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Enum


class Organism(ENCODEdTable):

    __tablename__ = 'organism'
    id = Column('organism_id', Integer, PrimaryKey=True)
    name = Column('organism_name', String, nullable=False)
    taxon_id = Column('taxon_id', Integer, nullable=False)


class Donor(ENCODEdTable, CommonEqualityMixin):

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


