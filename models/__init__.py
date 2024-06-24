#!/usr/bin/python3
from os import getenv
"""This module instantiates an object of class FileStorage"""

storage_ob = getenv("HBNB_TYPE_STORAGE")

if storage_ob == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
