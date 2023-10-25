#!/usr/bin/python3
# coding: utf-8


class Register:
    """
    注册器，将零散页面注册到主页面容器
    """
    def __init__(self, homewin=None):
        self.homeWin = homewin

    def regWin(self, win):

        assert self.homeWin, '未设置主窗口，请设置后重试！！'

        if win is self.homeWin:
            # 主页面，跳过
            return

        self.homeWin.addPage(win)





