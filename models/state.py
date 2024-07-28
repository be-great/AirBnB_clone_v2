#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage_ob
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    if storage_ob == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)

    # getter
    @property
    def cities(self):
        """return the cities"""
        if storage_ob != 'db':
            cities = models.storage.all(City)
            status_cities = [c for c in cities.values() if c.state_id == self.id]
            return status_cities
        return []