# coding: utf-8

from  PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from .ui.Ui_MainWindow import Ui_MainWindow
from .NotesWidget import NotesWidget
from .LoginFormWidget import LoginFormWidget
from core.NoteModel import NoteModel

PASSWORD = 'admin'
USERNAME = 'admin'

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.setupUi(self)

        # создание виджета
        self.notesWidget = NotesWidget(NoteModel(self),self)
        # добавляем страницу
        self.stackedWidget.addWidget(self.notesWidget)
        # делаем ее текущей страницей
        self.stackedWidget.setCurrentWidget(self.notesWidget)


        self.loginFormWidget = LoginFormWidget(self)
        self.stackedWidget.addWidget(self.loginFormWidget)
        self.stackedWidget.setCurrentWidget(self.loginFormWidget)






    def init_signals(self):

        self.loginFormWidget.logPass.connect(self.close_log_window)


    def init_signals_all(self):

        self.actionAdd.triggered.connect(self.notesWidget.add_new_note)
        self.actionExit.triggered.connect(self.close)

        self.actionEdit.triggered.connect(self.notesWidget.edit_selected_note)

        self.actionRemove.triggered.connect(self.notesWidget.remove_selected_note)

        self.notesWidget.selection_changed.connect(self.update_menu)


    def close_log_window(self):
        self.init_signals_all()

        self.stackedWidget.setCurrentWidget(self.notesWidget)
        self.menubar.setHidden(False)
        self.toolBar.setHidden(False)
        self.statusbar.setHidden(False)

    def update_menu(self):
        selected = self.notesWidget.selected_rows()
        self.actionEdit.setEnabled(len(selected) == 1)
        self.actionRemove.setEnabled(bool(selected))





