#!/usr/bin/python3
# coding: utf-8
import os

from .configfile import ConfigFile
from ...common.configurationfile import f_business, f_classpath, f_annotate, f_annotate_no, f_exceptpath, plu_plugins, \
    plu_name


class Config:
    """
    获取配置及bean对象
    1.读取配置文件
        配置文件类型为：'.yaml'、'.xml'、'.json'、'.ini'  优先级顺序为：yaml、xml、json、ini
        1.将配置文件放在:
            应用运行目录下 'resource' 文件夹下，文件名称为 'config'
        2.指定完整路径:
            (1) 相对路径：从应用运行目录开始 如：src/resource/config.yaml
            (2) 绝对路径：从磁盘开始 如：D:/app/src/resource/config.yaml

    2.扫描注解（特定装饰器）

    """
    def __init__(self, path=''):

        # 配置
        self.config = {}

        # bean对象
        self.bean = {}

        # 配置文件
        self.cf = ConfigFile(path)

    def getConfig(self):

        # 获取配置文件配置
        conf = self.cf.getConfig()

        if conf:

            self.__processConfigFile(conf)
            if 'env' in conf and conf['env'] == 'production':
                self.bean['annotate'] = self.__getCustomizeModels()

        # 配置文件不存在
        pass

    def __processConfigFile(self, conf):
        """ 分解配置数据. bean路径、插件配置、组件配置... """

        # ############# bean路径 ###################
        exceptList = []
        if conf.get(f_business):
            if conf.get(f_business).get(f_annotate):
                # 扫描文件的路径
                clsPath = conf.get(f_business).get(f_annotate).get(f_classpath)
                if clsPath:
                    annList = self.getModelPath(clsPath)
                    if annList:
                        self.bean[f_annotate] = annList

            # 实例文件的路径
            clsPath = conf.get(f_business).get(f_classpath)
            if clsPath:
                instList = self.getModelPath(clsPath)
                if instList:
                    self.bean[f_annotate_no] = instList

            # 排除的路径
            excPath = conf.get(f_business).get(f_exceptpath)
            if excPath:
                exceptList = self.getModelPath(excPath)

        # 不扫描具有优先级，将扫描列表里 与不扫描列表的重复项删除 =============================
        if self.bean.get(f_annotate_no):
            for ann_index in reversed(range(len(self.bean[f_annotate]))):
                if self.bean[f_annotate][ann_index] in self.bean[f_annotate_no]:
                    self.bean[f_annotate].pop(ann_index)

        # 将排除的路径从bean路径里删除 =============================
        if exceptList:
            for key in self.bean:
                paths = self.bean[key]
                for path_index in reversed(range(len(paths))):
                    if paths[path_index] in exceptList:
                        paths.pop(path_index)

        # ############# 组件配置 ################

        # ############# 插件配置 ################
        if conf.get(plu_plugins):
            # {pagemanager: {'name':'page', 'classpath':'pagemanager.PageManager', 'parameter':{'mainwin': 'main.bb'}}}
            for f_plName in conf.get(plu_plugins):
                # f_plName为插件名  pagemanager
                if plu_name not in conf[plu_plugins][f_plName] or not conf[plu_plugins][f_plName][plu_name]:
                    conf[plu_plugins][f_plName][plu_name] = f_plName

        # 将配置数据赋值给配置对象
        self.config = conf

    def getModelPath(self, paths):
        """
        __import__需要路径为文件级别，因此定义获取到文件
        ps: __import__(view_dict[file_name], fromlist=[''])
        :param paths 路径
        """
        fileList = []
        if paths.__class__ is list:
            # paths为路径列表，循环获取
            for path in paths:
                fileList += self.__getFilePath(path)
                pass
        else:
            # paths为单个路径，直接获取
            fileList += self.__getFilePath(paths)

        return fileList

    def __getFilePath(self, paths):
        # 判断路径是否为文件。 文件：输出  文件夹：获取文件夹及子文件夹中所有文件路径
        p = paths.replace('.', "/")
        # 文件
        if os.path.isfile(p + '.py'):
            return [paths]
        # 文件夹
        if os.path.isdir(p):
            fileList = []
            self.__getFilePathByDir(fileList, p, paths)
            return fileList
        return []

    def __getFilePathByDir(self, fileList, dirPath, baseLoad):
        """根据路径，列出所有py文件"""
        for item in os.listdir(dirPath):
            if item.startswith("__"):
                continue

            if item.endswith('.py'):
                fileName = item[:item.rfind('.')]
                fileList.append(baseLoad + '.' + fileName)
                continue

            if os.path.isdir(dirPath + r'/' + item):
                self.__getFilePathByDir(fileList, dirPath + r'/' + item, baseLoad + '.' + item)

    def __getCustomizeModels(self):
        """列出所有导入系统的模块"""
        import sys
        modules = []
        for m in sys.modules:

            if '__init__' in str(sys.modules[m]):
                continue
            if m.startswith('core.view.ui'):
                continue
            if m.startswith('core.view.style'):
                continue

            if m.startswith('core'):
                modules.append(m)
                # print('模块名:', m, '模块来源:', sys.modules[m])
        return modules









