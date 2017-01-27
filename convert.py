import sys
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QDoubleSpinBox,
    QVBoxLayout
)


class Course(QObject):
    def get(self):
        return 59.15


class Converter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.init_signals()
        self.initLayout()

    def initUi(self):
        self.setWindowTitle('Конвертер')
        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)
        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(99999999)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(9999999)

        self.convertBtn = QPushButton('Перевести', self)
        self.clearBtn = QPushButton('Очистить', self)
        self.convertBtn.setEnabled(False)

    def init_signals(self):
        self.convertBtn.clicked.connect(self.on_click)
        self.clearBtn.clicked.connect(self.on_clear)
        self.srcAmount.valueChanged.connect(self.change_value)
        self.resultAmount.valueChanged.connect(self.change_value)

    def on_click(self):
        value = max(self.srcAmount.value(), self.resultAmount.value())
        if self.srcAmount.value() != 0:
            self.resultAmount.setValue(value / Course().get())
        else:
            self.srcAmount.setValue(value / Course().get())

    def on_clear(self):
        self.resultAmount.setValue(0)
        self.srcAmount.setValue(0)

    def change_value(self):
        if self.srcAmount.value() == 0 and self.resultAmount.value() != 0:
            self.convertBtn.setEnabled(True)
        elif self.srcAmount.value() > 0 and self.resultAmount.value() == 0:
            self.convertBtn.setEnabled(True)
        else:
            self.convertBtn.setEnabled(False)

    def initLayout(self):
        self.w = QWidget()

        self.mainLayout = QVBoxLayout(self.w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.clearBtn)
        self.setCentralWidget(self.w)

    def press_event(self, key):
        if key.key() == Qt.Key_Enter: self.on_click()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = Converter()
    converter.show()

    sys.exit(app.exec_())