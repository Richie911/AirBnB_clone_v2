#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import models
import shlex

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False,)
    name = Column(String(128), nullable=False)
    cities = relationship("City",cascade='all, delete, delete-orphan',
                          back_populates="state")
    @property
    def cities(self):
        mod = models.storage.all()
        arr = []
        result = []
        for val in mod:
            city = val.replace('.', ' ')
            city = shlex.split(city)
            if city[0] is 'City':
                arr.append(mod[val])
        for element in arr:
            if (element.state_id == self.id):
                result.append(element)
        return (result)

