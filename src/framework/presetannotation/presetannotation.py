#!/usr/bin/python3
# coding: utf-8

"""
def outside(*outArgs):
    def middle(fun):
        def inner(*args):
            print(*outArgs)
            return fun(*args)
        return inner
    return middle

"""


def component(model):
    """组成"""
    def inner(*args):
        return model(*args)
    return inner


def view(model):
    """表现层标记"""
    def inner(*args):
        return model(*args)
    return inner


def business(model):
    """业务层标记"""
    def inner(*args):
        return model(*args)
    return inner


def database(model):
    """数据层标记"""
    def inner(*args):
        return model(*args)
    return inner






