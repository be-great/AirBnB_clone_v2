#!/usr/bin/python3
from os import getenv
from models.engine.db_storage import DBStorage
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
