#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey,Integer,Float
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__="places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(60), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                    backref="place")

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                                backref="place")
    else:
        @property
        def reviews(self):  
            model = models.storage.all()
            data = []
            result = []
            for key in model:
                if key.startswith() == 'Review':
                    data.append(model[key])
            for element in data:
                if element.place_id == self.id:
                    result.append(element)
            return (result)
