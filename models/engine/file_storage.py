import json
import os
from models.base_model import BaseModel
"""
module to define the file storage
"""


class FileStorage:
    """to convert string to file"""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        function to add object
        """
        objName = obj.__class__.__name__
        key = "{}.{}".format(objName, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """retrieves all objects"""
        return FileStorage.__objects

    def save(self):
        """saves all ojects in the Json file"""
        objects = FileStorage.__objects
        objectDictionary = {}

        for i in objects.keys():
            objectDictionary[i] = objects[i].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(objectDictionary, file)

    def reload(self):
        """
        to reload all data in the file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    objectDictionary = json.load(file)

                    for key, val in objectDictionary.items():
                        className, objectId = key.split('.')
                        classTemp = eval(className)
                        obj = classTemp(**val)
                        FileStorage.__objects[key] = obj
                except Exception:
                    pass
