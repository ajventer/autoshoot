
from PyQt5 import QtCore, QtGui, QtWidgets
from poledancer_mainwindow import Ui_MainWindow

class MainwindowEvents(object):
    def __init__(self, app, mainwindow, camera):
        self.app = app
        self.camera = camera
        self.mainwindow = mainwindow
        self.mainwindow.actionQuit.triggered.connect(app.closeAllWindows)
        self.mainwindow.actionCamera.triggered.connect(self.CameraConnect)
        self.mainwindow.StatusBarButton.clicked.connect(self.startSequence)

    def CameraConnect(self):
        self.camera.connect()
        self.mainwindow.StatusBarButton.setEnabled(True)
        self.mainwindow.statusbar.showMessage('Camera connected. Press start to begin')

    def startSequence(self):
        new_image = self.camera.getImage()
        self.mainwindow.starcanvas.updateImage(new_image)


        


