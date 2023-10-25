#!/usr/bin/python3
# coding: utf-8
from ...common.configurationfile import f_business, f_annotate, f_annotate_no, plu_plugins, plu_classpath, \
    plu_parameter, plu_name
from ...common.annotationname import annotationName
from ...common.presetpluginsname import presetPluginsName
from ..config.config import Config


class Core:
    """
    IOC容器
    核心是BeanFactory，是工厂模式的实现，运用控制翻转(思想)依赖注入(实现)，管理应用对象的配置和生命周期

    流程：
        创建核心IOC容器 --> 读取配置文件(扫描注解) --> 实例化bean对象(注意是否存在重写的bean) --> 实例化业务类

    作用：
        1.实例化类
        2.注入依赖属性
        3.管理类的实例

    """

    def __init__(self):

        # 对象容器
        self.__container = {}
        self.__container_class = {}

        # 插件容器
        self.__plugins = {}

        # 表现层容器
        self.__view = {}

        # 配置队象
        self.__conf = None

    def startUp(self):
        """启动容器"""

        # 实例化配置对象
        self.__conf = Config()
        self.__conf.getConfig()

        # 实例化自身组件(注意是否重写)

        # 实例化插件（自定义或预设）
        if self.__conf.config.get(plu_plugins):
            # 每个插件单独的配置
            for key in self.__conf.config.get(plu_plugins):
                # 实例化插件
                self.__createPlugins(self.__conf.config[plu_plugins][key], key)

        # 实例化业务类
        if self.__conf.config.get(f_business):
            self.__createBusinessInstance()

        # ################### DI依赖注入 ###################

        # 业务类的注入
        self.__setDI(self.__container)

        # 插件类的注入
        self.__setDI(self.__plugins)

        # ################### 初始化插件和组件 ###################
        for plu in self.__plugins:
            if hasattr(self.__plugins[plu], 'init'):
                self.__plugins[plu].init()

        # print('__container:', self.__container)
        # print('__container_class:', self.__container_class)
        # print('__plugins:', self.__plugins)
        # print('__view:', self.__view)

    def addToContainer(self, key, instance):
        self.__container[key] = instance
        # self.__container_class[instance.__class__.__name__.lower()] = instance
        self.__container_class[key] = instance

    def __setDI(self, container):
        # container 为待注入实例列表
        for inst_key in container:
            inst = container[inst_key]
            for attr in dir(inst):
                if attr.startswith('di_'):
                    # ### 需要注入依赖 ###
                    diname = attr[3:]
                    # 注入插件
                    if diname in self.__plugins:
                        setattr(inst, attr, self.__plugins[diname])

                    # 注入业务类
                    if diname.lower() in self.__container_class:
                        setattr(inst, attr, self.__container_class[diname.lower()])

                    # 注入组件
                    pass

                    # 注入容器
                    if diname == 'view':
                        setattr(inst, attr, self.__view)

    def __createBusinessInstance(self):
        """实例化自开发业务代码"""
        if not self.__conf.bean:
            # bean配置为空
            return

        # 不扫描
        if self.__conf.bean.get(f_annotate_no):
            for modelPath in self.__conf.bean.get(f_annotate_no):
                self.__createInstance(modelPath)

        # 扫描
        if self.__conf.bean.get(f_annotate):
            for modelPath in self.__conf.bean.get(f_annotate):
                self.__createInstance(modelPath, scan=True)

    def __createPlugins(self, pluSetting, pluginName):
        """
        实例化插件
        pluSetting: {'name': 'page', 'classpath': 'plugins.pagemanager.PageManager', 'parameter': {'mainwin': 'main'}}
        """
        '''
        根据路径导入插件模块并实例化，根据name 存储到插件容器
        '''

        param = {}
        if plu_parameter in pluSetting and pluSetting[plu_parameter]:
            param = pluSetting[plu_parameter]

        # ############ 预设插件 ############

        if pluginName in presetPluginsName:
            # 为预设插件
            if pluSetting[plu_name] in self.__plugins:
                print('插件名已存在，请查证')
            self.__plugins[pluSetting[plu_name]] = presetPluginsName[pluginName]['class'](**param)
            return

        # ############ 自定义插件 ############

        if plu_classpath not in pluSetting or not pluSetting[plu_classpath]:
            # 自定义插件必须指定插件启动类路径，未指定则忽略该插件
            return

        m_clspath = pluSetting[plu_classpath]

        model = __import__(m_clspath[:m_clspath.rfind('.')], fromlist=[''])

        pluginInstance = getattr(model, m_clspath[m_clspath.rfind('.') + 1:])(**param)

        if pluSetting[plu_name] in self.__plugins:
            print('插件名已存在，请查证')
        self.__plugins[pluSetting[plu_name]] = pluginInstance

    def __createInstance(self, modelPath, scan=False, *args, **kwargs):
        model = __import__(modelPath, fromlist=[''])
        file_name = modelPath[modelPath.rfind('.') + 1:]

        if scan:
            # 扫描
            for funName in dir(model):
                if funName.startswith('__'):
                    continue

                # 对比得到的函数是否是预设的注解 ====================???????????
                # getattr(model2, 'component') is component
                if funName in annotationName:
                    # 存在注解
                    modelInstance = self.__createInstanceByModel(model, file_name, *args, **kwargs)
                    self.__container[modelPath] = modelInstance
                    self.__container_class[file_name] = modelInstance

                    if funName == 'view':
                        # 表现层
                        self.__view[modelPath] = modelInstance
                    return

            # 扫描完，没有发现注解，不创建实例
            return

        # 不扫描，直接创建实例
        modelInstance = self.__createInstanceByModel(model, file_name, *args, **kwargs)
        self.__container[modelPath] = modelInstance
        self.__container_class[file_name] = modelInstance

    @classmethod
    def __createInstanceByModel(cls, model, file_name, *args, **kwargs):
        for name in dir(model):
            if name.lower() == file_name:
                # 待实例的类 getattr(model, name)
                # 注入属性在什么时候操作？ __init__之前还是之后 ====================???????????
                modelInstance = getattr(model, name)(*args, **kwargs)

                return modelInstance








