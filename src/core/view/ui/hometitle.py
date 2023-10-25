# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hometitle.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1023, 90)
        self.horizontalLayout_6 = QHBoxLayout(Form)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_8 = QHBoxLayout(self.widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.timew = QWidget(self.widget)
        self.timew.setObjectName(u"timew")
        self.timew.setStyleSheet(u"#timew{\n"
"	border: 1px solid #2d82b9;\n"
"	border-radius: 2px;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.timew)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 1, 9, 1)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(1, 5, 1, 1)
        self.day = QLabel(self.timew)
        self.day.setObjectName(u"day")
        font = QFont()
        font.setPointSize(9)
        font.setKerning(False)
        self.day.setFont(font)
        self.day.setStyleSheet(u"color: #b5f1fc;")
        self.day.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_14.addWidget(self.day)

        self.week = QLabel(self.timew)
        self.week.setObjectName(u"week")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setKerning(False)
        self.week.setFont(font1)
        self.week.setStyleSheet(u"color: #b5f1fc;")
        self.week.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.week)

        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 3)

        self.horizontalLayout_7.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.time = QLabel(self.timew)
        self.time.setObjectName(u"time")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setKerning(False)
        self.time.setFont(font2)
        self.time.setStyleSheet(u"color: #b5f1fc;")
        self.time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.time)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)


        self.horizontalLayout_8.addWidget(self.timew)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_17 = QVBoxLayout(self.widget_2)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(1, 1, 1, 1)
        self.title = QLabel(self.widget_2)
        self.title.setObjectName(u"title")
        font3 = QFont()
        font3.setFamilies([u"\u9ed1\u4f53"])
        font3.setBold(True)
        font3.setKerning(True)
        self.title.setFont(font3)
        self.title.setStyleSheet(u"")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.title)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_6 = QSpacerItem(98, 43, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_5 = QSpacerItem(97, 43, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.pushButton_4 = QPushButton(self.widget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.horizontalSpacer_4 = QSpacerItem(98, 43, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.horizontalLayout_12.addWidget(self.widget_3)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_11.addWidget(self.pushButton_5)

        self.horizontalLayout_11.setStretch(1, 1)

        self.verticalLayout_17.addLayout(self.horizontalLayout_11)

        self.verticalLayout_17.setStretch(1, 1)

        self.horizontalLayout_8.addWidget(self.widget_2)

        self.horizontalLayout_8.setStretch(1, 1)

        self.horizontalLayout_6.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.day.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.week.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.time.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.title.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6309\u94ae1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6309\u94ae2", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u6309\u94ae3", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u6309\u94ae4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
    # retranslateUi

