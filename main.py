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
        self.delete_button.setText("Удалить")
        self.sort_label.setText("Сортировать по")
        self.insert_data()

    def insert_data(self):
        self.db.connect()
        records = self.db.fetch_all_records('sales')

        if records is not None:
            self.tableWidget.setRowCount(len(records))
            for row_idx, row_data in enumerate(records):
                for col_idx, col_data in enumerate(row_data[1:]):
                    item = QtWidgets.QTableWidgetItem(str(col_data))
                    print(item.text())
                    self.tableWidget.setItem(row_idx, col_idx, item)
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
        self.add_button.clicked.connect(self.add_row)
        self.delete_button.setText("Удалить")
        self.sort_label.setText("Сортировать по")
        self.insert_data()

    def on_item_changed(self, item):
        row = item.row()
        column = item.column()

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
            if column == 0:
                self.old_values[row]['name'] = new_value
            elif column == 1:
                self.old_values[row]['surname'] = new_value
            elif column == 2:
                self.old_values[row]['patronymic'] = new_value
            elif column == 3:
                self.old_values[row]['phone'] = new_value

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

    def add_row(self):
        current_row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(current_row)

        # Автоматическое создание QTableWidgetItem для каждой ячейки новой строки
        for col in range(self.tableWidget.columnCount()):
            item = QTableWidgetItem("")
            self.tableWidget.setItem(current_row, col, item)

        # После добавления строки автоматически проверяем её заполненность и сохраняем в БД
        self.save_row_to_db(current_row)

    def save_row_to_db(self, row):
        # Проверка на пустые ячейки в строке
        row_data = []
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, col)
            if item is None or item.text().strip() == "":
                # Если ячейка пуста, выводим сообщение и выходим
                QMessageBox.warning(self, "Ошибка", "Все ячейки строки должны быть заполнены.")
                return
            row_data.append(item.text().strip())
        self.db.connect()
        self.db.insert_row_into_clients(row_data)



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
        self.delete_button.setText("Удалить")
        self.sort_label.setText("Сортировать по")
        self.insert_data()

    def on_item_changed(self, item):
        row = item.row()
        column = item.column()

        new_value = item.text()
        print(new_value)
        if new_value == '':
            item.setText(str(self.old_values[row]['name']))
        else:
            self.old_values[row]['name'] = new_value



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
        self.delete_button.setText("Удалить")
        self.sort_label.setText("Сортировать по")
        self.insert_data()



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

        row = item.row()
        column = item.column()

        if column in [2, 3]:
            new_value = item.text()

            if not self.is_valid_number(new_value):

                if column == 2:
                    item.setText(str(self.old_values[row]['price']))
                elif column == 3:
                    item.setText(str(self.old_values[row]['quantity']))
            else:

                if column == 2:
                    self.old_values[row]['price'] = float(new_value)
                elif column == 3:
                    self.old_values[row]['quantity'] = int(new_value)

        elif column in [0]:
            self.db.connect()
            categories = self.db.get_categories()
            new_value = item.text()
            if new_value == '' or new_value not in categories:
                item.setText(str(self.old_values[row]['category']))
            else:
                self.old_values[row]['category'] = new_value

        else:
            new_value = item.text()
            if new_value == '':
                item.setText(str(self.old_values[row]['name']))
            else:
                self.old_values[row]['name'] = new_value

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
    # db.connect()

    MainWindow = QtWidgets.QMainWindow()
    MainWindow.resize(1152, 864)
    ui = Sales(db)
    MainWindow.show()

    sys.exit(app.exec_())

