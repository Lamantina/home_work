# coding: utf-8

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class NoteModel(QSqlTableModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setTable('note')

        headers = ['ID',
                   'Наименование',
                   'Запланировано',
                   'Текст',
                   'Статус',
                   'Создан']

        # метод возвращает количество колонок в таблице
        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Horizontal, headers[i])


