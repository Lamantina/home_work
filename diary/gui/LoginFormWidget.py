# coding: utf-8

from  PyQt5.QtWidgets import QWidget, QMessageBox
from .ui.Ui_LoginFormWidget import Ui_Form
from PyQt5.QtCore import pyqtSignal


PASSWORD = 'admin'
USERNAME = 'admin'

class LoginFormWidget(QWidget, Ui_Form):

    log_pass = pyqtSignal(name='logPass')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.init_signals()


    def init_signals(self):
        self.loginBtn.clicked.connect(self.on_click_login)

    def on_click_login(self):

        if (str(self.usernameLineEdit.text()) == USERNAME and
                    str(self.passwordLineEdit.text()) == PASSWORD):
            self.log_pass.emit()

        else:
            self.errorMessage = QMessageBox.critical(self,'Ошибка', 'Неверный логин/пароль')


