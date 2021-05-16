# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from InfoScreen import InfoScreen
from ScanScreen import ScanScreen_
from InformationScreen import InformationScreen
from DatetimeLabel import *
from TSO_State import TSO_State

ONLINE = True
BANK_ONLINE = True
PETROL_ONLINE = True

MAXIMUM_AMOUNT = 15_000


class MainScreen(QtWidgets.QMainWindow):
    def __init__(self, state, data=None):
        super(MainScreen, self).__init__()
        self.setupUi()
        self.state = state
        self.choice_of_inscription()
        self.data = {}

        self._dictButtons = {
            self.pushButton: ('infoScreen', InfoScreen),
            self.pushButton_2: ('scanScreen', ScanScreen_),
            self.pushButton_3: ('informationScreen', InformationScreen)
        }

        set_current_datetime(self.label_5)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_datetime)
        time_delay = time_before_signal()
        self.timer.start(int(time_delay[0] * 1000 + time_delay[1] / 1000))

        self.pushButton.clicked.connect(self.showScreen)
        self.pushButton_2.clicked.connect(self.showScreen)
        self.pushButton_3.clicked.connect(self.showScreen)

    def update_datetime(self):
        # print('here')
        set_current_datetime(self.label_5)
        self.timer.stop()
        self.timer.start(60 * 1000)

    def update_data(self):
        self.data['inscription_num'] = 0

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def choice_of_inscription(self):
        inscription_list = ["В настоящее время оплата топливной картой недоступна",
                           "В настоящее время оплата банковской картой недоступна",
                           "В настоящее время оплата доступна только наличными",
                           "В настоящее время оплата наличными недоступна",
                           "В настоящее время оплата доступна только банковской картой",
                           "В настоящее время оплата доступна только топливной картой",
                           "В настоящее время заправка не осуществляется"]

        if ONLINE:
            if self.state.PAPER and self.state.INK:
                if self.state.CURRENCYDETECTOR:
                    if self.state.POS:
                        if BANK_ONLINE:
                            if PETROL_ONLINE:
                                inscription = None
                            else:
                                inscription = inscription_list[0]
                        else:
                            if PETROL_ONLINE:
                                inscription = inscription_list[1]
                            else:
                                inscription = inscription_list[2]
                    else:
                        inscription = inscription_list[2]
                else:
                    if self.state.POS:
                        if BANK_ONLINE:
                            if PETROL_ONLINE:
                                inscription = inscription_list[3]
                            else:
                                inscription = inscription_list[4]
                        else:
                            if PETROL_ONLINE:
                                inscription = inscription_list[5]
                            else:
                                inscription = inscription_list[6]
                    else:
                        inscription = inscription_list[6]
            else:
                inscription = inscription_list[6]
        else:
            inscription = inscription_list[6]
        if inscription is None:
            self.verticalLayout.removeWidget(self.label)
            self.label.hide()
        else:
            self.label.setText(inscription)
        if inscription == inscription_list[6]:
            self.verticalLayout.removeWidget(self.pushButton)
            self.verticalLayout.removeWidget(self.pushButton_2)
            self.verticalLayout.removeWidget(self.pushButton_3)
            self.pushButton.hide()
            self.pushButton_2.hide()
            self.pushButton_3.hide()
        print(inscription)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainScreen", "MainScreen"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "Заправка"))
        self.pushButton_2.setText(_translate("MainWindow", "Печать чека\nПеревод сдачи"))
        self.pushButton_3.setText(_translate("MainWindow", "Информация"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))

    def showScreen(self):
        sender = self.sender()
        screen_name, screen_class = self._dictButtons[self.sender()]
        if sender == self.pushButton:
            self.update_data()
            setattr(self, screen_name, screen_class(self.state, self.data))
        else:
            setattr(self, screen_name, screen_class(self.state))
        _screen = getattr(self, screen_name, None)
        _screen.show()
        self.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    state = TSO_State(currencydetector=False)
    ui = MainScreen(state)
    ui.show()
    sys.exit(app.exec_())
