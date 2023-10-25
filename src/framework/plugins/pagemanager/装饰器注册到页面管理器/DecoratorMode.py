#!/usr/bin/python3
# coding: utf-8


class DecoratorMode:
    """
    分别持有页面管理器和主窗口的实例，将被修饰对象注册到管理器和注入主窗口
    """
    def __init__(self):

        # 页面管理器
        from .UI.pagemanager import PageManager
        self.__page = PageManager()

        # 主窗口
        self.__holder = None

    def setHolder(self, hold):
        self.__holder = hold

    def getPage(self):
        return self.__page

    def register(self, path):
        def mid(fun):
            def inner():
                # 实例化窗口对象
                w = fun()
                # 将窗口对象注册到页面管理器
                self.__page.addItem(path, w)
                w.goto = self.__page.goto
                # 将窗口对象注入到主窗口
                self.__holder.addWin(w)
                return w
            return inner
        return mid













