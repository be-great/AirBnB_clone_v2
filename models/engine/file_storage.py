"""script for the file_storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary of objects, optionally filtered by class"""
        if cls is None:
            return FileStorage.__objects.copy()  # Return a copy of all objects
        else:
            return {obj_id: obj for obj_id,
                    obj in FileStorage.__objects.items()
                    if isinstance(obj, cls)}

    def delete(self, obj=None):
        """Deletes obj from __objects"""
        if obj is not None:
            key_to_delete = None
            for key, key_value in FileStorage.__objects.items():
                if key_value == obj:
                    key_to_delete = key
                    break
            if key_to_delete is not None:
                del FileStorage.__objects[key_to_delete]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        class_name = obj.__class__.__name__
        obj_id = obj.id
        key = f"{class_name}.{obj_id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass
