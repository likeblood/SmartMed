import pickle
import pandas as pd

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QWidget, QToolTip, QPushButton, QApplication, QMessageBox)

from .DownloadWindow import DownloadWindow
from ..Notification import NotificationWindow
from PyQt5.QtCore import Qt
from ..utils import get_columns



class WrappedDownloadWindow(DownloadWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__build_buttons()
        self.setWindowTitle('Что-то там 2')
        self.columns =''

    def __build_buttons(self):
        #плохо с неймингом, надо переделать бек некст
        self.pushButtonBack.clicked.connect(self.back
            )
        self.pushButtonNext.clicked.connect(self.next)
        self.pushButton.clicked.connect(self.path_to_file)
    def back(self):
        self.hide()
        self.parent.show()

    def next(self):
        
        self.hide()
        self.child.show()

    def path_to_file(self):
        w = QWidget()
        def callback():
            pass
        NotificationWindow.info(
            'Warning', 'Calculus, originally called infinitesimal calculus or "the calculus of infinitesimals", is the mathematical study of continuous change', callback=callback)
        w.show()

        #path = QtWidgets.QFileDialog.getOpenFileName()[0]
        #col = get_columns(path).columns
        #print(list(col))
        #self.comboBox.addItems(col)