# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/CustomerDetailsScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from MainScreen import MainScreen
from PaymentScreen import PaymentScreen
from PaymentScreenCard import PaymentScreenCard
from DatetimeLabel import *
from TSO_State import TSO_State


class CustomerDetailsScreen(QtWidgets.QMainWindow):
    def __init__(self, state, data=None):
        super(CustomerDetailsScreen, self).__init__()
        self.setupUi()
        self.state = state
        self.data = data

        self._dictButtons = {
            self.pushButton: ('mainScreen', MainScreen),
            'mainScreen': ('mainScreen', MainScreen),
            self.pushButton_2: (('paymentScreen', PaymentScreen),
                                ('paymentScreenCard', PaymentScreenCard))
        }

        self.init_timer()

        self.pushButton.clicked.connect(self.showScreen)
        self.pushButton_2.clicked.connect(self.showScreen)

        print(self.data)

    def init_timer(self):
        self.delay_timer = QtCore.QTimer()
        self.delay_timer.timeout.connect(self.showScreen)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timedelay)
        self.decrease = 0
        set_current_time(self.label_6, self.decrease)
        self.delay_timer.start(TIMER_DELAY * 1000)
        self.timer.start(1 * 1000)

    def update_timedelay(self):
        self.decrease += 1
        set_current_time(self.label_6, self.decrease)

    def update_data(self):
        customer_details = {
            'telephone': self.lineEdit.text(),
            'email': self.lineEdit_2.text()
        }
        self.data['customerDetails'] = customer_details

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 598)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("CustomerDetailsScreen", "CustomerDetailsScreen"))
        self.label_5.setText(_translate("MainWindow", "?????????????? ?? ?????????????? ???????? ??????????:"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "?????? ?????????????????? ?????????????????????? ?????????? ???????? ??????????????:"))
        self.label_3.setText(_translate("MainWindow", "??/??????"))
        self.label_2.setText(_translate("MainWindow", "?????????? ???????????????????? ????????????????"))
        self.label_4.setText(_translate("MainWindow", "?????????? ?????????????????????? ??????????"))
        self.pushButton.setText(_translate("MainWindow", "??????????"))
        self.pushButton_2.setText(_translate("MainWindow", "????????????????????"))

    def stop_timer(self):
        self.delay_timer.stop()
        self.timer.stop()

    def showScreen(self):
        self.stop_timer()

        sender = self.sender()
        if sender == self.delay_timer:
            screen_name, screen_class = self._dictButtons['mainScreen']
        elif sender == self.pushButton:
            screen_name, screen_class = self._dictButtons[sender]
        elif sender == self.pushButton_2:
            if self.data['payType'] == 'CASH':
                screen_name, screen_class = self._dictButtons[sender][0]
            elif self.data['payType'] in ['CARD', 'PCARD']:
                screen_name, screen_class = self._dictButtons[sender][1]

            self.update_data()

        setattr(self, screen_name, screen_class(self.state, self.data))
        _screen = getattr(self, screen_name, None)
        _screen.show()
        self.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    state = TSO_State(currencydetector=False)
    ui = CustomerDetailsScreen(state)
    ui.show()
    sys.exit(app.exec_())
