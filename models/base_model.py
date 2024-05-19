#!/usr/bin/python3
"""
module to define the "baseClass"
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    define all common methods and attributes of the classes
    """
    def __init__(self, *args, **kwargs):
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(val, date_format))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        models.storage.new(self)

    def save(self):
        """
        updates updated_at attribute with the current datetime that changed at
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns dictionary containing content (key: values) of __dict__
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict

    def __str__(self):
        """
        return string format that contain class name, class id and class dict
        """
        class_name = self.__class__.__name__
        ret = "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
        return ret

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    # print(my_model.id)
    # print(my_model)
    # print(type(my_model.created_at))
    # print("--")
    my_model_json = my_model.to_dict()
    # print(my_model_json)
    # print("JSON of my_model:")
    # for key in my_model_json.keys():
    #     print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    # print("--")
    my_new_model = BaseModel(**my_model_json)
    # print(my_new_model.id)
    # print(my_new_model)
    # print(type(my_new_model.created_at))

    # print("--")
    # print(my_model is my_new_model)