#!/usr/bin/python3
"""FileStorage class for AirBnB"""

import json


class FileStorage:
    """FileStorage class for AirBnB"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self) -> None:
        """Initialize FileStorage"""
        pass

    def all(self):
        """all method for FileStorage

        Returns:
            dict: dictionary of objects
        """
        return self.__objects

    def new(self, obj):
        """new method for FileStorage

        Args:
            obj (obj.__class__.__name__): object to add to __objects
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """save method for FileStorage
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        try:
            with open(self.__file_path, 'w') as file:
                json.dump(obj_dict, file)
        except FileNotFoundError:
            pass

    def reload(self):
        """reload method for FileStorage
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name in globals():
                        cls = globals()[class_name]
                        instance = cls(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass
