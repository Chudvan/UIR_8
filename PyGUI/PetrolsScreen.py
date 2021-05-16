# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/PetrolsScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from MainScreen import MainScreen
from PaymentMethodScreen import PaymentMethodScreen
from DatetimeLabel import *
from TSO_State import TSO_State
import requests


class Logic(QObject):
    new_screen = pyqtSignal(object)

    def __init__(self):
        super(Logic, self).__init__()
        self.actual = True

    def run(self):
        try:
            r = requests.get('http://127.0.0.1:8000/api/v1/TSO/session/')
        except requests.exceptions.ConnectionError:
            print('ERROR')
            return
        # print(r)

        if self.actual:
            #print(self.data)
            self.new_screen.emit(r.status_code)
        self.thread().quit()


class PetrolsScreen(QtWidgets.QMainWindow):
    def __init__(self, state, data=None):
        from ErrorScreen import ErrorScreen
        super(PetrolsScreen, self).__init__()
        self.state = state
        self.data = data
        self.setupUi()

        self._dictButtons = {
            self.pushButton: ('mainScreen', MainScreen),
            'mainScreen': ('mainScreen', MainScreen),
            'petrols': ('paymentMethodScreen', PaymentMethodScreen),
            'errorScreen': ('errorScreen', ErrorScreen)
        }

        self.init_timer()
        self.init_logic()

        self.pushButton.clicked.connect(self.showScreen)

        n = len(self.data['petrol']) if self.data['petrol'] else 0
        for i in range(n):
            pushButton_name = "pushButton_" + str(i + 2)
            pushButton = getattr(self, pushButton_name, None)
            pushButton.clicked.connect(self.start_logic)

        # self.pushButton_2.clicked.connect(self.showScreen)
        # self.pushButton_3.clicked.connect(self.showScreen)
        # self.pushButton_4.clicked.connect(self.showScreen)
        # self.pushButton_5.clicked.connect(self.showScreen)

        #print(self.data)

    def init_logic(self):
        self.thread = QtCore.QThread(self)
        self.logic = Logic()
        self.logic.moveToThread(self.thread)
        self.logic.new_screen.connect(self.showScreen)
        self.thread.started.connect(self.logic.run)

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

    def update_data(self, button):
        petrol = {
            'petrolType': button.petrolType,
            'price': button.price
        }
        self.data['petrol'] = petrol

    def create_buttons(self):
        n = len(self.data['petrol']) if self.data['petrol'] else 0
        for i in range(n):
            pushButton_name = "pushButton_" + str(i + 2)
            setattr(self, pushButton_name, QtWidgets.QPushButton(self.centralwidget))
            pushButton = getattr(self, pushButton_name, None)
            self.gridLayout.addWidget(pushButton, i // 4, i % 4, 1, 1)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
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
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.create_buttons()

        # self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        # self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_4.setObjectName("pushButton_4")
        # self.gridLayout.addWidget(self.pushButton_4, 0, 2, 1, 1)
        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        # self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_5.setObjectName("pushButton_5")
        # self.gridLayout.addWidget(self.pushButton_5, 0, 3, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_buttons(self):
        n = len(self.data['petrol']) if self.data['petrol'] else 0
        for i in range(n):
            pushButton_name = "pushButton_" + str(i + 2)
            pushButton = getattr(self, pushButton_name, None)
            pushButton.setText(self.data['petrol'][i]['petrolType'] + ' : ' + str(self.data['petrol'][i]['price']))
            pushButton.petrolType = self.data['petrol'][i]['petrolType']
            pushButton.price = self.data['petrol'][i]['price']

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PetrolsScreen", "PetrolsScreen"))
        self.label_5.setText(_translate("MainWindow", "Возврат в главное меню через:"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "Выберите пистолет на ТРК №" + str(self.state.TSO_number)))

        self.retranslate_buttons()

        # self.pushButton_3.setText(_translate("MainWindow", "PushButton3"))
        # self.pushButton_4.setText(_translate("MainWindow", "PushButton4"))
        # self.pushButton_2.setText(_translate("MainWindow", "PushButton2"))
        # self.pushButton_5.setText(_translate("MainWindow", "PushButton5"))

        self.pushButton.setText(_translate("MainWindow", "Выход"))

    def start_logic(self):
        sender = self.sender()
        self.update_data(sender)

        self.thread.start()

    def stop_timer(self):
        self.delay_timer.stop()
        self.timer.stop()

    def terminate_logic(self):
        self.logic.actual = False
        if self.thread.isRunning():
            print('if')
            self.thread.quit()
            self.thread.wait()
            self.thread.terminate()
            self.thread.wait()
        print(self.thread.isFinished(), self.thread.isRunning())

    def showScreen(self, status_code=None):
        self.stop_timer()
        self.terminate_logic()

        sender = self.sender()

        if sender == self.delay_timer:
            screen_name, screen_class = self._dictButtons['mainScreen']
            #self.logic.actual = False
        elif sender == self.pushButton:
            screen_name, screen_class = self._dictButtons[sender]
            #self.logic.actual = False
        elif status_code == 200:
            screen_name, screen_class = self._dictButtons['petrols']
        elif status_code == 503:
            screen_name, screen_class = self._dictButtons['errorScreen']
        else:
            raise Exception
        print(self.data)

        setattr(self, screen_name, screen_class(self.state, self.data))
        _screen = getattr(self, screen_name, None)
        _screen.show()
        self.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    state = TSO_State(currencydetector=False)
    ui = PetrolsScreen(state)
    ui.show()
    sys.exit(app.exec_())
