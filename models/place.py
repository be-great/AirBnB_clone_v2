""" place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from models.base_model import BaseModel, Base
from models import storage_ob
# from sqlalchemy.orm import relationship
# from models.review import Review
# import models


place_amenity = Table('place_amenity', Base.metadata,
                        Column(String(60), 'place_id', ForeignKey('places.id'), primary_key=True, nullable=False),
                        Column(String(60), 'amenity_id', ForeignKey('amenities.id'), primary_key=True, nullable=False)
                    )

class Place(BaseModel, Base):
    """ A place to stay """
    if storage_ob == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        # reviews = relationship('Review', backref='place', cascade='all, delete, delete-orphan')
    else:
        # @property
        # def reviews(self):
        #     """This is a Getter attribute that returns the list of Review
        #           instances with place_id equals to the current Place.id"""
        #     list_of_review = []
        #     for review in storage.all(Review).values():
        #         if review.place_id == self.id:
        #             list_of_review.append(review)
        #     return list_of_review

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

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)
