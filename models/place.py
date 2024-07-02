#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import environ
from models.amenity import Amenity
import models
import os


if models.storage_t == "db":
    metadata = Base.metadata

    place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', ondelete='CASCADE')),
                          Column('amenity_id', String(60),
                                 ForeignKey(
                                     'amenities.id', ondelete='CASCADE')))


class Place(BaseModel, Base):
    """This is the class for Place"""

    if models.storage_t == "db":
        __tablename__ = 'places'

        city_id = Column(String(60),
                         ForeignKey('cities.id', ondelete='CASCADE'),
                         nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id', ondelete='CASCADE'),
                         nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan',
                               passive_deletes=True)
        amenities = relationship('Amenity', backref='place_amenities',
                                 cascade='all, delete',
                                 secondary=place_amenity,
                                 viewonly=False, passive_deletes=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Getter returning list of review instances"""
            return [review for review in models.storage.all(
                Review).values() if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter returning list of Amenity instances"""
            return [amenity for amenity in models.storage.all(
                Amenity).values() if amenity.place_id == self.id]

        @amenities.setter
        def amenities(self, obj):
            if not isinstance(obj, Amenity):
                return
            self.amenity_ids.append(obj.id)
