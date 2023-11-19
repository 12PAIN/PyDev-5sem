import csv
import sys
import re

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from form import Ui_MainWindow


# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений

        self.schoolFilter = ''
        self.classFilter = ''

        self.setupUi(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Отображение CSV')
        self.classNumber.hide()
        self.schoolNumber.hide()
        self.classChoose.stateChanged.connect(self.setClassFilterInputVisible)
        self.schoolChoose.stateChanged.connect(self.setSchoolFilterInputVisible)

        self.loadData()
        self.dataBase.setColumnCount(len(self.title))
        self.dataBase.setHorizontalHeaderLabels(self.title)
        self.displayDataOnTable()

        self.classNumber.currentTextChanged.connect(self.filterChanged)
        self.schoolNumber.currentTextChanged.connect(self.filterChanged)

        self.classNumber.addItems(self.getClassNumber())
        self.schoolNumber.addItems(self.getSchoolNumber())

        self.classNumber.setCurrentText('')
        self.schoolNumber.setCurrentText('')


    def displayDataOnTable(self):
        regex = "^.*$"
        if self.schoolFilter != '' and self.classFilter == '':
            regex = f"^sh-kaluga16-{self.schoolFilter}-.*$"
        elif self.classFilter != '' and self.schoolFilter == '':
            regex = f"^sh-kaluga16-\d{{2}}-{self.classFilter}-.*$"
        elif self.schoolFilter != '' and self.classFilter != '':
            regex = f"^sh-kaluga16-{self.schoolFilter}-{self.classFilter}-.*$"

        filterFlag = True if self.schoolFilter != '' or self.classFilter != '' else False

        regex = re.compile(regex)

        def filterData(item):
            return False if regex.match(item[1]) is None else True

        currentData = list(filter(filterData, self.data))

        cMap = [None] * len(currentData)
        j = 0
        for i, data in enumerate(currentData):

            def currentColor(j):
                if j == 0:
                    currentColor = 'green'
                elif j == 1:
                    currentColor = 'yellow'
                else:
                    currentColor = 'cyan'
                return currentColor

            if data[-1] == '0':
                break

            if i == 0:
                cMap[i] = currentColor(j)

            if i > 0:
                if currentData[i - 1][-1] == currentData[i][-1]:
                    cMap[i] = cMap[i - 1]
                else:
                    j += 1
                    if j > 2:
                        break
                    cMap[i] = currentColor(j)

        self.dataBase.setRowCount(len(currentData))

        for i, row in enumerate(currentData):
            for j, elem in enumerate(row):
                self.dataBase.setItem(
                    i, j, QTableWidgetItem(elem))

            if cMap[i] is not None and filterFlag:
                for j in range(self.dataBase.columnCount()):
                    self.dataBase.item(i, j).setBackground(QColor(cMap[i]))

        self.dataBase.resizeColumnsToContents()

    def loadData(self):

        repository = Repository()
        title, data = repository.getData()

        self.title = ["ФИО", "Логин", "Суммарный балл"]
        self.data = [None] * len(data)

        for i, row in enumerate(data):
            self.data[i] = [None] * 3
            k = 0
            for j, value in enumerate(row):
                if j in [1, 2, 7]:
                    self.data[i][k] = row[j]
                    k += 1

    def filterChanged(self):
        if self.sender().objectName() == "schoolNumber":
            filterValue = self.schoolNumber.currentText()
            self.schoolFilter = filterValue


            self.classNumber.clear()
            classNumbers = self.getClassNumberForSchool(filterValue)
            self.classNumber.addItems(classNumbers)



        elif self.sender().objectName() == "classNumber":
            filterValue = self.classNumber.currentText()
            self.classFilter = filterValue

        self.displayDataOnTable()

    def setClassFilterInputVisible(self):
        if not self.classChoose.isChecked():
            self.classNumber.hide()
            self.classFilter = ''
            self.classNumber.clear()
            self.classNumber.addItems(self.getClassNumber())
        else:
            self.classNumber.show()


        self.filterChanged()

    def setSchoolFilterInputVisible(self):
        if not self.schoolChoose.isChecked():
            self.schoolNumber.hide()
            self.schoolFilter = ''
            self.classNumber.clear()
            self.classNumber.addItems(self.getClassNumber())
        else:
            self.schoolNumber.show()


        self.filterChanged()

    def get_column_data(self, column):
        data = [self.dataBase.item(row, column).text()
                for row in range(self.dataBase.rowCount())]
        return data

    def getClassNumber(self):
        classes = set()
        data = self.get_column_data(1)
        for i in data:
            classes.add(i.split("-")[3])
        classes.add('')
        return sorted(classes)

    def getClassNumberForSchool(self, schoolNumber=None):
        if schoolNumber is None or schoolNumber == '':
            return self.getClassNumber()

        classes = set()
        data = self.get_column_data(1)
        for i in data:
            if i.split("-")[2] == schoolNumber:
                classes.add(i.split("-")[3])
        classes.add('')

        return sorted(classes)

    def getSchoolNumber(self):
        schools = set()
        data = self.get_column_data(1)
        for i in data:
            schools.add(i.split("-")[2])
        schools.add('')
        return sorted(schools)


class Repository:

    def __init__(self):
        self.table_name = "../rez.csv"

    def getData(self):
        with open(self.table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            title = next(reader)
            return title, list(reader)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())