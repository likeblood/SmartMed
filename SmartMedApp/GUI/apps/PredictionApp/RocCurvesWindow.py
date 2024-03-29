# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RocCurvesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class RocCurvesWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 60, 421, 61))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 160, 331, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxAuc = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxAuc.setObjectName("checkBoxAuc")
        self.verticalLayout.addWidget(self.checkBoxAuc)
        self.checkBoxDiff = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxDiff.setObjectName("checkBoxDiff")
        self.verticalLayout.addWidget(self.checkBoxDiff)
        self.checkBoxPaint = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxPaint.setObjectName("checkBoxPaint")
        self.verticalLayout.addWidget(self.checkBoxPaint)
        self.pushButtonNext = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNext.setGeometry(QtCore.QRect(460, 420, 113, 32))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(330, 420, 113, 32))
        self.pushButtonBack.setObjectName("pushButtonBack")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Выбор параметров отображения ROC кривых</span></p></body></html>"))
        self.checkBoxAuc.setText(_translate("MainWindow", "ROC AUC"))
        self.checkBoxDiff.setText(_translate("MainWindow", "Построить кривые на отдельных графиках"))
        self.checkBoxPaint.setText(_translate("MainWindow", "Закрасить площадь под графиком"))
        self.pushButtonNext.setText(_translate("MainWindow", "Вперед"))
        self.pushButtonBack.setText(_translate("MainWindow", "Назад"))
