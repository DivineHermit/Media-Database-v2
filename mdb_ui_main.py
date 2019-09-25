# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mdb2_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 675)
        MainWindow.setMinimumSize(QtCore.QSize(800, 675))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.main_window = QtWidgets.QWidget(MainWindow)
        self.main_window.setObjectName("main_window")
        self.gl_main_window = QtWidgets.QGridLayout(self.main_window)
        self.gl_main_window.setContentsMargins(5, 5, 5, 5)
        self.gl_main_window.setSpacing(5)
        self.gl_main_window.setObjectName("gl_main_window")
        self.gb_search_bar = QtWidgets.QGroupBox(self.main_window)
        self.gb_search_bar.setObjectName("gb_search_bar")
        self.vl_search_bar = QtWidgets.QVBoxLayout(self.gb_search_bar)
        self.vl_search_bar.setContentsMargins(5, 0, 5, 5)
        self.vl_search_bar.setSpacing(5)
        self.vl_search_bar.setObjectName("vl_search_bar")
        self.le_search_bar = QtWidgets.QLineEdit(self.gb_search_bar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_search_bar.setFont(font)
        self.le_search_bar.setObjectName("le_search_bar")
        self.vl_search_bar.addWidget(self.le_search_bar)
        self.hl_search_options = QtWidgets.QHBoxLayout()
        self.hl_search_options.setSpacing(5)
        self.hl_search_options.setObjectName("hl_search_options")
        self.rb_title = QtWidgets.QRadioButton(self.gb_search_bar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rb_title.setFont(font)
        self.rb_title.setChecked(True)
        self.rb_title.setObjectName("rb_title")
        self.hl_search_options.addWidget(self.rb_title)
        self.rb_description = QtWidgets.QRadioButton(self.gb_search_bar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rb_description.setFont(font)
        self.rb_description.setObjectName("rb_description")
        self.hl_search_options.addWidget(self.rb_description)
        self.rb_genre = QtWidgets.QRadioButton(self.gb_search_bar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rb_genre.setFont(font)
        self.rb_genre.setObjectName("rb_genre")
        self.hl_search_options.addWidget(self.rb_genre)
        self.rb_notes = QtWidgets.QRadioButton(self.gb_search_bar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.rb_notes.setFont(font)
        self.rb_notes.setObjectName("rb_notes")
        self.hl_search_options.addWidget(self.rb_notes)
        self.vl_search_bar.addLayout(self.hl_search_options)
        self.gl_main_window.addWidget(self.gb_search_bar, 0, 0, 1, 1)
        self.gb_entry_count = QtWidgets.QGroupBox(self.main_window)
        self.gb_entry_count.setTitle("")
        self.gb_entry_count.setObjectName("gb_entry_count")
        self.vl_count_display = QtWidgets.QVBoxLayout(self.gb_entry_count)
        self.vl_count_display.setContentsMargins(5, 5, 5, 5)
        self.vl_count_display.setSpacing(5)
        self.vl_count_display.setObjectName("vl_count_display")
        self.lbl_entries_count = QtWidgets.QLabel(self.gb_entry_count)
        self.lbl_entries_count.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_entries_count.setFont(font)
        self.lbl_entries_count.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_entries_count.setWordWrap(True)
        self.lbl_entries_count.setObjectName("lbl_entries_count")
        self.vl_count_display.addWidget(self.lbl_entries_count)
        self.gl_main_window.addWidget(self.gb_entry_count, 2, 0, 1, 1)
        self.hl_media_display = QtWidgets.QHBoxLayout()
        self.hl_media_display.setSpacing(5)
        self.hl_media_display.setObjectName("hl_media_display")
        self.gb_media_titles = QtWidgets.QGroupBox(self.main_window)
        self.gb_media_titles.setObjectName("gb_media_titles")
        self.vl_entries_list = QtWidgets.QVBoxLayout(self.gb_media_titles)
        self.vl_entries_list.setContentsMargins(5, 0, 5, 5)
        self.vl_entries_list.setSpacing(5)
        self.vl_entries_list.setObjectName("vl_entries_list")
        self.lst_media_list = QtWidgets.QListView(self.gb_media_titles)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lst_media_list.setFont(font)
        self.lst_media_list.setObjectName("lst_media_list")
        self.vl_entries_list.addWidget(self.lst_media_list)
        self.hl_media_display.addWidget(self.gb_media_titles)
        self.gb_entries_info = QtWidgets.QGroupBox(self.main_window)
        self.gb_entries_info.setObjectName("gb_entries_info")
        self.gl_details = QtWidgets.QGridLayout(self.gb_entries_info)
        self.gl_details.setContentsMargins(5, 0, 5, 5)
        self.gl_details.setSpacing(5)
        self.gl_details.setObjectName("gl_details")
        self.fl_info = QtWidgets.QFormLayout()
        self.fl_info.setSpacing(5)
        self.fl_info.setObjectName("fl_info")
        self.lbl_Title = QtWidgets.QLabel(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_Title.setFont(font)
        self.lbl_Title.setObjectName("lbl_Title")
        self.fl_info.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_Title)
        self.le_title = QtWidgets.QLineEdit(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_title.setFont(font)
        self.le_title.setObjectName("le_title")
        self.fl_info.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_title)
        self.lbl_description = QtWidgets.QLabel(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_description.setFont(font)
        self.lbl_description.setObjectName("lbl_description")
        self.fl_info.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_description)
        self.lbl_genre = QtWidgets.QLabel(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_genre.setFont(font)
        self.lbl_genre.setObjectName("lbl_genre")
        self.fl_info.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_genre)
        self.lbl_season = QtWidgets.QLabel(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_season.setFont(font)
        self.lbl_season.setObjectName("lbl_season")
        self.fl_info.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_season)
        self.lbl_disc_count = QtWidgets.QLabel(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_disc_count.setFont(font)
        self.lbl_disc_count.setObjectName("lbl_disc_count")
        self.fl_info.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_disc_count)
        self.lbl_media_type = QtWidgets.QLabel(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_media_type.setFont(font)
        self.lbl_media_type.setObjectName("lbl_media_type")
        self.fl_info.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.lbl_media_type)
        self.lbl_age_rating = QtWidgets.QLabel(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_age_rating.setFont(font)
        self.lbl_age_rating.setObjectName("lbl_age_rating")
        self.fl_info.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_age_rating)
        self.te_description = QtWidgets.QPlainTextEdit(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.te_description.setFont(font)
        self.te_description.setTabChangesFocus(True)
        self.te_description.setObjectName("te_description")
        self.fl_info.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.te_description)
        self.le_age_rating = QtWidgets.QLineEdit(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_age_rating.setFont(font)
        self.le_age_rating.setObjectName("le_age_rating")
        self.fl_info.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_age_rating)
        self.sb_season = QtWidgets.QSpinBox(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sb_season.setFont(font)
        self.sb_season.setObjectName("sb_season")
        self.fl_info.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sb_season)
        self.sb_disc_count = QtWidgets.QSpinBox(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sb_disc_count.setFont(font)
        self.sb_disc_count.setMinimum(1)
        self.sb_disc_count.setObjectName("sb_disc_count")
        self.fl_info.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.sb_disc_count)
        self.lbl_play_time = QtWidgets.QLabel(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_play_time.setFont(font)
        self.lbl_play_time.setObjectName("lbl_play_time")
        self.fl_info.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.lbl_play_time)
        self.sb_play_time = QtWidgets.QSpinBox(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sb_play_time.setFont(font)
        self.sb_play_time.setMaximum(25000)
        self.sb_play_time.setObjectName("sb_play_time")
        self.fl_info.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.sb_play_time)
        self.cb_genre = QtWidgets.QComboBox(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cb_genre.setFont(font)
        self.cb_genre.setObjectName("cb_genre")
        self.fl_info.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cb_genre)
        self.cb_media_type = QtWidgets.QComboBox(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cb_media_type.setFont(font)
        self.cb_media_type.setObjectName("cb_media_type")
        self.fl_info.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.cb_media_type)
        self.lbl_notes = QtWidgets.QLabel(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lbl_notes.setFont(font)
        self.lbl_notes.setObjectName("lbl_notes")
        self.fl_info.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.lbl_notes)
        self.te_notes = QtWidgets.QPlainTextEdit(self.gb_entries_info)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.te_notes.setFont(font)
        self.te_notes.setTabChangesFocus(True)
        self.te_notes.setObjectName("te_notes")
        self.fl_info.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.te_notes)
        self.gl_details.addLayout(self.fl_info, 0, 0, 1, 1)
        self.hl_media_display.addWidget(self.gb_entries_info)
        self.hl_media_display.setStretch(0, 1)
        self.hl_media_display.setStretch(1, 3)
        self.gl_main_window.addLayout(self.hl_media_display, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.main_window)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuData = QtWidgets.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuDisplay_Count_By = QtWidgets.QMenu(self.menuView)
        self.menuDisplay_Count_By.setObjectName("menuDisplay_Count_By")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setAutoRepeat(False)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAdd_Entry = QtWidgets.QAction(MainWindow)
        self.actionAdd_Entry.setAutoRepeat(False)
        self.actionAdd_Entry.setObjectName("actionAdd_Entry")
        self.actionDelete_Entry = QtWidgets.QAction(MainWindow)
        self.actionDelete_Entry.setAutoRepeat(False)
        self.actionDelete_Entry.setObjectName("actionDelete_Entry")
        self.actionUpdate_Entry = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Entry.setAutoRepeat(False)
        self.actionUpdate_Entry.setObjectName("actionUpdate_Entry")
        self.actionEdit_Genres = QtWidgets.QAction(MainWindow)
        self.actionEdit_Genres.setAutoRepeat(False)
        self.actionEdit_Genres.setObjectName("actionEdit_Genres")
        self.actionEdit_Media_Types = QtWidgets.QAction(MainWindow)
        self.actionEdit_Media_Types.setAutoRepeat(False)
        self.actionEdit_Media_Types.setObjectName("actionEdit_Media_Types")
        self.actionDelete_Genre = QtWidgets.QAction(MainWindow)
        self.actionDelete_Genre.setAutoRepeat(False)
        self.actionDelete_Genre.setObjectName("actionDelete_Genre")
        self.actionDelete_Media_Type = QtWidgets.QAction(MainWindow)
        self.actionDelete_Media_Type.setAutoRepeat(False)
        self.actionDelete_Media_Type.setObjectName("actionDelete_Media_Type")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setAutoRepeat(False)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClear_UI = QtWidgets.QAction(MainWindow)
        self.actionClear_UI.setAutoRepeat(False)
        self.actionClear_UI.setObjectName("actionClear_UI")
        self.actionConvert_Types = QtWidgets.QAction(MainWindow)
        self.actionConvert_Types.setObjectName("actionConvert_Types")
        self.actionConvert_Genres = QtWidgets.QAction(MainWindow)
        self.actionConvert_Genres.setObjectName("actionConvert_Genres")
        self.actionDisplay_by_Genre = QtWidgets.QAction(MainWindow)
        self.actionDisplay_by_Genre.setCheckable(True)
        self.actionDisplay_by_Genre.setAutoRepeat(False)
        self.actionDisplay_by_Genre.setObjectName("actionDisplay_by_Genre")
        self.actionDisplay_by_Type = QtWidgets.QAction(MainWindow)
        self.actionDisplay_by_Type.setCheckable(True)
        self.actionDisplay_by_Type.setChecked(True)
        self.actionDisplay_by_Type.setAutoRepeat(False)
        self.actionDisplay_by_Type.setObjectName("actionDisplay_by_Type")
        self.menuFile.addAction(self.actionQuit)
        self.menuData.addAction(self.actionAdd_Entry)
        self.menuData.addAction(self.actionDelete_Entry)
        self.menuData.addAction(self.actionUpdate_Entry)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionEdit_Genres)
        self.menuData.addAction(self.actionConvert_Genres)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionEdit_Media_Types)
        self.menuData.addAction(self.actionConvert_Types)
        self.menuHelp.addAction(self.actionAbout)
        self.menuDisplay_Count_By.addAction(self.actionDisplay_by_Genre)
        self.menuDisplay_Count_By.addAction(self.actionDisplay_by_Type)
        self.menuView.addAction(self.actionClear_UI)
        self.menuView.addAction(self.menuDisplay_Count_By.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.lbl_Title.setBuddy(self.le_title)
        self.lbl_description.setBuddy(self.te_description)
        self.lbl_genre.setBuddy(self.cb_genre)
        self.lbl_season.setBuddy(self.sb_season)
        self.lbl_disc_count.setBuddy(self.sb_disc_count)
        self.lbl_media_type.setBuddy(self.cb_media_type)
        self.lbl_age_rating.setBuddy(self.le_age_rating)
        self.lbl_play_time.setBuddy(self.sb_play_time)
        self.lbl_notes.setBuddy(self.te_notes)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.rb_title, self.rb_description)
        MainWindow.setTabOrder(self.rb_description, self.rb_genre)
        MainWindow.setTabOrder(self.rb_genre, self.rb_notes)
        MainWindow.setTabOrder(self.rb_notes, self.le_title)
        MainWindow.setTabOrder(self.le_title, self.te_description)
        MainWindow.setTabOrder(self.te_description, self.le_age_rating)
        MainWindow.setTabOrder(self.le_age_rating, self.cb_genre)
        MainWindow.setTabOrder(self.cb_genre, self.sb_season)
        MainWindow.setTabOrder(self.sb_season, self.sb_disc_count)
        MainWindow.setTabOrder(self.sb_disc_count, self.cb_media_type)
        MainWindow.setTabOrder(self.cb_media_type, self.sb_play_time)
        MainWindow.setTabOrder(self.sb_play_time, self.te_notes)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Media Database"))
        self.gb_search_bar.setTitle(_translate("MainWindow", "Search &Options:"))
        self.le_search_bar.setPlaceholderText(_translate("MainWindow", "Search for..."))
        self.rb_title.setToolTip(_translate("MainWindow", "Search via entry titles."))
        self.rb_title.setStatusTip(_translate("MainWindow", "Search via entry titles."))
        self.rb_title.setWhatsThis(_translate("MainWindow", "Search via entry titles."))
        self.rb_title.setText(_translate("MainWindow", "&1: Title"))
        self.rb_title.setShortcut(_translate("MainWindow", "Alt+1"))
        self.rb_description.setToolTip(_translate("MainWindow", "Search entries via Description."))
        self.rb_description.setStatusTip(_translate("MainWindow", "Search entries via Description."))
        self.rb_description.setWhatsThis(_translate("MainWindow", "Search entries via Description."))
        self.rb_description.setText(_translate("MainWindow", "&2: Description"))
        self.rb_description.setShortcut(_translate("MainWindow", "Alt+2"))
        self.rb_genre.setToolTip(_translate("MainWindow", "Search entries via Genre."))
        self.rb_genre.setStatusTip(_translate("MainWindow", "Search entries via Genre."))
        self.rb_genre.setWhatsThis(_translate("MainWindow", "Search entries via Genre."))
        self.rb_genre.setText(_translate("MainWindow", "&3: Genre"))
        self.rb_genre.setShortcut(_translate("MainWindow", "Alt+3"))
        self.rb_notes.setToolTip(_translate("MainWindow", "Search entries via Notes."))
        self.rb_notes.setStatusTip(_translate("MainWindow", "Search entries via Notes."))
        self.rb_notes.setWhatsThis(_translate("MainWindow", "Search entries via Notes."))
        self.rb_notes.setText(_translate("MainWindow", "&4: Notes"))
        self.rb_notes.setShortcut(_translate("MainWindow", "Alt+4"))
        self.lbl_entries_count.setText(_translate("MainWindow", "0000: DVDs, 0000: PS4, 0000: PS3, 0000: PS2, 0000: PSVita, 0000: NDS"))
        self.gb_media_titles.setTitle(_translate("MainWindow", "Media T&itles:"))
        self.gb_entries_info.setTitle(_translate("MainWindow", "Media Details:"))
        self.lbl_Title.setText(_translate("MainWindow", "&Title"))
        self.lbl_description.setText(_translate("MainWindow", "&Description"))
        self.lbl_genre.setText(_translate("MainWindow", "&Genre"))
        self.lbl_season.setText(_translate("MainWindow", "&Season"))
        self.lbl_disc_count.setText(_translate("MainWindow", "Disc &Count"))
        self.lbl_media_type.setText(_translate("MainWindow", "&Media Type"))
        self.lbl_age_rating.setText(_translate("MainWindow", "Age &Rating"))
        self.lbl_play_time.setText(_translate("MainWindow", "&Play Time"))
        self.sb_play_time.setSuffix(_translate("MainWindow", " minutes"))
        self.lbl_notes.setText(_translate("MainWindow", "&Notes"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuData.setTitle(_translate("MainWindow", "&Data"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.menuDisplay_Count_By.setTitle(_translate("MainWindow", "Display Count By"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Quit the application."))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Quit the application."))
        self.actionAdd_Entry.setText(_translate("MainWindow", "&Add"))
        self.actionAdd_Entry.setToolTip(_translate("MainWindow", "Add an entry to the database."))
        self.actionAdd_Entry.setStatusTip(_translate("MainWindow", "Add an entry to the database."))
        self.actionAdd_Entry.setShortcut(_translate("MainWindow", "Alt+A"))
        self.actionDelete_Entry.setText(_translate("MainWindow", "Delete"))
        self.actionDelete_Entry.setToolTip(_translate("MainWindow", "Delete an entry from the databse."))
        self.actionDelete_Entry.setStatusTip(_translate("MainWindow", "Delete an entry from the databse."))
        self.actionUpdate_Entry.setText(_translate("MainWindow", "&Update"))
        self.actionUpdate_Entry.setToolTip(_translate("MainWindow", "Update an entry already in the database."))
        self.actionUpdate_Entry.setStatusTip(_translate("MainWindow", "Update an entry already in the database."))
        self.actionUpdate_Entry.setShortcut(_translate("MainWindow", "Alt+U"))
        self.actionEdit_Genres.setText(_translate("MainWindow", "Edit &Genres"))
        self.actionEdit_Genres.setStatusTip(_translate("MainWindow", "Alows the addition and delition of different genres."))
        self.actionEdit_Genres.setShortcut(_translate("MainWindow", "F8"))
        self.actionEdit_Media_Types.setText(_translate("MainWindow", "Edit &Media Types"))
        self.actionEdit_Media_Types.setStatusTip(_translate("MainWindow", "Allows the addition and deletion of different media types."))
        self.actionEdit_Media_Types.setShortcut(_translate("MainWindow", "F10"))
        self.actionDelete_Genre.setText(_translate("MainWindow", "Delete Genre"))
        self.actionDelete_Media_Type.setText(_translate("MainWindow", "Delete Media Type"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionAbout.setToolTip(_translate("MainWindow", "Show application information."))
        self.actionAbout.setStatusTip(_translate("MainWindow", "Show application information."))
        self.actionClear_UI.setText(_translate("MainWindow", "&Clear UI"))
        self.actionClear_UI.setStatusTip(_translate("MainWindow", "Clear UI"))
        self.actionClear_UI.setShortcut(_translate("MainWindow", "Esc"))
        self.actionConvert_Types.setText(_translate("MainWindow", "Convert &Types"))
        self.actionConvert_Types.setShortcut(_translate("MainWindow", "F11"))
        self.actionConvert_Genres.setText(_translate("MainWindow", "Convert Gen&res"))
        self.actionConvert_Genres.setShortcut(_translate("MainWindow", "F9"))
        self.actionDisplay_by_Genre.setText(_translate("MainWindow", "&Genre"))
        self.actionDisplay_by_Genre.setToolTip(_translate("MainWindow", "Display entry count by Genre."))
        self.actionDisplay_by_Genre.setStatusTip(_translate("MainWindow", "Display entry count by Genre."))
        self.actionDisplay_by_Genre.setWhatsThis(_translate("MainWindow", "Display entry count by Genre."))
        self.actionDisplay_by_Type.setText(_translate("MainWindow", "Media &Type"))
        self.actionDisplay_by_Type.setToolTip(_translate("MainWindow", "Display entry count by Media Type."))
        self.actionDisplay_by_Type.setStatusTip(_translate("MainWindow", "Display entry count by Media Type."))
        self.actionDisplay_by_Type.setWhatsThis(_translate("MainWindow", "Display entry count by Media Type."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

