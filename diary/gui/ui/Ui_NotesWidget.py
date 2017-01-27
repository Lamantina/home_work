# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notes_widget.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.dateSelector = QtWidgets.QDateEdit(Form)
        self.dateSelector.setMinimumSize(QtCore.QSize(150, 0))
        self.dateSelector.setCalendarPopup(True)
        self.dateSelector.setObjectName("dateSelector")
        self.horizontalLayout_3.addWidget(self.dateSelector)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.notesView = QtWidgets.QTableView(Form)
        self.notesView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.notesView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.notesView.setObjectName("notesView")
        self.notesView.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.notesView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Выберите дату"))

