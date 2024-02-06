#!/usr/bin/python3
"""
    base model class module, contain the basemodel class defination
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Defines all common attributes

    Attributes:
        id (str): unique identfier
        created_at (datetime.datetime): creation date
        updated_at (datetime.datetime): last update's time
    """
    def __init__(self, *args, **kwargs):
        """
            intialization
        """
        DT_FMT = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None or len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] =datetime.strptime(value, DT_FMT)
                else:
                    self.__dict__[key] = value
        else:

            models.storage.new(self)

    def __str__(self):
        """
            Return the official string representation
        """
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
            save the instance in the storage engine.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containg all key/values
        """

    my_dict = self.__dict__.copy()
    my_dict["__class__"] = type(self).__name__
    my_dict["created_at"] = my_dict["created_at"].isoformat()
    my_dict["updated_at"] = my_dict["updated_at"].isoformat()
    return my_dict
