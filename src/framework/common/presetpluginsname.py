#!/usr/bin/python3
# coding: utf-8


""" ------------------- 预设插件导入方法 ------------------- """


def getPagemanager(clsName):
    if clsName == 'pagemanager':
        from ..plugins.pagemanager.pagemanager import PageManager
        return PageManager


""" ------------------- 预设插件信息 ------------------- """

# 预设注解
presetPluginsName = {
    'pagemanager': {
        'use': "页面管理器，管理页面的显示、隐藏、跳转及生命周期函数。内置注册器，将零散页面注册到主页面容器",
        'class': getPagemanager('pagemanager'),
    },
}




