#!/usr/bin/python3
# coding: utf-8
from datetime import datetime

from PySide6 import QtWidgets
from PySide6.QtCore import QTimer

from core.view.style.style import pageStyle
from core.view.style.stylecommon import color_shenlan_3
from core.view.style.styleutils import padding, fontSize, fontColor, background
from core.view.ui.home import Ui_Form
from core.view.ui.hometitle import Ui_Form as t
from framework import view


@view
class Home(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']

        self.di_page = None
        self.di_basewin = None

        self.homeTitle = HomeTitle()
        self.titlelay.addWidget(self.homeTitle)

        self.initStata = 0  # 页面是否初始化  0 未初始化； 1 初始化

        self.nowPage = None

        self.init()

    def load(self):
        if not self.initStata:
            self.initPage()
            self.initStata = 1

        self.timerOutFun()

        self.homeTitle.pushButton.click()

    def unload(self):
        pass

    def init(self):
        self.homeTitle.title.setText('项目')

        self.setPageStyle()

    def initPage(self):
        self.di_basewin.closeEvent = self.baseWinCloseEvent

    def setPageButton(self):
        pass

    def baseWinCloseEvent(self, event):
        print('guanbi')

        self.hide()

        # 关闭当前界面子线程
        self.di_page.close()

        # sys.exit()

    def addPage(self, win):
        self.contentlay.addWidget(win)

    def setPageStyle(self):
        self.setStyleSheet(pageStyle)

        self.homeTitle.setStyleSheet(
            f'QLabel#day{{{fontSize(11)}}}'
            f'QLabel#week{{{fontSize(13)}}}'
            f'QLabel#time{{{fontSize(13)}}}'
            f'QLabel#title{{{fontSize(15) + fontColor("#ccb54a")}}}'
        )

        self.homeTitle.widget_3.setStyleSheet(
            f'QPushButton{{{padding(30,8,30,8)}}};'
        )

        self.homeTitle.pushButton_5.setStyleSheet(f'*:hover{{{fontColor("red")}}}')

    def setButtonClickStyle(self, button):
        if self.nowPage:
            self.nowPage.setStyleSheet('')

        button.setStyleSheet(background(color_shenlan_3))
        self.nowPage = button

    def timerOutFun(self):
        now = datetime.now()
        day = now.strftime("%Y-%m-%d")
        week = self.__week[now.weekday()]
        nowtime = now.strftime("%H:%M:%S")
        self.homeTitle.day.setText(day)
        self.homeTitle.week.setText(week)
        self.homeTitle.time.setText(nowtime)


class HomeTitle(QtWidgets.QWidget, t):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
