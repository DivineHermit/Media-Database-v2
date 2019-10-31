# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dlg_edit_types.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlg_edit_types(object):
    def setupUi(self, dlg_edit_types):
        dlg_edit_types.setObjectName("dlg_edit_types")
        dlg_edit_types.resize(300, 480)
        dlg_edit_types.setMinimumSize(QtCore.QSize(300, 480))
        dlg_edit_types.setMaximumSize(QtCore.QSize(600, 800))
        dlg_edit_types.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(dlg_edit_types)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gb_media_types = QtWidgets.QGroupBox(dlg_edit_types)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.gb_media_types.setFont(font)
        self.gb_media_types.setAlignment(QtCore.Qt.AlignCenter)
        self.gb_media_types.setObjectName("gb_media_types")
        self.dlg_grid_layout = QtWidgets.QGridLayout(self.gb_media_types)
        self.dlg_grid_layout.setContentsMargins(5, 5, 5, 5)
        self.dlg_grid_layout.setSpacing(5)
        self.dlg_grid_layout.setObjectName("dlg_grid_layout")
        self.btn_done = QtWidgets.QPushButton(self.gb_media_types)
        self.btn_done.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_done.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_done.setFont(font)
        self.btn_done.setDefault(True)
        self.btn_done.setObjectName("btn_done")
        self.dlg_grid_layout.addWidget(self.btn_done, 3, 2, 1, 1)
        self.btn_add_type = QtWidgets.QPushButton(self.gb_media_types)
        self.btn_add_type.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_add_type.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_add_type.setFont(font)
        self.btn_add_type.setObjectName("btn_add_type")
        self.dlg_grid_layout.addWidget(self.btn_add_type, 3, 0, 1, 1)
        self.btn_delete_type = QtWidgets.QPushButton(self.gb_media_types)
        self.btn_delete_type.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_delete_type.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_delete_type.setFont(font)
        self.btn_delete_type.setObjectName("btn_delete_type")
        self.dlg_grid_layout.addWidget(self.btn_delete_type, 3, 1, 1, 1)
        self.lst_media_types = QtWidgets.QListView(self.gb_media_types)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lst_media_types.setFont(font)
        self.lst_media_types.setObjectName("lst_media_types")
        self.dlg_grid_layout.addWidget(self.lst_media_types, 0, 0, 3, 3)
        self.gridLayout_2.addWidget(self.gb_media_types, 0, 0, 1, 1)

        self.retranslateUi(dlg_edit_types)
        QtCore.QMetaObject.connectSlotsByName(dlg_edit_types)
        dlg_edit_types.setTabOrder(self.btn_done, self.lst_media_types)

    def retranslateUi(self, dlg_edit_types):
        _translate = QtCore.QCoreApplication.translate
        dlg_edit_types.setWindowTitle(_translate("dlg_edit_types", "Dialog"))
        self.gb_media_types.setTitle(_translate("dlg_edit_types", "Edit Media Types"))
        self.btn_done.setText(_translate("dlg_edit_types", "&Done"))
        self.btn_done.setShortcut(_translate("dlg_edit_types", "Esc"))
        self.btn_add_type.setText(_translate("dlg_edit_types", "&Add"))
        self.btn_add_type.setShortcut(_translate("dlg_edit_types", "Alt+A"))
        self.btn_delete_type.setText(_translate("dlg_edit_types", "Delete"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dlg_edit_types = QtWidgets.QDialog()
    ui = Ui_dlg_edit_types()
    ui.setupUi(dlg_edit_types)
    dlg_edit_types.show()
    sys.exit(app.exec_())
