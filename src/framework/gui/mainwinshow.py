#!/usr/bin/python3
# coding: utf-8
from PySide6.QtWidgets import QMainWindow
from .mainwin import Ui_MainWindow


class MainWinShow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def addPage(self, win):
        self.mainlay.addWidget(win)






