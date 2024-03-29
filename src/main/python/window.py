# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1732, 1203)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBoxInputImg = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxInputImg.sizePolicy().hasHeightForWidth())
        self.comboBoxInputImg.setSizePolicy(sizePolicy)
        self.comboBoxInputImg.setMinimumSize(QtCore.QSize(275, 0))
        self.comboBoxInputImg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxInputImg.setObjectName("comboBoxInputImg")
        self.comboBoxInputImg.addItem("")
        self.comboBoxInputImg.setItemText(0, "")
        self.comboBoxInputImg.addItem("")
        self.comboBoxInputImg.addItem("")
        self.comboBoxInputImg.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxInputImg, 2, 1, 1, 2)
        self.browseButton = QtWidgets.QPushButton(self.tab)
        self.browseButton.setObjectName("browseButton")
        self.gridLayout_2.addWidget(self.browseButton, 7, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBoxTrajectory = QtWidgets.QComboBox(self.tab)
        self.comboBoxTrajectory.setObjectName("comboBoxTrajectory")
        self.comboBoxTrajectory.addItem("")
        self.comboBoxTrajectory.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxTrajectory, 1, 1, 1, 2)
        self.cutoff_Ratio = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cutoff_Ratio.sizePolicy().hasHeightForWidth())
        self.cutoff_Ratio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cutoff_Ratio.setFont(font)
        self.cutoff_Ratio.setAlignment(QtCore.Qt.AlignCenter)
        self.cutoff_Ratio.setObjectName("cutoff_Ratio")
        self.gridLayout_2.addWidget(self.cutoff_Ratio, 6, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.runButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        self.runButton.setObjectName("runButton")
        self.gridLayout_2.addWidget(self.runButton, 10, 0, 1, 3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.resultHistText = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.resultHistText.setFont(font)
        self.resultHistText.setObjectName("resultHistText")
        self.gridLayout_3.addWidget(self.resultHistText, 0, 1, 1, 1)
        self.inputHist = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputHist.sizePolicy().hasHeightForWidth())
        self.inputHist.setSizePolicy(sizePolicy)
        self.inputHist.setMaximumSize(QtCore.QSize(16777215, 300))
        self.inputHist.setText("")
        self.inputHist.setObjectName("inputHist")
        self.gridLayout_3.addWidget(self.inputHist, 1, 0, 1, 1)
        self.inputHistText = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputHistText.sizePolicy().hasHeightForWidth())
        self.inputHistText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inputHistText.setFont(font)
        self.inputHistText.setObjectName("inputHistText")
        self.gridLayout_3.addWidget(self.inputHistText, 0, 0, 1, 1)
        self.resultHist = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultHist.sizePolicy().hasHeightForWidth())
        self.resultHist.setSizePolicy(sizePolicy)
        self.resultHist.setMinimumSize(QtCore.QSize(0, 0))
        self.resultHist.setMaximumSize(QtCore.QSize(16777215, 300))
        self.resultHist.setText("")
        self.resultHist.setObjectName("resultHist")
        self.gridLayout_3.addWidget(self.resultHist, 1, 1, 1, 1)
        self.outImgSI = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outImgSI.sizePolicy().hasHeightForWidth())
        self.outImgSI.setSizePolicy(sizePolicy)
        self.outImgSI.setText("")
        self.outImgSI.setObjectName("outImgSI")
        self.gridLayout_3.addWidget(self.outImgSI, 1, 2, 1, 1)
        self.outPic = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outPic.sizePolicy().hasHeightForWidth())
        self.outPic.setSizePolicy(sizePolicy)
        self.outPic.setStyleSheet("background-color: rgb(50, 65, 75);\n"
"")
        self.outPic.setText("")
        self.outPic.setAlignment(QtCore.Qt.AlignCenter)
        self.outPic.setObjectName("outPic")
        self.gridLayout_3.addWidget(self.outPic, 2, 0, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 4, 14, 1)
        self.inPic = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inPic.sizePolicy().hasHeightForWidth())
        self.inPic.setSizePolicy(sizePolicy)
        self.inPic.setMinimumSize(QtCore.QSize(0, 360))
        self.inPic.setMaximumSize(QtCore.QSize(16777215, 400))
        self.inPic.setText("")
        self.inPic.setObjectName("inPic")
        self.gridLayout_2.addWidget(self.inPic, 9, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 3)
        self.cutoffSlider = QtWidgets.QSlider(self.tab)
        self.cutoffSlider.setMinimum(1)
        self.cutoffSlider.setMaximum(100)
        self.cutoffSlider.setProperty("value", 50)
        self.cutoffSlider.setOrientation(QtCore.Qt.Horizontal)
        self.cutoffSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.cutoffSlider.setObjectName("cutoffSlider")
        self.gridLayout_2.addWidget(self.cutoffSlider, 5, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.inputImgLabel = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputImgLabel.sizePolicy().hasHeightForWidth())
        self.inputImgLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inputImgLabel.setFont(font)
        self.inputImgLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputImgLabel.setObjectName("inputImgLabel")
        self.gridLayout_2.addWidget(self.inputImgLabel, 8, 0, 1, 3)
        self.comboBoxSize = QtWidgets.QComboBox(self.tab)
        self.comboBoxSize.setObjectName("comboBoxSize")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxSize, 3, 1, 1, 2)
        self.inputImgSI = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputImgSI.sizePolicy().hasHeightForWidth())
        self.inputImgSI.setSizePolicy(sizePolicy)
        self.inputImgSI.setMaximumSize(QtCore.QSize(16777215, 360))
        self.inputImgSI.setText("")
        self.inputImgSI.setObjectName("inputImgSI")
        self.gridLayout_2.addWidget(self.inputImgSI, 12, 0, 2, 3)
        self.label_6 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 11, 0, 1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1732, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Medical Imaging Final Project"))
        self.comboBoxInputImg.setItemText(1, _translate("MainWindow", "Phantom 1"))
        self.comboBoxInputImg.setItemText(2, _translate("MainWindow", "Phantom 2"))
        self.comboBoxInputImg.setItemText(3, _translate("MainWindow", "Custom Img (Use Browse)"))
        self.browseButton.setText(_translate("MainWindow", "Browse Image"))
        self.label_3.setText(_translate("MainWindow", "Input Img:"))
        self.comboBoxTrajectory.setItemText(0, _translate("MainWindow", "Cartesian"))
        self.comboBoxTrajectory.setItemText(1, _translate("MainWindow", "Radial"))
        self.cutoff_Ratio.setText(_translate("MainWindow", "50%"))
        self.label.setText(_translate("MainWindow", "Acquisition Trajectory:"))
        self.runButton.setText(_translate("MainWindow", "Run"))
        self.resultHistText.setText(_translate("MainWindow", "Fourier Transform w/ Acquisition Trajectory Applied:"))
        self.inputHistText.setText(_translate("MainWindow", "Fourier Transform:"))
        self.label_7.setText(_translate("MainWindow", "Signal Intensity of Output Img w/ Trajectory Applied:"))
        self.label_2.setText(_translate("MainWindow", "Cutoff/Repetitions:"))
        self.label_5.setText(_translate("MainWindow", "Phantom Size:"))
        self.inputImgLabel.setText(_translate("MainWindow", "Input Image:"))
        self.comboBoxSize.setItemText(0, _translate("MainWindow", "512 x 512"))
        self.comboBoxSize.setItemText(1, _translate("MainWindow", "1028 x 1028"))
        self.comboBoxSize.setItemText(2, _translate("MainWindow", "2056 x 2056"))
        self.comboBoxSize.setItemText(3, _translate("MainWindow", "4096 x 4096 (Computationally Heavy)"))
        self.label_6.setText(_translate("MainWindow", "Input Image Signal Intensity:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Control"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

