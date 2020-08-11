#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import ForeignKey, Column, Relationship, String
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = Relationship("Place", cascade="all, delete", backref="cities")
