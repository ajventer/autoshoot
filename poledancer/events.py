
from PyQt5 import QtCore, QtGui, QtWidgets
from poledancer_mainwindow import Ui_MainWindow

class MainwindowEvents(object):
    def __init__(self, app, mainwindow):
        self.app = app
        self.mainwindow = mainwindow
        self.mainwindow.actionQuit.triggered.connect(app.closeAllWindows)
        


