from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from queries import Database
import mysql.connector
from mysql.connector import Error
from config import db_config



class Sales(object):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.old_values = {}
        self.flag = False


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setVerticalSpacing(0)
        self.sales_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.sales_button, 0, 0, 1, 1)
        self.clients_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.clients_button, 1, 0, 1, 1)
        self.products_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.products_button, 2, 0, 1, 1)
        self.categories_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.categories_button, 3, 0, 1, 1)
        self.report_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.report_button, 4, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_10.setContentsMargins(11, 30, 11, 30)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setVerticalSpacing(20)
        self.add_button = QtWidgets.QPushButton(self.frame_4)
        self.gridLayout_5.addWidget(self.add_button, 0, 0, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.frame_4)
        self.gridLayout_5.addWidget(self.delete_button, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(10, 0, 0, 0)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMaximumSize(QtCore.QSize(1412142, 12412412))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_11.setContentsMargins(11, 11, 0, 0)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setMaximumSize(QtCore.QSize(12213, 70))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_9.setHorizontalSpacing(7)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMaximumSize(QtCore.QSize(3000, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_13.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.sort_label = QtWidgets.QLabel(self.frame_7)
        self.gridLayout_6.addWidget(self.sort_label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.comboBox = QtWidgets.QComboBox(self.frame_7)
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.gridLayout_6.addWidget(self.comboBox, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_13.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_7, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.lineEdit = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.gridLayout_12.addWidget(self.lineEdit, 0, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout_14.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_8, 0, 1, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout_7.addWidget(self.frame_5, 0, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_9)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Клиент", "Дата", "Товар", "Количество", "Сумма"])

        self.gridLayout_15.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_9, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.renameUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def renameUi(self, MainWindow):
        MainWindow.setWindowTitle("Магазин")
        self.sales_button.setText("Продажи")
        self.clients_button.setText("Клиенты")
        self.clients_button.clicked.connect(lambda: self.go_to_clients())
        self.products_button.setText("Товары")
        self.products_button.clicked.connect(lambda: self.go_to_products())
        self.categories_button.setText("Категории")
        self.categories_button.clicked.connect(lambda: self.go_to_categories())
        self.report_button.setText("Отчёт")
        self.report_button.clicked.connect(lambda: self.go_to_report())
        self.add_button.setText("Добавить")
        self.add_button.clicked.connect(self.add_sales)
        self.check_clients_and_products()
        self.delete_button.setText("Удалить")
        self.sort_label.setText("Сортировать по")
        self.insert_data()

    def add_sales(self):
        self.flag = True
        self.db.connect()
        clients = self.db.get_id_clients()
        self.db.connect()
        products = self.db.get_id_products()
        client = clients[0]
        product = products[0]
        date = '20.12.2024'
        quantity = 1
        amount = 5000

        row_position = self.tableWidget.rowCount()
        self.old_values[row_position] = {'client': client,
                                         'products':product,
                                         'date': date,
                                         'quantity': quantity,
                                         'amount': amount
                                         }
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(client)))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(date))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(product)))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(quantity)))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(str(amount)))
        self.db.connect()
        row_values = []

        for column in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row_position, column)
            if item is not None:
                row_values.append(item.text())

        self.db.save_to_db_sales(row_values)
        self.flag = False

    def check_clients_and_products(self):
        self.db.connect()
        clients = self.db.get_id_clients()
        self.db.connect()
        products = self.db.get_id_products()

        if clients and products:
            self.add_button.setEnabled(True)
        else:
            self.add_button.setEnabled(False)

    def insert_data(self):

        self.db.connect()
        records = self.db.fetch_all_records('sales')
        if records is not None:
            self.tableWidget.setRowCount(len(records))
            for row_index, row in enumerate(records):
                self.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(row[1])))
                self.tableWidget.setItem(row_index, 1, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(row[3])))
                self.tableWidget.setItem(row_index, 3, QTableWidgetItem(str(row[4])))
                self.tableWidget.setItem(row_index, 4, QTableWidgetItem(str(row[5])))

                self.old_values[row_index] = {
                    'client': row[1],
                    'date': row[2],
                    'product': row[3],
                    'quantity': row[4],
                    'amount': row[5]
                }
        self.tableWidget.itemChanged.connect(self.on_item_changed)

    def on_item_changed(self, item):
        if not self.flag:
            row = item.row()
            column = item.column()
            self.db.connect()
            sales = self.db.fetch_all_records('sales')
            sale_id = sales[row][0]

            if column in [3, 4]:
                new_value = item.text()

                if not self.is_valid_number(new_value):

                    if column == 3:
                        item.setText(str(self.old_values[row]['quantity']))
                    elif column == 4:
                        item.setText(str(self.old_values[row]['amount']))
                else:
                    self.db.connect()
                    if column == 3:
                        if '.' not in new_value:
                            if (int(new_value) % 1 == 0):
                                self.old_values[row]['quantity'] = int(new_value)
                                self.db.update_sales(sale_id, 'quantity', new_value)
                            else:
                                item.setText(str(self.old_values[row]['quantity']))
                        else:
                            item.setText(str(self.old_values[row]['quantity']))

                    elif column == 4:
                        self.old_values[row]['amount'] = float(new_value)
                        self.db.update_sales(sale_id, 'amount', new_value)

            elif column in [0]:
                self.db.connect()
                clients = self.db.get_id_clients()
                new_value = item.text()
                if self.is_valid_number(new_value):
                    if ('.' not in new_value):
                        if int(new_value) not in clients:
                            item.setText(str(self.old_values[row]['client']))
                        else:
                            self.old_values[row]['client'] = int(new_value)
                            self.db.connect()
                            self.db.update_sales(sale_id, 'client', new_value)
                    else:
                        item.setText(str(self.old_values[row]['client']))
                else:
                    item.setText(str(self.old_values[row]['client']))

            elif column in [2]:
                self.db.connect()
                products = self.db.get_id_products()
                new_value = item.text()
                if self.is_valid_number(new_value):
                    if ('.' not in new_value):
                        if int(new_value) not in products:
                            item.setText(str(self.old_values[row]['product']))
                        else:
                            self.old_values[row]['product'] = int(new_value)
                            self.db.connect()
                            self.db.update_sales(sale_id, 'product', new_value)

                    else:
                        item.setText(str(self.old_values[row]['product']))
                else:
                    item.setText(str(self.old_values[row]['product']))

            else:
                self.db.connect()
                new_value = item.text()
                if new_value == '':
                    item.setText(str(self.old_values[row]['date']))
                else:
                    self.old_values[row]['date'] = new_value
                    self.db.update_sales(sale_id, 'date', new_value)

    def is_valid_number(self, value):
        try:
            if value == "":
                return False
            float(value)
            return True
        except ValueError:
            return False
    def go_to_clients(self):
        self.clients_window = Clients(self.db)

    def go_to_products(self):
        self.clients_window = Products(self.db)

    def go_to_categories(self):
        self.clients_window = Categories(self.db)

    def go_to_report(self):
        self.clients_window = Report(self.db)

