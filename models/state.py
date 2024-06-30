#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
