#!/usr/bin/python3
# coding: utf-8


class PageManager:
    """
    ==== 针对pyside实现 ====

    目前尝试有基于树、字典、事件
    在使用中发现，使用树形结构存储和检索，效率不如基于hash表的字典，内存占用也没有量级的增加，因此使用字典来实现存储和检索

    -- 控制页面显示和隐藏 这里使用的是直接控制，可以定义事件，让qt自己去显示和隐藏
    ---- 这里是显示（show）和隐藏（hide）。如果内存紧张，可以修改为生成和销毁。也可以混用

    只实现了一级页面的跳转，多级的控制未实现

    """

    def __init__(self):

        # 所有页面
        from .page_dict import ControllerByDict
        self.__pages = ControllerByDict()

        self.__now = None

        # 主页面
        self.__mainWindow = None

    def goto(self, loadPath, *args, **kwargs):
        if not loadPath:
            print('路径为空')
            return
        if self.__now:
            if loadPath == self.__now.path:
                # 跳转界面为当前显示界面
                print('当前界面')
                return
            self.__hide(self.__now, *args, **kwargs)

        win = self.__getItem(loadPath)

        if not win:
            # 根据路径无法找到页面
            print('未找到页面')
            return

        if self.__now:
            # 不能与上面合并，因为一旦合并，同时又没有找到页面，这样所有页面都隐藏了，界面一片空白
            self.__hide(self.__now, *args, **kwargs)

        self.__show(win, *args, **kwargs)
        self.__now = win

    def addItems(self, **kwargs):
        for path in kwargs:
            self.addItem(path, kwargs[path])
            kwargs[path].path = path

    def addItem(self, path, win):
        win.hide()  # 隐藏页面
        # win.close()  # 关闭页面,大部分情况下是隐藏，通hide()

        self.__pages.add(path, win)

    def close(self, *args, **kwargs):
        if self.__now:
            self.__hide(self.__now, *args, **kwargs)

    def setMainWindow(self, win):
        self.__mainWindow = win

    def getMainWindow(self):
        return self.__mainWindow

    def __getItem(self, loadPath):
        return self.__pages.get(loadPath)

    @classmethod
    def __show(cls, page, *args, **kwargs):
        if hasattr(page, 'load'):
            page.load(*args, **kwargs)
        page.show()

    @classmethod
    def __hide(cls, page, *args, **kwargs):
        if hasattr(page, 'unload'):
            page.unload(*args, **kwargs)
        page.hide()








