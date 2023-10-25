#!/usr/bin/python3
# coding: utf-8


class ControllerByDict:
    """
    基于hash实现的字典的存储与检索
    """

    def __init__(self):
        self.__data = {}

    def getAll(self):
        return self.__data

    def get(self, key):
        if key in self.__data:
            return self.__data.get(key)

    def add(self, key, value):
        if key not in self.__data:
            self.__data[key] = value
            return 1

    def set(self, key, value):
        self.__data.update({key: value})

    def delete(self, key):
        if key in self.__data:
            return self.__data.pop(key)


















