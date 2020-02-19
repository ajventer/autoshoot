from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class starCanvas(QLabel):
    def __init__(self, mainwindow):
        QLabel.__init__(self)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.mainwindow = mainwindow
        self.pixmap = QPixmap("Resources/icon.png")
        self.setPixmap(self.pixmap)
        self.installEventFilter(self)
        self.setMouseTracking(True)
        self.Clicked = None
        self.previous = None
        self.drift = None
        self.stage = 1


    def eventFilter(self, source, event):
        if (source is self and event.type() == QEvent.Resize):
            self.setPixmap(self.pixmap.scaled(self.size(), Qt.KeepAspectRatio))
        elif (source is self and event.type() == QEvent.MouseButtonRelease):
            self.handleClick(event.pos())
        return self.mainwindow.eventFilter(source, event)

    def updateImage(self, image):
        self.pixmap = QPixmap.fromImage(image)
        self.setPixmap(self.pixmap.scaled(self.size(), Qt.KeepAspectRatio))
        self.update()


    def paintEvent(self, QPaintEvent):
        super(starCanvas, self).paintEvent(QPaintEvent)
        print (self.Clicked)
        if self.Clicked and not self.stage == 4:            
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red))
            painter.drawLine(self.Clicked.x(),0,self.Clicked.x(),self.height())
            painter.drawLine(0,self.Clicked.y(),self.width(),self.Clicked.y())
        if self.stage == 4:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red))
            painter.drawLine(self.previous.x(),self.previous.y(),self.Clicked.x(),self.previous.y())
            painter.setPen(QPen(Qt.blue))
            painter.drawLine(self.Clicked.x(),self.previous.y(),self.Clicked.x(),self.Clicked.y())


    def drift_str(self):
        return 'Azimuth drift: '+str(self.drift[0])+' / Altitude drift:  '+str(self.drift[1])


    def calculate_drift(self):
        print (self.Clicked, self.previous)
        drift_az = self.Clicked.x() - self.previous.x()
        drift_alt = self.Clicked.y() - self.previous.y()
        self.drift = (drift_az, drift_alt)

    def handleClick(self, pos):
        self.Clicked = pos
        self.update()
