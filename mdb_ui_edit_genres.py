# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mdb_edit_genres.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_edit_genres_window(object):
    def setupUi(self, edit_genres_window):
        edit_genres_window.setObjectName("edit_genres_window")
        edit_genres_window.setWindowModality(QtCore.Qt.WindowModal)
        edit_genres_window.resize(800, 600)
        edit_genres_window.setMinimumSize(QtCore.QSize(640, 480))
        edit_genres_window.setMaximumSize(QtCore.QSize(1024, 768))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        edit_genres_window.setFont(font)
        self.central_widget = QtWidgets.QWidget(edit_genres_window)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gb_genres = QtWidgets.QGroupBox(self.central_widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.gb_genres.setFont(font)
        self.gb_genres.setAlignment(QtCore.Qt.AlignCenter)
        self.gb_genres.setObjectName("gb_genres")
        self.hl_genres = QtWidgets.QHBoxLayout(self.gb_genres)
        self.hl_genres.setContentsMargins(10, 10, 10, 10)
        self.hl_genres.setSpacing(5)
        self.hl_genres.setObjectName("hl_genres")
        self.lst_genres = QtWidgets.QListWidget(self.gb_genres)
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        self.hl_genres.setStretch(0, 1)
        self.hl_genres.setStretch(1, 3)
        self.verticalLayout_2.addWidget(self.gb_genres)
        self.gb_buttons = QtWidgets.QGroupBox(self.central_widget)
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
        self.btn_done = QtWidgets.QPushButton(self.gb_buttons)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_done.setFont(font)
        self.btn_done.setObjectName("btn_done")
        self.hl_buttons.addWidget(self.btn_done)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_buttons.addItem(spacerItem)
        self.btn_add_genre = QtWidgets.QPushButton(self.gb_buttons)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_add_genre.setFont(font)
        self.btn_add_genre.setObjectName("btn_add_genre")
        self.hl_buttons.addWidget(self.btn_add_genre)
        self.btn_update_genre = QtWidgets.QPushButton(self.gb_buttons)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_update_genre.setFont(font)
        self.btn_update_genre.setObjectName("btn_update_genre")
        self.hl_buttons.addWidget(self.btn_update_genre)
        self.btn_delete_genre = QtWidgets.QPushButton(self.gb_buttons)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_delete_genre.setFont(font)
        self.btn_delete_genre.setObjectName("btn_delete_genre")
        self.hl_buttons.addWidget(self.btn_delete_genre)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_buttons.addItem(spacerItem1)
        self.btn_clear = QtWidgets.QPushButton(self.gb_buttons)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.hl_buttons.addWidget(self.btn_clear)
        self.verticalLayout_2.addWidget(self.gb_buttons)
        edit_genres_window.setCentralWidget(self.central_widget)

        self.retranslateUi(edit_genres_window)
        QtCore.QMetaObject.connectSlotsByName(edit_genres_window)
        edit_genres_window.setTabOrder(self.le_genre_name, self.te_genre_description)
        edit_genres_window.setTabOrder(self.te_genre_description, self.te_genre_examples)
        edit_genres_window.setTabOrder(self.te_genre_examples, self.btn_done)
        edit_genres_window.setTabOrder(self.btn_done, self.btn_add_genre)
        edit_genres_window.setTabOrder(self.btn_add_genre, self.btn_update_genre)
        edit_genres_window.setTabOrder(self.btn_update_genre, self.btn_delete_genre)
        edit_genres_window.setTabOrder(self.btn_delete_genre, self.btn_clear)
        edit_genres_window.setTabOrder(self.btn_clear, self.lst_genres)

    def retranslateUi(self, edit_genres_window):
        _translate = QtCore.QCoreApplication.translate
        edit_genres_window.setWindowTitle(_translate("edit_genres_window", "Edit Genres"))
        self.gb_genres.setTitle(_translate("edit_genres_window", "Genres"))
        self.lbl_genre_name.setText(_translate("edit_genres_window", "Genre Name"))
        self.le_genre_name.setPlaceholderText(_translate("edit_genres_window", "e.g. Rock & Roll, RPG, Comedy, etc."))
        self.lbl_genre_description.setText(_translate("edit_genres_window", "Genre Description"))
        self.te_genre_description.setPlaceholderText(_translate("edit_genres_window", "e.g. Rock & Roll is a popular style of music..."))
        self.lbl_genre_examples.setText(_translate("edit_genres_window", "Genre Examples"))
        self.te_genre_examples.setPlaceholderText(_translate("edit_genres_window", "e.g. ACDC, Meat Loaf, etc."))
        self.btn_done.setText(_translate("edit_genres_window", "&Done"))
        self.btn_done.setShortcut(_translate("edit_genres_window", "Esc"))
        self.btn_add_genre.setText(_translate("edit_genres_window", "&Add"))
        self.btn_add_genre.setShortcut(_translate("edit_genres_window", "Alt+A"))
        self.btn_update_genre.setText(_translate("edit_genres_window", "&Update"))
        self.btn_update_genre.setShortcut(_translate("edit_genres_window", "Alt+U"))
        self.btn_delete_genre.setText(_translate("edit_genres_window", "D&elete"))
        self.btn_clear.setText(_translate("edit_genres_window", "&Clear"))
        self.btn_clear.setShortcut(_translate("edit_genres_window", "Alt+C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_genres_window = QtWidgets.QMainWindow()
    ui = Ui_edit_genres_window()
    ui.setupUi(edit_genres_window)
    edit_genres_window.show()
    sys.exit(app.exec_())

