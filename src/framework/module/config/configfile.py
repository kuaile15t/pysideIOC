#!/usr/bin/python3
# coding: utf-8
import os.path


class ConfigFile:
    """
    读取配置文件
        配置文件类型为：'.yml/.yaml'、'.xml'、'.json'、'.ini'  优先级顺序为：yaml、yml、xml、json、ini
        1.将配置文件放在:
            应用运行目录下 'resource' 文件夹下，文件名称为 'config'
        2.指定完整路径:
            (1) 相对路径：从应用运行目录开始 如：src/resource/config.yaml
            (2) 绝对路径：从磁盘开始 如：D:/app/src/resource/config.yaml
    """
    def __init__(self, path=''):

        # 配置文件路径
        self.path = r'resources/config.yaml'
        if path:
            self.path = path

        if not os.path.exists(self.path):
            # config.yaml不存在，尝试config_pro.yaml
            if os.path.exists(r'resources/config_pro.yaml'):
                # 存在
                self.path = r'resources/config_pro.yaml'

    def getConfig(self):
        """
        优先级：yaml --> yml --> xml --> json --> ini
        """

        # yaml格式文件
        if os.path.exists(self.path):
            return self.__getYamlConfig()

        # yml格式文件
        self.path = self.path.replace('yaml', 'yml')
        if os.path.exists(self.path):
            return self.__getYamlConfig()

        # xml格式文件
        self.path = self.path.replace('yml', 'xml')
        if os.path.exists(self.path):
            return self.__getXmlConfig()

        # json格式文件
        self.path = self.path.replace('xml', 'json')
        if os.path.exists(self.path):
            return self.__getJsonConfig()

        # ini格式文件
        self.path = self.path.replace('json', 'ini')
        if os.path.exists(self.path):
            return self.__getIniConfig()

    def __getYamlConfig(self):
        """读取yml/yaml文件"""
        import yaml

        # 打开文件
        with open(self.path, "r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data

    def __getXmlConfig(self):

        return

    def __getJsonConfig(self):

        return

    def __getIniConfig(self):
        from configparser import ConfigParser
        cp = ConfigParser()
        cp.read(os.getcwd() + self.path, encoding="utf-8-sig")

        conf = {}

        '''获取所有的selections'''
        selections = cp.sections()
        for selection in selections:
            sel_dict = {}
            '''获取指定selections下的所有options'''
            options = cp.options(selection)
            for option in options:
                '''获取指定selection下的指定option的值'''
                value = cp.get(selection, option)
                sel_dict[option] = value

            conf[selection] = sel_dict

        return conf





