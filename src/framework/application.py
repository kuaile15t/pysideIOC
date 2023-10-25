#!/usr/bin/python3
# coding: utf-8
from .module.core.core import Core


class Application:
    """
    管理上下文，持有核心容器，提供运行方法
    1. 设置主函数：
            （1）没有GUI界面的程序，设置函数，如果是对象编程的话，使用 类对象.运行方法 来设置
                    已暂时取消了该项支持，因为暂时没有必须的集成工具，后期有需求可以再添加

            （2）GUI界面程序，设置为主界面的类名。目前只支持Qt（pyside/pyqt）界面

    2. 执行run()

    记录：类是type的实例，而函数不是。因此，使用isinstance(变量, type)判断 变量 是不是类
    """
    def __init__(self, mainFun=None, initPlugins=None):

        self.__mainFun = mainFun

        self.__initPlugins = initPlugins

    def run(self, mode='qt', **kwargs):
        """引用运行方法"""

        # 无界面
        # self.__runNoUI()

        # 运行pyside应用
        if mode == 'qt':
            self.__runPyside(**kwargs)

    def __runPyside(self, title='', iconPath='', fullscreen=0, welcome=False, welimg='', welmsg=''):
        """
        pyside界面
        :param title:
        :param iconPath:
        :param fullscreen:
        :param welcome:
        :param welimg:
        :param welmsg:
        :return:
        """

        import sys
        from PySide6.QtWidgets import QApplication

        # == == == == == = 启动app == == == == == =
        # 对Qt部件的操作一般都要在创建Qt程序后才能进行
        app = QApplication(sys.argv)

        splash = None
        if welcome:
            # =========== 启动显示欢迎图片 ===========
            from PySide6.QtWidgets import QSplashScreen
            from PySide6.QtGui import QPixmap

            # 创建启动界面，支持png透明图片
            if welimg:
                splash = QSplashScreen(QPixmap(welimg))  # 启动界面图片地址
            else:
                splash = QSplashScreen()  # 启动界面图片地址

            splash.show()

            if welmsg:
                # 显示启动欢迎语
                splash.showMessage(welmsg)

        app.processEvents()  # 防止进程卡死

        # 创建窗口
        # == 不能提前创建，缺少qt上下文，会崩溃
        # -- 主窗口在容器里创建 --
        from .gui.mainwinshow import MainWinShow
        mainwin = MainWinShow()

        # 启动ioc 并运行
        c = Core()
        c.addToContainer('basewin', mainwin)
        c.startUp()

        # 设置界面标题
        if title:
            mainwin.setWindowTitle(title)

        # 设置界面icon图标
        if iconPath:
            from PySide6.QtGui import QIcon
            """判断是不是icon，是：直接设置； 不是：使用pixmap转换，再设置"""
            if iconPath.endswith('.ico'):
                mainwin.setWindowIcon(QIcon(iconPath))
            else:
                from PySide6.QtGui import QPixmap
                icon = QIcon()
                icon.addPixmap(QPixmap(iconPath), QIcon.Normal, QIcon.Off)
                mainwin.setWindowIcon(icon)

        # 显示界面
        if fullscreen:
            mainwin.showFullScreen()  # 全屏
        else:
            mainwin.show()

        if splash:
            # 关闭启动画面
            # splash.close()
            splash.finish(mainwin)

        sys.exit(app.exec())

    def __runNoUI(self):
        """无界面"""
        # if not isinstance(self.__mainFun, type):
        #     # ### 类是type的实例，函数不是 ###
        #     # 没有界面
        #
        #     # 创建容器
        #     # from .container.container import Container
        #     # con = Container()
        #
        #     if not self.__mainFun:
        #         # 主函数为空
        #         print('请设置主函数..')
        #         return
        #
        #     self.__mainFun()
        #     return
        pass














