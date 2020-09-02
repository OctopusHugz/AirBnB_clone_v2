#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel, Column, String
from models.city import City
from models import storage


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
            cities_list = []
            cities_dict = storage.all(City)
            for city in cities_dict.values():
                if self.id == city.state_id:
                    cities_list.append(city)
            return cities_list
