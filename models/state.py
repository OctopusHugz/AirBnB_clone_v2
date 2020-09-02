#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel, Column, String
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state", passive_deletes=True)


if getenv('HBNB_TYPE_STORAGE') != 'db':
    @property
    def cities(self):
        """ Cities getter """
        return self.cities
