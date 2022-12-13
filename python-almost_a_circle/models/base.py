#!/usr/bin/python3
"""Creating a base class"""

import json
import turtle
import csv


class Base:
    """Attributes: id number"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Function that Initialize a new id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Defining a function that
        converts a list of dictionaries to a JSON string"""
        if list_dictionaries is None:
            return "[]"

        if len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Defining a function that writes the
        JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        new_list = []
        if list_objs:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))

        with open(file_name, mode="w") as myFile:
            myFile.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Defining a function that
        converts a JSON string to a list of dictionaries"""
        if json_string is None:
            return []

        if len(json_string) == 0:
            return []

        list_dicts = json.loads(json_string)
        return list_dicts

    @classmethod
    def create(cls, **dictionary):
        """Defining a function  that returns
        an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 2)
        if cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Defining a function that
        returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                content = file.read()
        except FileNotFoundError:
            return []

        ex_content = cls.from_json_string(content)
        context_list = []
        for instance_dict in ex_content:
            context_list.append(cls.create(**instance_dict))
        return context_list
