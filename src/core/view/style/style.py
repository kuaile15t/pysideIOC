#!/usr/bin/python3
# coding: utf-8
from .stylecommon import allstyle, btnstyle, color_cheng, btnhover, color_shenlan, color_qianlan, lineEditstyle, \
    comboBoxstyle, color_white, color_shenlan_3, color_shenlan_2
from .styleutils import background, fontSize, fontColor, radius, padding, border

# ========================== 整体样式 ===================================
# 背景
mainBackground = background(color_shenlan)
# 字体
mainFontSize = fontSize(11)
# 字体颜色
mainFontColor = fontColor(color_white)

all_style = allstyle.format(mainBackground + mainFontSize + mainFontColor)

# ################################## 按钮 #######################################
# 偏移
mainBtnSpace = padding(15, 7, 15, 7)
# 按钮边框
# mainBtnBorder = border((45, 130, 185))
mainBtnBorder = border('#2d82b9')
# 按钮圆角
mainBtnRadius = radius(2)
# 按钮字体
mainBtnFontSize = fontSize(10)
# 按钮背景颜色
mainBtnBg = background(color_qianlan)

btn_style = btnstyle.format(mainBtnSpace + mainBtnRadius + mainBtnFontSize + mainBtnBg + mainBtnBorder)
# btn_style = btnstyle.format(mainBtnSpace + mainBtnRadius + mainBtnFontSize + mainBtnBg)

# ###### 边框鼠标指向按钮后更改的样式 ######
# 按钮边框
mainBtnBorderHover = border(bottom=(55, 226, 236), border_size=2)
# 按钮字体颜色
mainBtnFontColorHover = fontColor(color_cheng)
# 按钮背景颜色
mainBtnBgHover = background(color_shenlan_3)

btn_hover_style = btnhover.format(mainBtnBorderHover + mainBtnFontColorHover + mainBtnBgHover)

# ################################## 输入框 #######################################
# 背景
lineEditBg = background(color_shenlan_2)
# 边框
lineEditBorder = border((27, 114, 181))
# 偏移
lineEditSpace = padding(5)

lineEdit_style = lineEditstyle.format(lineEditBg + lineEditBorder + lineEditSpace)

# ################################## 下拉菜单 #######################################
# 背景
comboBoxBg = background(color_shenlan_2)
# 边框
comboBoxBorder = border((27, 114, 181))
# 偏移
comboBoxSpace = padding(5)
# 字体
# comboBoxFontSize = fontSize(10)

comboBox_style = comboBoxstyle.format(comboBoxBorder + comboBoxSpace + comboBoxBg)

# ################################## 表格 #######################################

# 顶部标题栏
headerStyle = f'''QHeaderView::section{{{background(color_shenlan) + border() + padding(8)}}}'''

# 左上角
# '{border: 0px solid #6cc7fe;border-radius:0px;border-color: rgb(41, 139, 201);font: bold 11pt;padding:12px 0 0 10px;}'
left_top_style = f'QTableCornerButton::section {{{background(color_shenlan) + border()}}}'

table_style = 'QTableView ' + headerStyle + left_top_style


pageStyle = all_style + btn_style + btn_hover_style + lineEdit_style + comboBox_style + table_style








