#!/usr/bin/python3
# coding: utf-8


class Page:
    """
    目前尝试有基于树、字典、事件
    在使用中发现，使用树形结构存储和检索，效率不如基于hash表的字典，内存占用也没有量级的增加，因此使用字典来实现存储和检索

    -- 控制页面显示和隐藏 这里使用的是直接控制，可以定义事件，让qt自己去显示和隐藏
    ---- 这里是显示（show）和隐藏（hide）。如果内存紧张，可以修改为生成和销毁。也可以混用

    """

    def __init__(self):

        # 树根 --》 所有节点
        self.pages = Node()

        self.now = None

    def goto(self, loadPath, *args):
        if not loadPath:
            print('路径为空')
            return
        if self.now:
            if loadPath == self.now.path:
                # 跳转界面为已显示界面
                print('当前界面')
                return

        node = self.querypage(loadPath)

        if not node:
            # 根据路径无法找到节点
            print('未找到节点')
            return

        if self.now:
            self.hide(self.now, *args)
        self.show(node, *args)
        self.now = node

    def querypage(self, loadPath):
        return self.querynode(self.pages, loadPath.split('.'), 0)

    def addPage(self, win):
        win.hide()  # 隐藏页面
        # win.close()  # 关闭页面,大部分情况下是隐藏，通hide()

        pathList = win.path.split('.')  # login.log.s.a  --> [login,log,s,a]
        a_node = Node(win, pathList[-1], pathList)
        return self.addnode(self.pages, a_node, 0)

    def addnode(self, node, a_node, index):
        """
        1.2.3.4  【1,2,3,4】

        判断当前条件是否相等
        相等：
            判断当前条件是否为 新增节点 的最后一个条件
            是：
                判断节点是否存在窗口
                    存在：返回错误（路径重复）
                    不存在：置换当前节点
            否：
                判断左侧是否存在节点
                    存在：继续与左节点对比下一条件
                    不存在：根据剩余索引建立节点，置于左侧
        不相等：
            判断右侧是否存在节点
                存在：继续与右节点对比当前条件
                不存在：根据剩余索引建立节点，置于右侧
        """
        a_pathList = a_node.pathList
        if node.path == a_pathList[index]:
            # 相等 True 左
            if index + 1 >= len(a_pathList):
                # 是最后一个条件
                if node.page:
                    print('路径重复', node.pathList)
                    return 2
                # 最后一个条件，路径不重复 --》 直接置换当前节点
                # 实际上就是把页面对象赋值给当前节点
                node.page = a_node.page
                return 1
            # 不是最后一个条件
            if node.left:
                return self.addnode(node.left, a_node, index + 1)
            # 正常添加
            # rnode = self.createNodeByPathList(a_node, a_pathList, index)
            node.left = self.createNodeByPathList(a_node, a_pathList, index).left
            return 1

        # 不相等 false 右
        if node.right:
            return self.addnode(node.right, a_node, index)
        node.right = self.createNodeByPathList(a_node, a_pathList, index)
        return 1

    def querynode(self, node, pathList, index):
        """
        1.2.3.4  【1,2,3,4】

        判断当前条件是否相等
        相等：
            判断当前条件是否为 新增节点 的最后一个条件
            是：
                返回当前节点
            否：
                判断左侧是否存在节点
                    存在：继续与左节点对比下一条件
                    不存在：页面不存在，返回空
        不相等：
            判断右侧是否存在节点
                存在：继续与右节点对比当前条件
                不存在：页面不存在，返回空
        """

        if node.path == pathList[index]:
            if index + 1 >= len(pathList):
                # 是最后一个条件
                return node
            # 不是最后一个条件
            if node.left:
                return self.querynode(node.left, pathList, index + 1)
            return

        # 不相等 false 右
        if node.right:
            return self.querynode(node.right, pathList, index)
        return

    def getCount(self):
        count = []
        self.getNodeCount(self.pages, count)
        print(len(count))

    def getNodeCount(self, node, count):
        if node.page:
            # print(node.path)
            # count.append(1)
            pass
        count.append(1)
        if node.left:
            self.getNodeCount(node.left, count)
        if node.right:
            self.getNodeCount(node.right, count)

    @classmethod
    def show(cls, node, *args):
        if hasattr(node.page, 'load'):
            node.page.load(*args)
        node.page.show()

    @classmethod
    def hide(cls, node, *args):
        if hasattr(node.page, 'unload'):
            node.page.unload(*args)
        node.page.hide()

    def close(self, *args):
        if self.now:
            self.hide(self.now, *args)

    # ==================================== util ===========================================

    def simplifyTree(self, tree):
        """
        ===== 不能简化，一旦简化路径不全，无法查询 =====

        简化需要符合2个条件：
            1.本节点没有界面
            2.只有一个下级节点（左 或者 右）

        判断是否有页面
        是：
            是否有左节点 有：继续判断左节点
            是否有右节点 有：继续判断右节点
        否：
            是否只有一个下级节点  是：置换，继续判断

        """
        pass

    def simplifyTreeUtil(self, node):
        # 不对
        if node.page:
            if node.left:
                self.simplifyTreeUtil(node)
            if node.right:
                pass

    def createNodeByPathList(self, a_node, path_list, index):
        # [1, 2, 3] --> [2, 3]
        if index + 1 >= len(path_list):
            return a_node
        rNode = Node(None, path_list[index])
        rNode.left = self.createNodeByPathList(a_node, path_list, index + 1)
        return rNode
        # 循环方式建立
        # rNode = None
        # for i in range(index, len(path_list)):
        #     tNode = Node(None, i)
        #     if not rNode:
        #         rNode = tNode

    # ----------------------------------- 另一种思路 -----------------------------------------------------------
    def querypage1(self, path):
        pathList = path.split('.')
        node = self.pages
        for i in pathList:
            node = self.querynode1(node, i)
        return node

    def querynode1(self, node, path):
        # 逻辑不对
        if not node:
            return None
        if node.path == path:
            return node.left
        return self.querynode1(node.right, path)


