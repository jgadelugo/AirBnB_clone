#!/usr/bin/python3
""" Class FileStorage the serializes instances to a JSON file
and deserializes JSON file to instances"""

import json


class FileStorage:
    """ Class FileStorage """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """

        return type(self).__name__.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """


    def save(self):
        """ Serializes __objects to the JSON file __file_path """


    def reload(self):
        """ Deserializes the JSON file to __objects if __file_path exists
        otherwise do nothing, with no exception being reaised """
