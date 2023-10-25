#!/usr/bin/python3
# coding: utf-8


class Register:
    def __init__(self, path):
        self.__path = path

        from .UI.pagemanager import PageManager
        self.__page = PageManager()

    def __call__(self, fun):
        self.__fun = fun
        return self.__callback

    def __callback(self):

        f = self.__fun()

        self.__page.addItem(self)

        return f





