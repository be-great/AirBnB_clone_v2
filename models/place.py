""" place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from models.base_model import BaseModel, Base
from models import storage_ob
from sqlalchemy.orm import relationship
# from models.review import Review
import models


class Place(BaseModel, Base):
    """ Representation of a Place """

    if models.storage_ob == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)

        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities")

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

    if models.storage_ob != 'db':
        @property
        def reviews(self):
            """ Getter attribute that returns the list of Review instances """
            from models.review import Review
            return [review for review in models.storage.all(Review).values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """ Getter attribute that returns the list of Amenity instances """
            from models.amenity import Amenity
            return [amenity for amenity in models.storage.all(Amenity).values()
                    if amenity.place_id == self.id]

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)
