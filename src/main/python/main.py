import locale
import sys
import numpy
import cv2

import qdarkstyle
from PyQt5.QtWidgets import QMainWindow
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from window import Ui_MainWindow
from FT import DFT
from message import Ui_mssgWidget
from message import Ui_mssgWidget
from matplotlib import pyplot as plt
from PyQt5 import QtCore
# from QtCore import Qt
# from PIL import Image
import os
from scipy import stats

locale.setlocale(locale.LC_ALL, '')
# import operator
path = os.path.dirname(os.path.abspath(__file__))



class Main(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        self.actionQuit.triggered.connect(QApplication.quit)
        self.browseButton.clicked.connect(self.openFile) # This is used as a signal to browse for an img
        self.runButton.clicked.connect(self.onClickRun) # This runs the function OnClickRun when run button is clicked
        self.functionSelected = str(self.comboBoxTrajectory.currentText()) # Current trajectory selected
        self.imgSelect = str(self.comboBoxInputImg.currentText()) # Current img Choice selected
        self.phantomSizeSelected = str(self.comboBoxSize.currentText()) # Select size of Phantom
        # print(self.functionSelected)
        # self.comboBox.activated[str].connect(self.onComboClicked)
        # self.comboBoxHistShapingParams.activated[str].connect(self.onComboClicked2)
        self.comboBoxInputImg.currentTextChanged.connect(self.onComboClicked)
        # self.histScaleSlider.valueChanged.connect(self.histScaleValue.setNum)
        self.cutoffSlider.valueChanged.connect(self.cutoffLabel)
        self.cutoffValue = float(self.cutoffSlider.value())/100

        self.MRI = DFT()

    def compute_histogram(self,image):

        hist = [0] * 256
        r, c = image.shape

        for i in range(r):
            for j in range(c):
                hist[image[i, j]] = hist[image[i, j]] + 1

        return hist

    def cutoffLabel(self,value):
        self.cutoffValue = float(value)/100
        self.cutoff_Ratio.setText(str(self.cutoffValue) + '%')

    # # --------------------------------------------------------------------------------------------------------------
    # ######## THIS METHOD IS IN CHARGE OF KEEPING TRACK OF WHICH FUNCTION IS SELECTED IN THE DROP DOWN MENY #########
    # def onComboClicked2(self, text):
    #     # Here, we change the value of global
    #     self.functionSelectedParam = str(self.comboBoxHistShapingParams.currentText())
    #     print(self.functionSelectedParam)
    # ################################################################################################################
    #
    # # --------------------------------------------------------------------------------------------------------------
    # ######## THIS METHOD IS IN CHARGE OF KEEPING TRACK OF WHICH FUNCTION IS SELECTED IN THE DROP DOWN MENU #########
    def onComboClicked(self):
        self.inPic.clear() # We first clear the img
        self.name = '' # RESETS self.name
        inputDir = path + '/Inputs/'

        if not os.path.exists(inputDir):
            os.makedirs(inputDir)

        # Here, we change the value of global
        self.inputImgSelection = str(self.comboBoxInputImg.currentText())
        # IF a phantom is selected, we disable the browse button
        if self.inputImgSelection == 'Phantom 1':
            self.name = '' # RESETS self.name
            inputDirP1 = inputDir + 'phantom1.jpg'
            self.browseButton.setEnabled(False)
            img = self.MRI.phantom1(360,360)
            cv2.imwrite(os.path.join(inputDir,'phantom1.jpg'), img)

            self.pixmap = QPixmap(appctxt.get_resource(inputDirP1))
            self.inPic.setPixmap(self.pixmap.scaled(self.inPic.width(), self.inPic.height(), QtCore.Qt.KeepAspectRatio))
            self.inPic.setAlignment(QtCore.Qt.AlignCenter)

        elif self.inputImgSelection == 'Phantom 2':
            self.name = '' # RESETS self.name
            inputDirP2 = inputDir + 'phantom2.jpg'
            self.browseButton.setEnabled(False)
            img = self.MRI.phantom2(360,360)
            cv2.imwrite(os.path.join(inputDir,'phantom2.jpg'), img)

            self.pixmap = QPixmap(appctxt.get_resource(inputDirP2))
            self.inPic.setPixmap(self.pixmap.scaled(self.inPic.width(), self.inPic.height(), QtCore.Qt.KeepAspectRatio))
            self.inPic.setAlignment(QtCore.Qt.AlignCenter)
        # ELSE, the browse button is available
        else:
            self.browseButton.setEnabled(True)
    # ################################################################################################################

    # --------------------------------------------------------------------------------------------------------------
    ###### THIS FUNCTION BROWSES AND SAVES THE PIXMAP OF INPUT IMG AND FILEPATH OF INPUT IMAGE AS self.name #######
    def openFile(self):

        try:
            self.name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
            print(self.name,'  Input Img')
            self.pixmap = QPixmap(appctxt.get_resource(self.name))
            self.inPic.setPixmap(self.pixmap.scaled(self.inPic.width(), self.inPic.height(), QtCore.Qt.KeepAspectRatio))
            self.inPic.setAlignment(QtCore.Qt.AlignCenter)

        except:
            pass
    ################################################################################################################

    def onClickRun(self):


        cutoffFactor = float(self.cutoffValue)
        outputDir = 'Output/'
        outputDir2 = path + '/Output/'

        # Here we do the operation for the Cartesian function

        try:
            self.inputHist.clear()
            self.resultHist.clear()
            self.inputImgSI.clear()
            self.outImgSI.clear()
        except:
            print("ERROR!!!")

        # If the chosen img is Phantom1, we then define the size by the selected Size
        if str(self.comboBoxInputImg.currentText()) == 'Phantom 1':
            if(str(self.comboBoxSize.currentText()) == '512 x 512'):
                # print(512)
                size = 512
                img = self.MRI.phantom1(512,512)
            elif(str(self.comboBoxSize.currentText()) == '1028 x 1028'):
                # print(1028)
                size = 1028
                img = self.MRI.phantom1(1028, 1028)
            elif(str(self.comboBoxSize.currentText()) == '2056 x 2056'):
                # print(2056)
                size = 2056
                img = self.MRI.phantom1(2056, 2056)
            elif(str(self.comboBoxSize.currentText()) == '4096 x 4096'):
                # print(4096)
                size = 4096
                img = self.MRI.phantom1(4096,4096)
        # If the chosen img is Phantom1, we then define the size by the selected Size
        elif str(self.comboBoxInputImg.currentText()) == 'Phantom 2':
            if(str(self.comboBoxSize.currentText()) == '512 x 512'):
                # print(512)
                size = 512
                img = self.MRI.phantom2(512,512)
            elif(str(self.comboBoxSize.currentText()) == '1028 x 1028'):
                # print(1028)
                size = 1028
                img = self.MRI.phantom2(1028, 1028)
            elif(str(self.comboBoxSize.currentText()) == '2056 x 2056'):
                # print(2056)
                size = 2056
                img = self.MRI.phantom2(2056, 2056)
            elif(str(self.comboBoxSize.currentText()) == '4096 x 4096 (Computationally Heavy)'):
                # print(4096)
                size = 4096
                img = self.MRI.phantom2(4096,4096)
        # If the chosen imgs is Custom, we browse for an img
        elif str(self.comboBoxInputImg.currentText()) == "Custom Img (Use Browse)":
            try:
                img = cv2.imread(self.name, 0)
                height, width = img.shape
                size = height
            except:
                self.mssgBox = QWidget()
                message = Ui_mssgWidget()
                message.setupUi(self.mssgBox)
                message.mssgLabel.setText("Browse for an\nimage first!")
                self.mssgBox.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint |
                                            QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
                self.mssgBox.show()
                return


        # height, width = img.shape

        img = self.MRI.shiftedDFT(img)
        kSpaceImgOut = self.MRI.prepareOutput(img) # Fourier transform Output with Cutoff
        cv2.imwrite(os.path.join(outputDir2,'kSpaceImg.jpg'),kSpaceImgOut)

        kSpaceImgOut = cv2.imread(outputDir2 + '/kSpaceImg.jpg', 0)
        inHist = self.compute_histogram(kSpaceImgOut)
        # TO COMPUTE SI AND DISPLAY
        plt.clf()
        inHist_fig = plt.plot(inHist)
        plt.savefig(outputDir2 + '/Input_SI_Graph.png')
        self.pixmapInSI = QPixmap(outputDir2 + '/Input_SI_Graph.png')
        self.inputImgSI.setPixmap(self.pixmapInSI.scaled(self.inputImgSI.width(), self.inputImgSI.height(), QtCore.Qt.KeepAspectRatio))
        self.inputImgSI.setAlignment(QtCore.Qt.AlignCenter)

        self.pixmapInHist = QPixmap(outputDir2 + '/kSpaceImg.jpg')
        self.inputHist.setPixmap(self.pixmapInHist.scaled(self.inputHist.width(), self.inputHist.height(), QtCore.Qt.KeepAspectRatio))
        self.inputHist.setAlignment(QtCore.Qt.AlignCenter)

        cutoff = cutoffFactor * size

        if str(self.comboBoxTrajectory.currentText()) == "Cartesian":
            outCartesianPath = path + '/Output/Cartesian_Output/'
            if not os.path.exists(outCartesianPath):
                os.makedirs(outCartesianPath)

            kSpaceImgCut = self.MRI.cartesianMask(img, cutoff)
            kSpaceImgOutCut = self.MRI.prepareOutput(kSpaceImgCut) # Fourier transform Output with Cutoff
            cv2.imwrite(os.path.join(outCartesianPath,'kSpaceImgCut.jpg'),kSpaceImgOutCut)
            # kSpaceImgOutCut = cv2.imread(outCartesianPath + '/kSpaceImgCut.jpg', 0)
            self.pixmapResultHist = QPixmap(outCartesianPath + '/kSpaceImgCut.jpg')
            self.resultHist.setPixmap(self.pixmapResultHist.scaled(self.resultHist.width(), self.resultHist.height(), QtCore.Qt.KeepAspectRatio))
            self.resultHist.setAlignment(QtCore.Qt.AlignCenter)

            outImgCut = self.MRI.revertDFT(kSpaceImgCut)

            outImgCut = self.MRI.prepareFinalOutput(outImgCut) #
            cv2.imwrite(os.path.join(outCartesianPath,'kSpaceImgCut.jpg'),outImgCut)

            outImgCut = cv2.imread(outCartesianPath + 'kSpaceImgCut.jpg',0)
            plt.clf()
            outHist = self.compute_histogram(outImgCut)
            inHist_fig = plt.plot(outHist)
            plt.savefig(outCartesianPath + '/Output_SI_Graph.png')
            self.pixmapOutSI = QPixmap(outCartesianPath + '/Output_SI_Graph.png')
            self.outImgSI.setPixmap(self.pixmapOutSI.scaled(self.outImgSI.width(), self.outImgSI.height(), QtCore.Qt.KeepAspectRatio))
            self.outImgSI.setAlignment(QtCore.Qt.AlignCenter)

            self.pixmapOut = QPixmap(outCartesianPath + 'kSpaceImgCut.jpg')
            # self.outPic.setScaledContents(True)
            self.outPic.setPixmap(self.pixmapOut.scaled(self.outPic.width(), self.outPic.height(), QtCore.Qt.KeepAspectRatio))
            self.outPic.setAlignment(QtCore.Qt.AlignCenter)

        elif str(self.comboBoxTrajectory.currentText()) == "Radial":
            outRadialPath = path + '/Output/Radial_Output/'
            if not os.path.exists(outRadialPath):
                os.makedirs(outRadialPath)

            kSpaceImgCut = self.MRI.radial(img, cutoff)
            kSpaceImgOutCut = self.MRI.prepareOutput(kSpaceImgCut) # Fourier transform Output with Cutoff
            cv2.imwrite(os.path.join(outRadialPath,'kSpaceImgCut.jpg'),kSpaceImgOutCut)
            # kSpaceImgOutCut = cv2.imread(outRadialPath + '/kSpaceImgCut.jpg', 0)
            self.pixmapResultHist = QPixmap(outRadialPath + '/kSpaceImgCut.jpg')
            self.resultHist.setPixmap(self.pixmapResultHist.scaled(self.resultHist.width(), self.resultHist.height(), QtCore.Qt.KeepAspectRatio))
            self.resultHist.setAlignment(QtCore.Qt.AlignCenter)

            outImgCut = self.MRI.revertDFT(kSpaceImgCut)
            outImgCut = self.MRI.prepareFinalOutput(outImgCut) #
            cv2.imwrite(os.path.join(outRadialPath,'kSpaceImgCut.jpg'),outImgCut)
            outImgCut = cv2.imread(outRadialPath + 'kSpaceImgCut.jpg', 0)
            outHist = self.compute_histogram(outImgCut)
            plt.clf()
            inHist_fig = plt.plot(outHist)
            plt.savefig(outRadialPath + '/Output_SI_Graph.png')
            self.pixmapOutSI = QPixmap(outRadialPath + '/Output_SI_Graph.png')
            self.outImgSI.setPixmap(self.pixmapOutSI.scaled(self.outImgSI.width(), self.outImgSI.height(), QtCore.Qt.KeepAspectRatio))
            self.outImgSI.setAlignment(QtCore.Qt.AlignCenter)

            self.pixmapOut = QPixmap(outRadialPath + 'kSpaceImgCut.jpg')
            # self.outPic.setScaledContents(True)
            self.outPic.setPixmap(self.pixmapOut.scaled(self.outPic.width(), self.outPic.height(), QtCore.Qt.KeepAspectRatio))
            self.outPic.setAlignment(QtCore.Qt.AlignCenter)




if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = Main()
    window.showMaximized()
    appctxt.app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)

