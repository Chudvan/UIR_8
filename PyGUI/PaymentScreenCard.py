# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/PaymentScreenCard.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from MainScreen import MainScreen, MAXIMUM_AMOUNT
from InfoScreen import InfoScreen
from DatetimeLabel import *
from TSO_State import TSO_State


class PaymentScreenCard(QtWidgets.QMainWindow):
    def __init__(self, state, data = None):
        super(PaymentScreenCard, self).__init__()
        self.state = state
        self.data = data
        self._sum = 0
        self.liters = 0
        self.maximum_amount = MAXIMUM_AMOUNT
        self.setupUi()

        self._dictButtons = {
            self.pushButton: ('mainScreen', MainScreen),
            'mainScreen': ('mainScreen', MainScreen),
            self.pushButton_2: ('infoScreen', InfoScreen)
        }

        self.init_timer()

        self.pushButton.clicked.connect(self.showScreen)
        self.pushButton_2.clicked.connect(self.showScreen)
        self.doubleSpinBox.valueChanged.connect(self.update_spin_boxes)
        self.doubleSpinBox_2.valueChanged.connect(self.update_spin_boxes)

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
        self.data['volume'] = int(self.get_liters() * 100) / 100
        self.data['amount'] = self.get_sum()
        self.data['inscription_num'] = 1
        self.data['dateTime'] = get_datetime('YYYY-MM-DDTHH:MM')

    def set_liters(self, value):
        self.liters = value
        if self.get_liters() != self.liters:
            self.doubleSpinBox_2.setValue(value)

    def get_liters(self):
        return self.doubleSpinBox_2.value()

    def set_sum(self, value):
        if value > self.maximum_amount:
            return
        self._sum = value
        if self.get_sum() != self._sum:
            self.doubleSpinBox.setValue(value)

    def get_sum(self):
        return self.doubleSpinBox.value()

    def update_spin_boxes(self):
        sender = self.sender()
        if sender == self.doubleSpinBox:
            print('sum')
            self.set_sum(self.get_sum())
            if self.data:
                self.set_liters(self.get_sum() / self.data['petrol']['price'])
        elif sender == self.doubleSpinBox_2:
            print('litres')
            current_litres = self.liters
            self.set_liters(self.get_liters())
            if self.data:
                if self.get_liters() * self.data['petrol']['price'] <= self.maximum_amount:
                    self.set_sum(self.get_liters() * self.data['petrol']['price'])
                else:
                    self.set_liters(current_litres)
        print(self._sum)
        print(self.liters)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(861, 530)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
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
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setMaximum(self.maximum_amount)
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_2.setMaximum(self.maximum_amount)
        self.gridLayout.addWidget(self.doubleSpinBox_2, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setText("")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_4.addWidget(self.label_17)
        self.gridLayout_5.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PaymentScreenCard", "PaymentScreenCard"))
        self.label_5.setText(_translate("MainWindow", "Возврат в главное меню через:"))
        self.label_6.setText(_translate("MainWindow", "TextLabel6"))
        self.label.setText(_translate("MainWindow", "Введите сумму к оплате или количество литров"))
        self.label_7.setText(_translate("MainWindow", "Ввести рубли:"))
        self.label_16.setText(_translate("MainWindow", "Л."))
        self.label_8.setText(_translate("MainWindow", "Руб."))
        self.label_14.setText(_translate("MainWindow", "Ввести литры:"))
        if self.data:
            self.label_2.setText(_translate("MainWindow",
                                            str(self.data['pump']['number']) + ' : ' + self.data['pump']['status']))
            self.label_3.setText(_translate("MainWindow",
                                            self.data['petrol']['petrolType'] + ' : ' + str(self.data['petrol']['price'])))
        self.label_18.setText(_translate("MainWindow", "Максимальная сумма заказа"))
        self.label_19.setText(_translate("MainWindow", "За данную операцию комиссия не взимается!"))
        self.pushButton.setText(_translate("MainWindow", "Выход"))
        self.pushButton_2.setText(_translate("MainWindow", "Оплатить"))

        self.doubleSpinBox.setValue(self._sum)
        self.doubleSpinBox_2.setValue(self.liters)
        self.lineEdit.setText(str(self.maximum_amount))

    def stop_timer(self):
        self.delay_timer.stop()
        self.timer.stop()

    def showScreen(self):
        self.stop_timer()

        sender = self.sender()
        if sender == self.delay_timer or sender == self.pushButton:
            screen_name, screen_class = self._dictButtons['mainScreen']
        else:
            screen_name, screen_class = self._dictButtons[sender]

            self.update_data()
        setattr(self, screen_name, screen_class(self.state, self.data))
        _screen = getattr(self, screen_name, None)
        _screen.show()
        self.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    state = TSO_State(currencydetector=False)
    ui = PaymentScreenCard(state)
    ui.show()
    sys.exit(app.exec_())
