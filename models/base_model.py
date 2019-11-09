#!/usr/bin/python3
""" Class BaseModel defines common attributes/methods for other classes """

import uuid
from datetime import datetime as dt


class BaseModel:
    """ Class BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initilize a new instance of BaseModel class
        using arguments and keyword arguments """

        if kwargs and kwargs != []:
            for key, value in kwargs.items():
                if key is '__class__':
                    value = self.__class__
                if key is 'created_at':
                    value = dt.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key is 'updated_at':
                    value = dt.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()

    def __str__(self):
        """ Prints string represneting the class

        [<class name>] (<self.id>) <self.__dict__> """
        return ("[{}] ({}) {}".format
                (type(self).__name__, self.id, self.__dict__))

    def save(self):
        """ Updates public instance attribute update_at
        with current datetime"""

        self.updated_at = dt.now()

    def to_dict(self):
        """ Returns dictionary containing all the keys/values """

        __dict__ = dict(self.__dict__)
        __dict__['__class__'] = type(self).__name__
        __dict__['created_at'] = self.created_at.isoformat()
        __dict__['updated_at'] = self.updated_at.isoformat()
        return __dict__
