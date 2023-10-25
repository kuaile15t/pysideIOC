#!/usr/bin/python3
# coding: utf-8


def radius(*radiusNum, top_left=0, top_right=0, bottom_left=0, bottom_right=0, **kwargs):
    """
    设置圆角
    top_left、top_right、bottom_left、bottom_right具有优先级

    radiusNum可以指定0-4个角度
        1个时：整体设置为该角度  --> border-radius: 2px;
        按照左上、右上、左下、右下 顺序设定角度。
        多余4个时 多的会忽略。
        未指定角度时，无圆角
    """

    if radiusNum:
        if len(radiusNum) == 1:
            return f'border-radius: {radiusNum[0]}px;'

        if not top_left:
            # 能走到这里, 说明至少有两个值
            top_left = radiusNum[0]
        if not top_right:
            # 能走到这里, 说明至少有两个值
            top_right = radiusNum[1]
        if not bottom_left:
            if len(radiusNum) >= 3:
                bottom_left = radiusNum[2]
        if not bottom_right:
            if len(radiusNum) >= 4:
                bottom_right = radiusNum[3]

    res = ''
    if top_left:
        res += f'border-top-left-radius: {top_left}px;'
    if top_right:
        res += f'border-top-right-radius: {top_right}px;'
    if bottom_left:
        res += f'border-bottom-left-radius: {bottom_left}px;'
    if bottom_right:
        res += f'border-bottom-right-radius: {bottom_right}px;'

    return res


def border(*color, left=None, top=None, right=None, bottom=None, border_size=1, **kwargs):
    """
    设置边框
    各方向left、top、right、bottom具有优先级
    color可以指定0-4个颜色
        0个时：未指定颜色，无边框  --> border: 0;
        1个时：整体设置为该颜色  --> border: 1px solid #333333;
        按照左、上、右、下 顺序设定边框颜色。
        多余4个时 多的会忽略。
    """

    if color:
        if len(color) == 1:
            return f'border: {border_size}px solid {getColor(color[0])};'

        if not left:
            # 能走到这里, 说明至少有两个值
            left = color[0]
        if not top:
            # 能走到这里, 说明至少有两个值
            top = color[1]
        if not right:
            if len(color) >= 3:
                right = color[2]
        if not bottom:
            if len(color) >= 4:
                bottom = color[3]

    res = ''
    if left:
        res += f'border-left: {border_size}px solid {getColor(left)};'
    if top:
        res += f'border-top: {border_size}px solid {getColor(top)};'
    if right:
        res += f'border-right: {border_size}px solid {getColor(right)};'
    if bottom:
        res += f'border-bottom: {border_size}px solid {getColor(bottom)};'

    if not res:
        # 无边框
        return f'border: 0;'

    return res


def padding(*paddingNum, left=0, top=0, right=0, bottom=0, **kwargs):
    """
    :param bottom:
    :param right:
    :param top:
    :param left:
    :param paddingNum: int  只给一个值时整体都是相应值；多个值时，按照左、上、右、下赋值。 超过4个值时。多余的会忽略
    """
    if len(paddingNum) == 1:
        return f'padding: {paddingNum[0]}px;'

    if paddingNum:
        if not left:
            # 能走到这里, 说明paddingNum至少有两个值
            left = paddingNum[0]

        if not top:
            # 能走到这里, 说明paddingNum至少有两个值
            top = paddingNum[1]

        if not right:
            if len(paddingNum) >= 3:
                right = paddingNum[2]

        if not bottom:
            if len(paddingNum) >= 4:
                bottom = paddingNum[3]

    res = ''
    if left:
        res += f'padding-left: {left}px;'
    if top:
        res += f'padding-top: {top}px;'
    if right:
        res += f'padding-right: {right}px;'
    if bottom:
        res += f'padding-bottom: {bottom}px;'

    return res


def fontColor(color):
    col = getColor(color)
    if col:
        return f'color: {col};'


def fontSize(fontsize):
    return f'font: {fontsize}pt;'


def background(color=None):
    if color:
        col = getColor(color)
        if col:
            return f'background: {col};'
    return ''


# ========================================= 功能函数，不输出样式 =========================================================
def getColor(color):
    if isinstance(color, tuple):
        # rgb(255, 255, 255);  /  rgba(255, 255, 255, 0);
        if len(color) > 4 or len(color) < 3:
            # 参数错误
            print('背景颜色输入错误..')
            return

        # "()" 会跟随参数的clolo放入"f{}"
        if len(color) > 3:
            return f'rgba{color}'
        return f'rgb{color}'

    # : #ffffff;
    return f'{color}'


# ****************************************** 设置表格样式 *******************************************************

def setTableStyle(table, selectRow=False):
    """设置表格基本样式"""
    from PySide6.QtWidgets import QHeaderView

    # 表格设置
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 单元格自动伸缩填充
    table.setShowGrid(True)  # 是否显示网格线 false为不显示 true为显示
    if selectRow:
        from PySide6.QtWidgets import QTableWidget
        table.setSelectionBehavior(QTableWidget.SelectRows)  # 设置点击选中一行





