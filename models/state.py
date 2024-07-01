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

    if models.storage.storage_t == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """Property Getter for list of city instance linked to state"""
            target_cities = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    target_cities.append(city)
            return target_cities
