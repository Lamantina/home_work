# coding: utf-8

from PyQt5.QtCore import QObject, QFile
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

SCHEMA = 'resourses/schema.sql'
DATABASE_NAME = 'diary.sqlite'



class DataBase(QObject):
    def __open(self):
        self.__db = QSqlDatabase().addDatabase('QSQLITE')
        self.__db.setDatabaseName(DATABASE_NAME)
        # вернет True или False (подключились или нет)
        return self.__db.open()

    def __restore(self):
        if not self.__open():
            return False

        # в переменной queries будет лежать список
        queries = open(SCHEMA).read().split(';')

        for query in queries:
            query = query.strip()

            if query:
                # выполнение запросов к базе данных
                sql = QSqlQuery(self.__db)
                if not sql.exec(query):
                    QFile(DATABASE_NAME).remove()
                    return  False

        return True

    def connect(self):
        return self.__open() if QFile(DATABASE_NAME).exists() else self.__restore()



