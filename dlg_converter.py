# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_converter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlg_converter(object):
    def setupUi(self, dlg_converter):
        dlg_converter.setObjectName("dlg_converter")
        dlg_converter.resize(600, 95)
        dlg_converter.setMinimumSize(QtCore.QSize(600, 95))
        dlg_converter.setMaximumSize(QtCore.QSize(16777215, 95))
        dlg_converter.setModal(True)
        self.dlg_v_layout = QtWidgets.QVBoxLayout(dlg_converter)
        self.dlg_v_layout.setContentsMargins(5, 5, 5, 5)
        self.dlg_v_layout.setSpacing(5)
        self.dlg_v_layout.setObjectName("dlg_v_layout")
        self.hl_convert_options_layout = QtWidgets.QHBoxLayout()
        self.hl_convert_options_layout.setSpacing(5)
        self.hl_convert_options_layout.setObjectName("hl_convert_options_layout")
        self.cb_old_values = QtWidgets.QComboBox(dlg_converter)
        self.cb_old_values.setCurrentText("")
        self.cb_old_values.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cb_old_values.setObjectName("cb_old_values")
        self.hl_convert_options_layout.addWidget(self.cb_old_values)
        self.lbl_to = QtWidgets.QLabel(dlg_converter)
        self.lbl_to.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_to.setObjectName("lbl_to")
        self.hl_convert_options_layout.addWidget(self.lbl_to)
        self.cb_new_values = QtWidgets.QComboBox(dlg_converter)
        self.cb_new_values.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cb_new_values.setObjectName("cb_new_values")
        self.hl_convert_options_layout.addWidget(self.cb_new_values)
        self.hl_convert_options_layout.setStretch(0, 1)
        self.hl_convert_options_layout.setStretch(2, 1)
        self.dlg_v_layout.addLayout(self.hl_convert_options_layout)
        self.hl_buttons = QtWidgets.QHBoxLayout()
        self.hl_buttons.setSpacing(5)
        self.hl_buttons.setObjectName("hl_buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hl_buttons.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(dlg_converter)
        self.btn_ok.setObjectName("btn_ok")
        self.hl_buttons.addWidget(self.btn_ok)
        self.btn_cancel = QtWidgets.QPushButton(dlg_converter)
        self.btn_cancel.setObjectName("btn_cancel")
        self.hl_buttons.addWidget(self.btn_cancel)
        self.hl_buttons.setStretch(0, 1)
        self.dlg_v_layout.addLayout(self.hl_buttons)

        self.retranslateUi(dlg_converter)
        QtCore.QMetaObject.connectSlotsByName(dlg_converter)

    def retranslateUi(self, dlg_converter):
        _translate = QtCore.QCoreApplication.translate
        dlg_converter.setWindowTitle(_translate("dlg_converter", "Dialog"))
        self.cb_old_values.setToolTip(_translate("dlg_converter", "Old value."))
        self.cb_old_values.setStatusTip(_translate("dlg_converter", "Old value."))
        self.cb_old_values.setWhatsThis(_translate("dlg_converter", "Old value."))
        self.lbl_to.setText(_translate("dlg_converter", "Convert to >>"))
        self.cb_new_values.setToolTip(_translate("dlg_converter", "New value."))
        self.cb_new_values.setStatusTip(_translate("dlg_converter", "New value."))
        self.cb_new_values.setWhatsThis(_translate("dlg_converter", "New value."))
        self.btn_ok.setText(_translate("dlg_converter", "&Ok"))
        self.btn_ok.setShortcut(_translate("dlg_converter", "Alt+O"))
        self.btn_cancel.setText(_translate("dlg_converter", "&Cancel"))
        self.btn_cancel.setShortcut(_translate("dlg_converter", "Esc"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dlg_converter = QtWidgets.QDialog()
    ui = Ui_dlg_converter()
    ui.setupUi(dlg_converter)
    dlg_converter.show()
    sys.exit(app.exec_())
