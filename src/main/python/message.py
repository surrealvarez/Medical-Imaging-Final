# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mssgWidget(object):
    def setupUi(self, mssgWidget):
        mssgWidget.setObjectName("mssgWidget")
        mssgWidget.resize(254, 125)
        self.verticalLayout = QtWidgets.QVBoxLayout(mssgWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mssgLabel = QtWidgets.QLabel(mssgWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mssgLabel.setFont(font)
        self.mssgLabel.setText("")
        self.mssgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mssgLabel.setObjectName("mssgLabel")
        self.verticalLayout.addWidget(self.mssgLabel)

        self.retranslateUi(mssgWidget)
        QtCore.QMetaObject.connectSlotsByName(mssgWidget)

    def retranslateUi(self, mssgWidget):
        _translate = QtCore.QCoreApplication.translate
        mssgWidget.setWindowTitle(_translate("mssgWidget", "Warning!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mssgWidget = QtWidgets.QWidget()
    ui = Ui_mssgWidget()
    ui.setupUi(mssgWidget)
    mssgWidget.show()
    sys.exit(app.exec_())

