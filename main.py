from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pic

#first_Dialog
class first_Dialog(QMainWindow):
    def __init__(self):
        super(first_Dialog,self).__init__()
        loadUi(r"first_Dialog1.ui",self)
        self.pushButton.clicked.connect(self.nextpage)
        self.pushButton_1.clicked.connect(self.check_password)
        # self.pushButton_1.clicked.connect(self.page3)
    
    def check_password(self):
        msg = QMessageBox()
        if self.lineEdit_1.text() == 'Karthikeyan' and self.lineEdit_2.text() == '9751':
            msg.buttonClicked.connect(self.page3)
            msg.setText('Success')
            msg.exec_()
        elif self.lineEdit_1.text() == 'Arun' and self.lineEdit_2.text() == '1234':
            page5_=home_page()
            msg.buttonClicked.connect(page5_.page5)
            msg.setText('Success')
            msg.exec_()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()

    def nextpage(self):
        nextpage=second_Dialog()
        widget.addWidget(nextpage)
        widget.setCurrentIndex(widget.currentIndex()+1)
       
    def page3(self):
        page3=home_page()
        widget.addWidget(page3)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    
class second_Dialog(QDialog):
    def __init__(self):
        super(second_Dialog,self).__init__()
        loadUi(r"second_Dialog.ui",self)
        self.pushButton2_1.clicked.connect(self.backfunction)

    def backfunction(self):
        msg = QMessageBox()
        msg.setText('Success signup')
        msg.exec_()
        backpage=first_Dialog()
        widget.addWidget(backpage)
        widget.setCurrentIndex(widget.currentIndex()+1)


class home_page(QMainWindow):
    def __init__(self):
        super(home_page,self).__init__()
        loadUi(r"home_page1.ui",self)
        self.pushButton_2.clicked.connect(self.page4)
        self.pushButton3_1.clicked.connect(self.page5)

    def page4(self):
        app.quit()
        print("Exit")
    

    def page5(self):
        page5=VideoWindow()
        widget.addWidget(page5)
        widget.setCurrentIndex(widget.currentIndex()+1)

class VideoWindow(QMainWindow):

    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)
        self.setWindowTitle("BOTTLE DEFECTS INSPECTION SYSTEM") 
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        # Create new action
        openAction = QAction(QIcon('open.png'), '&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open movie')
        openAction.triggered.connect(self.openFile)

        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        #fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        # Set widget to contain window contents
        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

    def openFile(self):
        #fileName, _ = QFileDialog.getOpenFileName(self, "Open files",QDir.homePath())
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open file','/home/', ("Images (*.png *.tiff *.jpg *.py *.pdf *.doc)"))
                
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def exitCall(self):
        exitCall=home_page()
        widget.addWidget(exitCall)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())




app=QApplication(sys.argv)
mainwindow=first_Dialog()
secondpage=second_Dialog()
thirdpage=home_page()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
#widget.addWidget(secondpage)
#widget.addWidget(thirdpage)
# widget.SetFixedWidth(800)
widget.setFixedWidth(950)
widget.setFixedHeight(480)
# widget.setFixedHeight(580)
widget.show()
app.exec_()
