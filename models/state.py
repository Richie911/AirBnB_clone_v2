#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """ Getter method to fetch cities related to the state """
        all_objects = models.storage.all()
        cities_list = []
        for key, obj in all_objects.items():
            if obj.__class__.__name__ == 'City' and obj.state_id == self.id:
                cities_list.append(obj)
        return cities_list
