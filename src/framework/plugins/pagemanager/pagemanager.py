#!/usr/bin/python3
# coding: utf-8
from .register import Register


class PageManager(Register):
    """
    ==== 针对pyside实现 ====

    集成注册器

    目前尝试有基于树、字典、事件
    在使用中发现，使用树形结构存储和检索，效率不如基于hash表的字典，内存占用也没有量级的增加，因此使用字典来实现存储和检索

    -- 控制页面显示和隐藏 这里使用的是直接控制，可以定义事件，让qt自己去显示和隐藏
    ---- 这里是显示（show）和隐藏（hide）。如果内存紧张，可以修改为生成和销毁。也可以混用

    只实现了一级页面的跳转，多级的控制未实现

    """

    def __init__(self, homewin=None, basepath=None):
        super().__init__(homewin)

        self.di_view = None
        self.di_basewin = None

        self.basepath = basepath

        # 所有页面
        from .page_dict import ControllerByDict
        self.__pages = ControllerByDict()

        self.__now = None

    def init(self):
        # 设置主页面
        self.homeWin = self.di_view[self.homeWin]

        # 将主页面注册到基页面
        self.di_basewin.addPage(self.homeWin)

        # 将页面注册到主页面及页面管理器
        for win_key in self.di_view:
            win = self.di_view[win_key]

            # 注册到主页面
            self.regWin(win)

            # 注册到页面管理器
            winpath = win_key[len(self.basepath):]
            if winpath.startswith('.'):
                winpath = winpath[1:]
            self.addItem(winpath, win)

        if hasattr(self.homeWin, 'load'):
            self.homeWin.load()
        self.homeWin.show()

    def goto(self, loadPath, *args, **kwargs):
        if not loadPath:
            print('路径为空')
            return
        if self.__now:
            if loadPath == self.__now.path:
                # 跳转界面为当前显示界面
                print('当前界面')
                return

        win = self.__getItem(loadPath)

        if not win:
            # 根据路径无法找到页面
            print('未找到页面')
            return

        if self.__now:
            self.__hide(self.__now, *args, **kwargs)

        self.__show(win, *args, **kwargs)
        self.__now = win

    def addItems(self, **kwargs):
        for path in kwargs:
            self.addItem(path, kwargs[path])

    def addItem(self, path, win):
        win.hide()  # 隐藏页面
        # win.close()  # 关闭页面,大部分情况下是隐藏，通hide()

        # 为界面添加路径，用来对比是否是当前路径
        win.path = path

        self.__pages.add(path, win)

    def close(self, *args, **kwargs):
        if self.__now:
            self.__hide(self.__now, *args, **kwargs)

    def setProperty(self, attrName, attrValue, *args, **kwargs):
        setattr(self, attrName, attrValue)

    def getProperty(self, attrName, *args, **kwargs):
        if hasattr(self, attrName):
            val = getattr(self, attrName)
            delattr(self, attrName)
            return val
        return None

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








