# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraphsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class GraphsWindowCross(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 461, 51))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 130, 510, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxLogAllinGroup = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxLogAllinGroup.setObjectName("checkBoxLogAllinGroup")
        self.verticalLayout.addWidget(self.checkBoxLogAllinGroup)
        self.checkBoxAllinGroup = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxAllinGroup.setObjectName("checkBoxAllinGroup")
        self.verticalLayout.addWidget(self.checkBoxAllinGroup)
        self.checkBoxForEachGroup = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxForEachGroup.setObjectName("checkBoxForEachGroup")
        self.verticalLayout.addWidget(self.checkBoxForEachGroup)
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
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt;\">Выберите графики для визуализации</span></p></body></html>"))
        self.checkBoxLogAllinGroup.setText(_translate("MainWindow", "  Индивидуальные графики для пациентов \n"
"  c концентрациями обоих препаратов"))
        self.checkBoxAllinGroup.setText(_translate("MainWindow", "  Графики со средними концентрациями \n"
"  препаратов по группам"))
        self.checkBoxForEachGroup.setText(_translate("MainWindow", "  График, где данные обобщены \n"
"  по двум препаратам"))
        self.pushButtonNext.setText(_translate("MainWindow", "Завершить"))
        self.pushButtonBack.setText(_translate("MainWindow", "Назад"))

