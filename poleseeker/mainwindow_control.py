from PyQt5 import QtCore, QtGui, QtWidgets
from poleseeker_mainwindow import Ui_MainWindow

class PoleSeekerMainWindow(Ui_MainWindow):
    '''
    All UI code not done via QT-Designer,
    thus allowing it to not be overridden when the QTDesigner code 
    is changed.
    '''
    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        MainWindow.showMaximized()
        self.statusbar.showMessage('Click the start button to begin alignment')
        self.StatusBarButton = QtWidgets.QPushButton(self.centralwidget)
        #self.StatusBarButton.setGeometry(QtCore.QRect(290, 300, 112, 31))
        self.StatusBarButton.setObjectName("pushButton")
        self.StatusBarButton.setText ('Start')

        self.statusbar.addPermanentWidget(self.StatusBarButton)
