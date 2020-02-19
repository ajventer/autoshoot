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
        self.lastClicked = None


    def eventFilter(self, source, event):
        if (source is self and event.type() == QEvent.Resize):
            self.setPixmap(self.pixmap.scaled(self.size(), Qt.KeepAspectRatio))
        elif (source is self and event.type() == QEvent.MouseButtonRelease):
            self.handleClick(event.pos())
        return self.mainwindow.eventFilter(source, event)

    def updateImage(self, image):
        self.pixmap = QPixmap(image)
        self.setPixmap(self.pixmap)
        self.update()


    def paintEvent(self, QPaintEvent):
        super(starCanvas, self).paintEvent(QPaintEvent)
        print (self.lastClicked)
        if self.lastClicked:            
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red))
            painter.drawLine(self.lastClicked.x(),0,self.lastClicked.x(),self.height())
            painter.drawLine(0,self.lastClicked.y(),self.width(),self.lastClicked.y())


    def handleClick(self, pos):
        print (pos)
        self.lastClicked = pos
        self.update()