class Clients(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.old_values = {}
        self.flag = False

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setVerticalSpacing(0)
        self.sales_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.sales_button, 0, 0, 1, 1)
        self.clients_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.clients_button, 1, 0, 1, 1)
        self.products_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.products_button, 2, 0, 1, 1)
        self.categories_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.categories_button, 3, 0, 1, 1)
        self.report_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.report_button, 4, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_10.setContentsMargins(11, 30, 11, 30)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setVerticalSpacing(20)
        self.add_button = QtWidgets.QPushButton(self.frame_4)
        self.gridLayout_5.addWidget(self.add_button, 0, 0, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.frame_4)
        self.gridLayout_5.addWidget(self.delete_button, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(10, 0, 0, 0)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMaximumSize(QtCore.QSize(1412142, 12412412))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_11.setContentsMargins(11, 11, 0, 0)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setMaximumSize(QtCore.QSize(12213, 70))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_9.setHorizontalSpacing(7)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMaximumSize(QtCore.QSize(3000, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_13.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.sort_label = QtWidgets.QLabel(self.frame_7)
        self.gridLayout_6.addWidget(self.sort_label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.comboBox = QtWidgets.QComboBox(self.frame_7)
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.gridLayout_6.addWidget(self.comboBox, 1, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.gridLayout_13.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_7, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.lineEdit = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.gridLayout_12.addWidget(self.lineEdit, 0, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridLayout_14.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_8, 0, 1, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridLayout_7.addWidget(self.frame_5, 0, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_9)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Имя", "Фамилия", "Отчество", "Телефон"])

        self.gridLayout_15.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_9, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.renameUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def renameUi(self, MainWindow):
        MainWindow.setWindowTitle("Магазин")
        self.sales_button.setText("Продажи")
        self.sales_button.clicked.connect(lambda: self.go_to_sales())
        self.clients_button.setText("Клиенты")
        self.products_button.setText("Товары")
        self.products_button.clicked.connect(lambda: self.go_to_products())
        self.categories_button.setText("Категории")
        self.categories_button.clicked.connect(lambda: self.go_to_categories())
        self.report_button.setText("Отчёт")
        self.report_button.clicked.connect(lambda: self.go_to_report())
        self.add_button.setText("Добавить")
        self.add_button.clicked.connect(self.add_client)

        self.delete_button.setText("Удалить")
        self.sort_label.setText("Сортировать по")
        self.insert_data()

    def add_client(self):
        self.flag = True
        name = 'Иван'
        surname = 'Иванов'
        patronymic = 'Иванович'
        phone = '123-123-123'
        row_position = self.tableWidget.rowCount()
        self.old_values[row_position] = {'name': name,
                                         'surname':surname,
                                         'patronymic': patronymic,
                                         'phone': phone
                                         }
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(name))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(surname))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(patronymic))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(phone))
        self.db.connect()
        row_values = []

        for column in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row_position, column)
            if item is not None:
                row_values.append(item.text())

        self.db.save_to_db_clients(row_values)
        self.flag = False


    def on_item_changed(self, item):
        if not self.flag:
            row = item.row()
            column = item.column()
            self.db.connect()
            records = self.db.fetch_all_records('clients')
            client_id = records[row][0]

            new_value = item.text()

            if new_value == '':
                if column == 0:
                    item.setText(str(self.old_values[row]['name']))
                elif column == 1:
                    item.setText(str(self.old_values[row]['surname']))
                elif column == 2:
                    item.setText(str(self.old_values[row]['patronymic']))
                elif column == 3:
                    item.setText(str(self.old_values[row]['phone']))
            else:
                self.db.connect()
                if column == 0:
                    self.old_values[row]['name'] = new_value
                    self.db.update_clients(client_id, 'name', new_value)
                elif column == 1:
                    self.old_values[row]['surname'] = new_value
                    self.db.update_clients(client_id, 'surname', new_value)
                elif column == 2:
                    self.old_values[row]['patronymic'] = new_value
                    self.db.update_clients(client_id, 'patronymic', new_value)
                elif column == 3:
                    self.old_values[row]['phone'] = new_value
                    self.db.update_clients(client_id, 'phone', new_value)


    def insert_data(self):
        self.db.connect()
        records = self.db.fetch_all_records('clients')

        if records is not None:
            self.tableWidget.setRowCount(len(records))
            for row_index, row in enumerate(records):
                self.tableWidget.setItem(row_index, 0, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(row_index, 1, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(row_index, 2, QTableWidgetItem(row[3]))
                self.tableWidget.setItem(row_index, 3, QTableWidgetItem(row[4]))

                self.old_values[row_index] = {
                    'name': row[1],
                    'surname': row[2],
                    'patronymic': row[3],
                    'phone': row[4]
                }
        self.tableWidget.itemChanged.connect(self.on_item_changed)



    def go_to_sales(self):
        self.clients_window = Sales(self.db)

    def go_to_products(self):
        self.clients_window = Products(self.db)

    def go_to_categories(self):
        self.clients_window = Categories(self.db)

    def go_to_report(self):
        self.clients_window = Report(self.db)

class Categories(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.old_values = {}

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setVerticalSpacing(0)
        self.sales_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.sales_button, 0, 0, 1, 1)
        self.clients_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.clients_button, 1, 0, 1, 1)
        self.products_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.products_button, 2, 0, 1, 1)
        self.categories_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.categories_button, 3, 0, 1, 1)
        self.report_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.report_button, 4, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_10.setContentsMargins(11, 30, 11, 30)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setVerticalSpacing(20)
        self.add_button = QtWidgets.QPushButton(self.frame_4)
        self.gridLayout_5.addWidget(self.add_button, 0, 0, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.frame_4)
        self.gridLayout_5.addWidget(self.delete_button, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(10, 0, 0, 0)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMaximumSize(QtCore.QSize(1412142, 12412412))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_11.setContentsMargins(11, 11, 0, 0)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setMaximumSize(QtCore.QSize(12213, 70))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_9.setHorizontalSpacing(7)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMaximumSize(QtCore.QSize(3000, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_13.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.sort_label = QtWidgets.QLabel(self.frame_7)
        self.gridLayout_6.addWidget(self.sort_label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.comboBox = QtWidgets.QComboBox(self.frame_7)
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.gridLayout_6.addWidget(self.comboBox, 1, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.gridLayout_13.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_7, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.lineEdit = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.gridLayout_12.addWidget(self.lineEdit, 0, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridLayout_14.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_8, 0, 1, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridLayout_7.addWidget(self.frame_5, 0, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_9)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Наименование"])

        self.gridLayout_15.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_9, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.renameUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def renameUi(self, MainWindow):
        MainWindow.setWindowTitle("Магазин")
        self.sales_button.setText("Продажи")
        self.sales_button.clicked.connect(lambda: self.go_to_sales())
        self.clients_button.setText("Клиенты")
        self.clients_button.clicked.connect(lambda: self.go_to_clients())
        self.products_button.setText("Товары")
        self.products_button.clicked.connect(lambda: self.go_to_products())
        self.categories_button.setText("Категории")
        self.report_button.setText("Отчёт")
        self.report_button.clicked.connect(lambda: self.go_to_report())
        self.add_button.setText("Добавить")
        self.add_button.clicked.connect(self.add_category)
        self.delete_button.setText("Удалить")
        self.sort_label.setText("Сортировать по")
        self.insert_data()

    def add_category(self):
        category = 'Категория'
        row_position = self.tableWidget.rowCount()
        self.old_values[row_position] = {'name': category}
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(category))
        self.db.connect()
        item = self.tableWidget.item(row_position, 0)
        self.db.save_to_db_categories(item.text())


    def on_item_changed(self, item):
        row = item.row()
        column = item.column()

        new_value = item.text()
        if new_value == '':
            item.setText(str(self.old_values[row]['name']))
        else:
            old_value = self.old_values[row]['name']
            self.old_values[row]['name'] = new_value
            self.db.connect()
            self.db.update_categories(new_value, old_value)



    def insert_data(self):
        self.db.connect()
        records = self.db.fetch_all_records('categories')

        if records is not None:
            self.tableWidget.setRowCount(len(records))
            for row_index, row in enumerate(records):
                self.tableWidget.setItem(row_index, 0, QTableWidgetItem(row[1]))

                self.old_values[row_index] = {
                    'name': row[1],
                }
        self.tableWidget.itemChanged.connect(self.on_item_changed)

    def go_to_sales(self):
        self.clients_window = Sales(self.db)

    def go_to_products(self):
        self.clients_window = Products(self.db)

    def go_to_clients(self):
        self.clients_window = Clients(self.db)

    def go_to_report(self):
        self.clients_window = Report(self.db)

class Products(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.old_values = {}
        self.flag = False

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setVerticalSpacing(0)
        self.sales_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.sales_button, 0, 0, 1, 1)
        self.clients_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.clients_button, 1, 0, 1, 1)
        self.products_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.products_button, 2, 0, 1, 1)
        self.categories_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.categories_button, 3, 0, 1, 1)
        self.report_button = QtWidgets.QPushButton(self.frame_3)
        self.gridLayout_4.addWidget(self.report_button, 4, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_10.setContentsMargins(11, 30, 11, 30)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setVerticalSpacing(20)
        self.add_button = QtWidgets.QPushButton(self.frame_4)
        self.gridLayout_5.addWidget(self.add_button, 0, 0, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.frame_4)
        self.gridLayout_5.addWidget(self.delete_button, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(10, 0, 0, 0)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMaximumSize(QtCore.QSize(1412142, 12412412))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_11.setContentsMargins(11, 11, 0, 0)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setMaximumSize(QtCore.QSize(12213, 70))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_9.setHorizontalSpacing(7)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMaximumSize(QtCore.QSize(3000, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_13.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.sort_label = QtWidgets.QLabel(self.frame_7)
        self.gridLayout_6.addWidget(self.sort_label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.comboBox = QtWidgets.QComboBox(self.frame_7)
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.gridLayout_6.addWidget(self.comboBox, 1, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.gridLayout_13.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_7, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.lineEdit = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.gridLayout_12.addWidget(self.lineEdit, 0, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridLayout_14.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_8, 0, 1, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridLayout_7.addWidget(self.frame_5, 0, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_9)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Категория", "Наименование", "Цена", "Кол-во на складе"])

        self.gridLayout_15.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_9, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.renameUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def renameUi(self, MainWindow):
        MainWindow.setWindowTitle("Магазин")
        self.sales_button.setText("Продажи")
        self.sales_button.clicked.connect(lambda: self.go_to_sales())
        self.clients_button.setText("Клиенты")
        self.clients_button.clicked.connect(lambda: self.go_to_clients())
        self.products_button.setText("Товары")
        self.categories_button.setText("Категории")
        self.categories_button.clicked.connect(lambda: self.go_to_categories())
        self.report_button.setText("Отчёт")
        self.report_button.clicked.connect(lambda: self.go_to_report())
        self.add_button.setText("Добавить")
        self.add_button.clicked.connect(self.add_product)
        self.check_categories()
        self.delete_button.setText("Удалить")
        self.sort_label.setText("Сортировать по")
        self.insert_data()

    def add_product(self):
        self.flag = True
        self.db.connect()
        categories = self.db.get_categories()
        category = categories[0]
        name = 'Наименование'
        price = 2999
        quantity = 1
        row_position = self.tableWidget.rowCount()
        self.old_values[row_position] = {'category': category,
                                         'surname': name,
                                         'patronymic': price,
                                         'phone': quantity
                                         }
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(category))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(name))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(price)))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(str(quantity)))
        self.db.connect()

        row_values = []

        item_c = self.tableWidget.item(row_position, 0)

        id_cat = self.db.get_id_by_name(item_c.text())
        self.db.connect()
        row_values.append(id_cat)
        row_values.append((self.tableWidget.item(row_position, 1).text()))
        row_values.append((self.tableWidget.item(row_position, 2).text()))
        row_values.append((self.tableWidget.item(row_position, 3).text()))
        self.db.save_to_db_products(row_values)
        self.flag = False

    def check_categories(self):
        self.db.connect()
        categories = self.db.get_categories()

        if categories:
            self.add_button.setEnabled(True)
        else:
            self.add_button.setEnabled(False)
    def insert_data(self):
        self.db.connect()
        records = self.db.fetch_records_from_products()
        if records is not None:
            self.tableWidget.setRowCount(len(records))
            for row_index, row in enumerate(records):
                self.tableWidget.setItem(row_index, 0, QTableWidgetItem(row[0]))
                self.tableWidget.setItem(row_index, 1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(row[2])))
                self.tableWidget.setItem(row_index, 3, QTableWidgetItem(str(row[3])))

                self.old_values[row_index] = {
                    'category': row[0],
                    'name': row[1],
                    'price': row[2],
                    'quantity': row[3]
                }
        self.tableWidget.itemChanged.connect(self.on_item_changed)

    def on_item_changed(self, item):
        if not self.flag:
            row = item.row()
            column = item.column()
            self.db.connect()
            records = self.db.fetch_all_records('products')
            product_id = records[row][0]

            if column in [2, 3]:
                new_value = item.text()

                if not self.is_valid_number(new_value):

                    if column == 2:
                        item.setText(str(self.old_values[row]['price']))
                    elif column == 3:
                        item.setText(str(self.old_values[row]['quantity']))
                else:
                    self.db.connect()
                    if column == 2:
                        self.old_values[row]['price'] = float(new_value)
                        self.db.update_products(product_id, 'price', new_value)
                    elif column == 3:
                        if '.' not in new_value:
                            if (int(new_value) % 1 == 0):
                                self.old_values[row]['quantity'] = int(new_value)
                                self.db.update_products(product_id, 'quantity', new_value)
                            else:
                                item.setText(str(self.old_values[row]['quantity']))
                        else:
                            item.setText(str(self.old_values[row]['quantity']))

            elif column in [0]:
                self.db.connect()
                categories = self.db.get_categories()
                new_value = item.text()
                if new_value == '' or new_value not in categories:
                    item.setText(str(self.old_values[row]['category']))
                else:
                    self.old_values[row]['category'] = new_value
                    self.db.connect()
                    id_cat = self.db.get_id_by_name(new_value)
                    self.db.connect()
                    self.db.update_products(product_id, 'category', id_cat)


            else:
                self.db.connect()
                new_value = item.text()
                if new_value == '':
                    item.setText(str(self.old_values[row]['name']))
                else:
                    self.old_values[row]['name'] = new_value
                    self.db.update_products(product_id, 'name_prod', new_value)

    def is_valid_number(self, value):
        try:
            if value == "":
                return False
            float(value)
            return True
        except ValueError:
            return False

    def go_to_sales(self):
        self.clients_window = Sales(self.db)

    def go_to_clients(self):
        self.clients_window = Clients(self.db)

    def go_to_categories(self):
        self.clients_window = Categories(self.db)

    def go_to_report(self):
        self.clients_window = Report(self.db)

class Report(object):
    def __init__(self, db):
        super().__init__()
        self.db = db


        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.sales_button = QtWidgets.QPushButton(self.frame_3)
        self.sales_button.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.sales_button, 0, 0, 1, 1)
        self.clients_button = QtWidgets.QPushButton(self.frame_3)
        self.clients_button.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.clients_button, 1, 0, 1, 1)
        self.products_button = QtWidgets.QPushButton(self.frame_3)
        self.products_button.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.products_button, 2, 0, 1, 1)
        self.categories_button = QtWidgets.QPushButton(self.frame_3)
        self.categories_button.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.categories_button, 3, 0, 1, 1)
        self.report_button = QtWidgets.QPushButton(self.frame_3)
        self.report_button.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.report_button, 4, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_10.setContentsMargins(11, 30, 11, 30)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setVerticalSpacing(20)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.form_button = QtWidgets.QPushButton(self.frame_4)
        self.form_button.setObjectName("pushButton_7")
        self.gridLayout_5.addWidget(self.form_button, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMaximumSize(QtCore.QSize(1412142, 12412412))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_11.setContentsMargins(11, 11, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setMaximumSize(QtCore.QSize(12213, 70))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_9.setHorizontalSpacing(7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_7.addWidget(self.frame_5, 1, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.textEdit = QtWidgets.QTextEdit(self.frame_9)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_15.addWidget(self.textEdit, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_9, 2, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_6)
        self.dateEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_7.addWidget(self.dateEdit, 0, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.renameUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def renameUi(self, MainWindow):
        self.form_button.setText("Сформировать отчёт")
        MainWindow.setWindowTitle("Магазин")
        self.sales_button.setText("Продажи")
        self.sales_button.clicked.connect(lambda: self.go_to_sales())
        self.clients_button.setText("Клиенты")
        self.clients_button.clicked.connect(lambda: self.go_to_clients())
        self.products_button.setText("Товары")
        self.products_button.clicked.connect(lambda: self.go_to_products())
        self.categories_button.setText("Категории")
        self.categories_button.clicked.connect(lambda: self.go_to_categories())
        self.report_button.setText("Отчёт")


    def go_to_clients(self):
        self.clients_window = Clients(self.db)

    def go_to_products(self):
        self.clients_window = Products(self.db)

    def go_to_categories(self):
        self.clients_window = Categories(self.db)

    def go_to_sales(self):
        self.clients_window = Sales(self.db)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    db = Database()

    MainWindow = QtWidgets.QMainWindow()
    MainWindow.resize(1152, 864)
    ui = Sales(db)
    MainWindow.show()

    sys.exit(app.exec_())

