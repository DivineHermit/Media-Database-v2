# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dlg_edit_genres.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlg_edit_genres(object):
    def setupUi(self, dlg_edit_genres):
        dlg_edit_genres.setObjectName("dlg_edit_genres")
        dlg_edit_genres.resize(640, 480)
        dlg_edit_genres.setMinimumSize(QtCore.QSize(640, 480))
        dlg_edit_genres.setMaximumSize(QtCore.QSize(1024, 768))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        dlg_edit_genres.setFont(font)
        dlg_edit_genres.setModal(True)
        self.dlg_grid_layout = QtWidgets.QGridLayout(dlg_edit_genres)
        self.dlg_grid_layout.setContentsMargins(5, 5, 5, 5)
        self.dlg_grid_layout.setSpacing(5)
        self.dlg_grid_layout.setObjectName("dlg_grid_layout")
        self.gb_genres = QtWidgets.QGroupBox(dlg_edit_genres)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.gb_genres.setFont(font)
        self.gb_genres.setAlignment(QtCore.Qt.AlignCenter)
        self.gb_genres.setObjectName("gb_genres")
        self.hl_genres = QtWidgets.QHBoxLayout(self.gb_genres)
        self.hl_genres.setContentsMargins(5, 0, 5, 5)
        self.hl_genres.setSpacing(5)
        self.hl_genres.setObjectName("hl_genres")
        self.lst_genres = QtWidgets.QListView(self.gb_genres)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lst_genres.setFont(font)
        self.lst_genres.setObjectName("lst_genres")
        self.hl_genres.addWidget(self.lst_genres)
        self.vl_genre_info = QtWidgets.QVBoxLayout()
        self.vl_genre_info.setSpacing(5)
        self.vl_genre_info.setObjectName("vl_genre_info")
        self.lbl_genre_name = QtWidgets.QLabel(self.gb_genres)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lbl_genre_name.setFont(font)
        self.lbl_genre_name.setObjectName("lbl_genre_name")
        self.vl_genre_info.addWidget(self.lbl_genre_name)
        self.le_genre_name = QtWidgets.QLineEdit(self.gb_genres)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.le_genre_name.setFont(font)
        self.le_genre_name.setObjectName("le_genre_name")
        self.vl_genre_info.addWidget(self.le_genre_name)
        self.lbl_genre_description = QtWidgets.QLabel(self.gb_genres)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lbl_genre_description.setFont(font)
        self.lbl_genre_description.setObjectName("lbl_genre_description")
        self.vl_genre_info.addWidget(self.lbl_genre_description)
        self.te_genre_description = QtWidgets.QPlainTextEdit(self.gb_genres)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.te_genre_description.setFont(font)
        self.te_genre_description.setTabChangesFocus(True)
        self.te_genre_description.setObjectName("te_genre_description")
        self.vl_genre_info.addWidget(self.te_genre_description)
        self.lbl_genre_examples = QtWidgets.QLabel(self.gb_genres)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lbl_genre_examples.setFont(font)
        self.lbl_genre_examples.setObjectName("lbl_genre_examples")
        self.vl_genre_info.addWidget(self.lbl_genre_examples)
        self.te_genre_examples = QtWidgets.QPlainTextEdit(self.gb_genres)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.te_genre_examples.setFont(font)
        self.te_genre_examples.setTabChangesFocus(True)
        self.te_genre_examples.setObjectName("te_genre_examples")
        self.vl_genre_info.addWidget(self.te_genre_examples)
        self.hl_genres.addLayout(self.vl_genre_info)
        self.hl_genres.setStretch(1, 3)
        self.dlg_grid_layout.addWidget(self.gb_genres, 0, 0, 1, 1)
        self.gb_buttons = QtWidgets.QGroupBox(dlg_edit_genres)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.gb_buttons.setFont(font)
        self.gb_buttons.setTitle("")
        self.gb_buttons.setObjectName("gb_buttons")
        self.hl_buttons = QtWidgets.QHBoxLayout(self.gb_buttons)
        self.hl_buttons.setContentsMargins(5, 5, 5, 5)
        self.hl_buttons.setSpacing(5)
        self.hl_buttons.setObjectName("hl_buttons")
        self.btn_add_genre = QtWidgets.QPushButton(self.gb_buttons)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_add_genre.setFont(font)
        self.btn_add_genre.setObjectName("btn_add_genre")
        self.hl_buttons.addWidget(self.btn_add_genre)
        self.btn_delete_genre = QtWidgets.QPushButton(self.gb_buttons)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_delete_genre.setFont(font)
        self.btn_delete_genre.setObjectName("btn_delete_genre")
        self.hl_buttons.addWidget(self.btn_delete_genre)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_buttons.addItem(spacerItem)
        self.btn_done = QtWidgets.QPushButton(self.gb_buttons)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_done.setFont(font)
        self.btn_done.setDefault(True)
        self.btn_done.setObjectName("btn_done")
        self.hl_buttons.addWidget(self.btn_done)
        self.dlg_grid_layout.addWidget(self.gb_buttons, 1, 0, 1, 1)
        self.lbl_genre_name.setBuddy(self.le_genre_name)
        self.lbl_genre_description.setBuddy(self.te_genre_description)
        self.lbl_genre_examples.setBuddy(self.te_genre_examples)

        self.retranslateUi(dlg_edit_genres)
        QtCore.QMetaObject.connectSlotsByName(dlg_edit_genres)

    def retranslateUi(self, dlg_edit_genres):
        _translate = QtCore.QCoreApplication.translate
        dlg_edit_genres.setWindowTitle(_translate("dlg_edit_genres", "Edit Genres"))
        self.gb_genres.setTitle(_translate("dlg_edit_genres", "Edit Genres Details"))
        self.lbl_genre_name.setText(_translate("dlg_edit_genres", "Genre &Name"))
        self.le_genre_name.setPlaceholderText(_translate("dlg_edit_genres", "e.g. Rock & Roll, RPG, Comedy, etc."))
        self.lbl_genre_description.setText(_translate("dlg_edit_genres", "Genre &Description"))
        self.te_genre_description.setPlaceholderText(
            _translate("dlg_edit_genres", "e.g. Rock & Roll is a popular style of music..."))
        self.lbl_genre_examples.setText(_translate("dlg_edit_genres", "Genre E&xamples"))
        self.te_genre_examples.setPlaceholderText(_translate("dlg_edit_genres", "e.g. ACDC, Meat Loaf, etc."))
        self.btn_add_genre.setText(_translate("dlg_edit_genres", "&Add"))
        self.btn_add_genre.setShortcut(_translate("dlg_edit_genres", "Alt+A"))
        self.btn_delete_genre.setText(_translate("dlg_edit_genres", "Delete"))
        self.btn_done.setText(_translate("dlg_edit_genres", "&Done"))
        self.btn_done.setShortcut(_translate("dlg_edit_genres", "Esc"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dlg_edit_genres = QtWidgets.QDialog()
    ui = Ui_dlg_edit_genres()
    ui.setupUi(dlg_edit_genres)
    dlg_edit_genres.show()
    sys.exit(app.exec_())
