#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class would transition from the filestorage to DBstorage"""
    __engine = None
    __session = None

    def __init__(self):
        """init objects"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """init all"""
        classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
        dict_ = {}
        if cls is None:
            for key, value in classes.items():
                objs = self.__session.query(value).all()
                for o in objs:
                    key = f"{o.__class__.__name__}.{o.id}"
                    dict_[key] = o
        else:
            objs = self.__session.query(cls).all()
            for o in objs:
                key = f"{o.__class__.__name__}.{o.id}"
                dict_[key] = o
        return dict_

    def new(self, obj):
        """add new object to the DB"""
        self.__session.add(obj)

    def save(self):
        """save the object to the DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete the obj to the DB"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload the object"""
        Base.metadata.create_all(self.__engine)
        sessionmaker_ = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        session = scoped_session(sessionmaker_)
        self.__session = session

    def close(self):
        """call the reload function"""
        self.__session.remove()