class Node:

    def __init__(self, page=None, path='root', pathList=None, left=None, right=None):
        self.left = left
        self.right = right
        self.page = page
        self.path = path
        self.pathList = pathList


# if __name__ == '__main__':
#     a = Page()
#
#     p = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     pathlist = []
#
#     for i in range(100000):
#         path_l = []
#         while True:
#             length = random.randint(1, 9)
#             # length = 3
#             while len(path_l) != length:
#                 index = random.randint(0, len(p) - 1)
#                 path_l.append(p[index])
#             path = '.'.join(path_l)
#             if path not in pathlist:
#                 pathlist.append(path)
#                 break
#             else:
#                 path_l = []
#                 print('重建')
#     # print(pathlist)
#
#     pathlist = ['1.3.2', '2.1.3.4', '2.3.3', '4.3.1.2', '4.3.4.3', '1.2', '1.3', '4', '2', '4.2', '4.3.3', '3.3.1.3',
#                 '1.4', '1.1.1', '1.3.1', '1.1.3.4', '4.3.1', '1', '3', '4.1.1', '4.1', '2.1.2', '4.4.4', '2.3',
#                 '2.4.4', '4.2.4', '3.4.1', '2.2.3.1', '3.2.2.2', '2.4']
#
#     t1 = time.time()
#
#     for i in pathlist:
#         C = type('ZhishikuMain', (object,), {'path': i})
#         cc = C()
#         re_s = a.addPage(cc)
#         if not re_s:
#             print('添加失败', re_s)
#
#     t2 = time.time()
#     print(t2 - t1)
#
#     print('====================================== 查询 ===========================================')
#     t1 = time.time()
#     for i in range(100000):
#         index = random.randint(0, len(pathlist) - 1)
#         # index = 6
#
#         b = a.querypage(pathlist[index])
#         # b = a.querypage1(pathlist[index])
#
#         if b:
#             if pathlist[index][-1] != b.path:
#                 print(b.path, ':', index)
#         else:
#             print(b)
#     t2 = time.time()
#     print(t2 - t1)
#
#     print('=================================================================================')
#     a.getCount()


