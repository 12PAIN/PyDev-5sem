import csv
import sqlite3
import sys
import re
from sqlite3 import Error

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from form import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений


        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Фильмы')


class Repository:

    def __init__(self):
        self.database = 'films_db.sqlite'

    def getConnection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.database)
            return connection
        except Error as e:
            print(e)

        return connection

    def getTables(self):
        conn = self.getConnection()
        conn.text_factory = str
        cursor = conn.cursor()
        tablesFetch = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        table_names = sorted(list(zip(*tablesFetch))[0])

        return table_names

    def getTableColumnNames(self, tableName):
        conn = self.getConnection()
        conn.text_factory = str
        cursor = conn.cursor()

        columnNamesFetch = cursor.execute("PRAGMA table_info('%s')" % tableName).fetchall()
        return list(list(zip(*columnNamesFetch))[1])
        # return columnNamesFetch
    def getTextInfo(self):
        newline_indent = '\n   '
        con = self.getConnection()
        con.text_factory = str
        cur = con.cursor()

        result = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        table_names =sorted(list(zip(*result))[0])
        print("\ntables are:" + newline_indent + newline_indent.join(table_names))

        for table_name in table_names:
            result = cur.execute("PRAGMA table_info('%s')" % table_name).fetchall()
            column_names = list(zip(*result))[1]
            print(("\ncolumn names for %s:" % table_name)
                  + newline_indent
                  + (newline_indent.join(column_names)))

        con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ex = MyWidget()
    # ex.show()
    # sys.excepthook = except_hook
    # sys.exit(app.exec_())

    db = Repository()
    # db.getInfo()
    # print(db.getTables())
    print(db.getTableColumnNames('films'))
