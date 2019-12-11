# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tool.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow , QApplication
import pandas
import cv2


class Ui_Tool_of_Marking(object):
    pic = ''
    def setupUi(self, Tool_of_Marking):
        Tool_of_Marking.setObjectName("Tool_of_Marking")
        Tool_of_Marking.resize(1124, 604)
        self.centralwidget = QtWidgets.QWidget(Tool_of_Marking)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(919, 190, 181, 195))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_search = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.button_search.setObjectName("button_search")
        self.verticalLayout_3.addWidget(self.button_search)
        self.button_up = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.button_up.setObjectName("button_up")
        self.verticalLayout_3.addWidget(self.button_up)
        self.button_down = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.button_down.setObjectName("button_down")
        self.verticalLayout_3.addWidget(self.button_down)
        self.button_save = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.button_save.setObjectName("button_save")
        self.verticalLayout_3.addWidget(self.button_save)
        self.slider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.verticalLayout_3.addWidget(self.slider)
        self.output = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(12)
        self.output.setFont(font)
        self.output.setText("")
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")
        self.verticalLayout_3.addWidget(self.output)

        self.picture = QtWidgets.QScrollArea(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(10, 10, 891, 531))
        self.picture.setWidgetResizable(False)
        self.picture.setObjectName("picture")

        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 889, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        
        self.Display = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Display.setGeometry(QtCore.QRect(1, 4, 881, 521))
        self.Display.setObjectName("Display")
        self.picture.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(890, 30, 191, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.r_title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(12)
        self.r_title.setFont(font)
        self.r_title.setFocusPolicy(QtCore.Qt.NoFocus)
        self.r_title.setScaledContents(False)
        self.r_title.setAlignment(QtCore.Qt.AlignCenter)
        self.r_title.setObjectName("r_title")
        self.verticalLayout.addWidget(self.r_title)
        self.g_title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(12)
        self.g_title.setFont(font)
        self.g_title.setAlignment(QtCore.Qt.AlignCenter)
        self.g_title.setObjectName("g_title")
        self.verticalLayout.addWidget(self.g_title)
        self.b_title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(12)
        self.b_title.setFont(font)
        self.b_title.setAlignment(QtCore.Qt.AlignCenter)
        self.b_title.setObjectName("b_title")
        self.verticalLayout.addWidget(self.b_title)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.r_value = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r_value.sizePolicy().hasHeightForWidth())
        self.r_value.setSizePolicy(sizePolicy)
        self.r_value.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(11)
        self.r_value.setFont(font)
        self.r_value.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.r_value.setObjectName("r_value")
        self.verticalLayout_2.addWidget(self.r_value)
        self.g_value = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_value.sizePolicy().hasHeightForWidth())
        self.g_value.setSizePolicy(sizePolicy)
        self.g_value.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(11)
        self.g_value.setFont(font)
        self.g_value.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.g_value.setObjectName("g_value")
        self.verticalLayout_2.addWidget(self.g_value)
        self.b_value = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.b_value.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_value.sizePolicy().hasHeightForWidth())
        self.b_value.setSizePolicy(sizePolicy)
        self.b_value.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(11)
        self.b_value.setFont(font)
        self.b_value.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.b_value.setObjectName("b_value")
        self.verticalLayout_2.addWidget(self.b_value)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        Tool_of_Marking.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tool_of_Marking)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        Tool_of_Marking.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tool_of_Marking)
        self.statusbar.setObjectName("statusbar")
        Tool_of_Marking.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Tool_of_Marking)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Tool_of_Marking)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(Tool_of_Marking)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionUndo = QtWidgets.QAction(Tool_of_Marking)
        self.actionUndo.setObjectName("actionUndo")
        self.actionNext = QtWidgets.QAction(Tool_of_Marking)
        self.actionNext.setObjectName("actionNext")
        self.actionUp = QtWidgets.QAction(Tool_of_Marking)
        self.actionUp.setObjectName("actionUp")
        self.actionDown = QtWidgets.QAction(Tool_of_Marking)
        self.actionDown.setObjectName("actionDown")
        self.actionMagnify = QtWidgets.QAction(Tool_of_Marking)
        self.actionMagnify.setObjectName("actionMagnify")
        self.actionShrink = QtWidgets.QAction(Tool_of_Marking)
        self.actionShrink.setObjectName("actionShrink")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuEdit.addAction(self.actionUp)
        self.menuEdit.addAction(self.actionDown)
        self.menuEdit.addAction(self.actionMagnify)
        self.menuEdit.addAction(self.actionShrink)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        # 设置快捷键
        self.actionOpen.setShortcut("Ctrl+E")
        self.actionMagnify.setShortcut("Ctrl+I")
        self.actionShrink.setShortcut("Ctrl+O")                     # 设置快捷键

        self.retranslateUi(Tool_of_Marking)
        #按键连接
        self.actionOpen.triggered.connect(self.show_img_in_lable_center)
        self.actionShrink.triggered.connect(self.Shrink)
        self.actionMagnify.triggered.connect(self.Magnify)
        #self.button_save.clicked.connect(self.img_save)
        QtCore.QMetaObject.connectSlotsByName(Tool_of_Marking)

    def retranslateUi(self, Tool_of_Marking):
        _translate = QtCore.QCoreApplication.translate
        Tool_of_Marking.setWindowTitle(_translate("Tool_of_Marking", "MainWindow"))
        self.button_search.setText(_translate("Tool_of_Marking", "Search"))
        self.button_up.setText(_translate("Tool_of_Marking", "上一张"))
        self.button_down.setText(_translate("Tool_of_Marking", "下一张"))
        self.button_save.setText(_translate("Tool_of_Marking", "保存"))
        self.Display.setText(_translate("Tool_of_Marking", "Display"))
        self.r_title.setText(_translate("Tool_of_Marking", "R"))
        self.g_title.setText(_translate("Tool_of_Marking", "G"))
        self.b_title.setText(_translate("Tool_of_Marking", "B"))
        self.menuFile.setTitle(_translate("Tool_of_Marking", "File"))
        self.menuEdit.setTitle(_translate("Tool_of_Marking", "Edit"))
        self.actionOpen.setText(_translate("Tool_of_Marking", "Open"))
        self.actionSave.setText(_translate("Tool_of_Marking", "Save"))
        self.actionSave_as.setText(_translate("Tool_of_Marking", "Save as"))
        self.actionUndo.setText(_translate("Tool_of_Marking", "Undo"))
        self.actionNext.setText(_translate("Tool_of_Marking", "Next"))
        self.actionUp.setText(_translate("Tool_of_Marking", "Up        ctrl+left"))
        self.actionDown.setText(_translate("Tool_of_Marking", "Down   ctrl+right"))
        self.actionMagnify.setText(_translate("Tool_of_Marking", "Magnify"))
        self.actionShrink.setText(_translate("Tool_of_Marking", "Shrink"))
       

    #def img_save(self):
    #    fname,ftype = QtWidgets.QFileDialog.getSaveFileName(None, "另存为文件", "C:/Users/liste/Desktop", "All Files(*);;Image Files(*.jpg *.png)")#选取路径
    #    QScreen *screen = QGuiApplication.primaryScreen()

    def Magnify(self):
        global pic
        pix_map =  pic
        print(self.Display.width())
        print(self.Display.height())
        #缩小比例
        scale_m = 1.2
        #定义临时变量来存储长宽
        width = int(self.Display.width()*scale_m)
        height= int(self.Display.height()*scale_m)
        #改变控件的长宽
        self.Display.setFixedWidth(self.Display.width()*scale_m)
        self.Display.setFixedHeight(self.Display.height()*scale_m)
        self.scrollAreaWidgetContents.resize(width,height)

        scaredPixmap = pix_map.scaled(QSize(width, height), aspectRatioMode = Qt.KeepAspectRatio) 
        self.Display.setPixmap(QtGui.QPixmap.fromImage(scaredPixmap))
        print(width)
        print(height)
        print(self.Display.width())
        print(self.Display.height())
        pic = pix_map

    def Shrink(self):
        global pic
        pix_map =  pic
        print(self.Display.width())
        print(self.Display.height())
        #缩小比例
        scale_s = 0.8
        #定义临时变量来存储长宽
        width = int(self.Display.width()*scale_s)
        height= int(self.Display.height()*scale_s)
        #改变控件的长宽
        self.Display.setFixedWidth(self.Display.width()*scale_s)
        self.Display.setFixedHeight(self.Display.height()*scale_s)
        self.scrollAreaWidgetContents.resize(width,height)

        scaredPixmap = pix_map.scaled(QSize(width, height), aspectRatioMode = Qt.KeepAspectRatio) 
        self.Display.setPixmap(QtGui.QPixmap.fromImage(scaredPixmap))
        print(width)
        print(height)
        print(self.Display.width())
        print(self.Display.height())
        pic = pix_map

        #读取和显示图片
    def show_img_in_lable_center(self):
        #label表示要用来显示图片的那个标签~
        #fname表示事先获取到的要打开的图片文件名（含路径），可用QtWidgets.QFileDialog.getOpenFileName()获取哈~
        #print(fname) #显示文件名
        fname,ftype = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", "C:/Users/liste/Desktop", "All Files(*);;Image Files(*.jpg *.png)")#选取路径

        #尝试判断文件打开失败
            #if(fname.isEmpty()):
            #    self.output.setText("打开失败！")   
        
        pix_img = QImage(fname)
        global pic 
        pic = pix_img

        # Qt.KeepAspectRatio设置为等比例缩放
        # Qt.IgnoreAspectRatio为不按比例缩放
        #scaredPixmap = pix_map.scaled(QSize(1000, 2000), aspectRatioMode = Qt.KeepAspectRatio)
        img_w = pix_img.width()
        img_h = pix_img.height()
        lab_w = self.Display.width()
        lab_h = self.Display.height()
        if (img_w > lab_w) | (img_h > lab_h):
           #若图片宽高大于label宽高，则在label居中显示按图片原始比例缩放后的图片
            w_rate = float(img_w) / float(lab_w)
            h_rate = float(img_h) / float(lab_h)
            if w_rate >= h_rate:
               w = lab_w
               h = int(img_h / w_rate)
            else:
               w = int(img_w / h_rate)
               h = lab_h
        else:
            #若图片宽高都小于label宽高，则按图片原始大小显示
            w = img_w
            h = img_h
        self.Display.setPixmap(QtGui.QPixmap.fromImage(pix_img.scaled(w,h)))
        self.output.setText("打开成功！")   #显示打开文件成功


if  __name__=="__main__":
    #全局变量
    #图片变量
    #pic = ''
    import  sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QMainWindow()
    ui=Ui_Tool_of_Marking()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
