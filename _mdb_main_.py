import logging
from logging.handlers import RotatingFileHandler

from PyQt5 import (QtSql, QtWidgets, QtCore)

from dlg_converter import Ui_dlg_converter
from dlg_edit_genres import Ui_dlg_edit_genres
from dlg_edit_types import Ui_dlg_edit_types
from mdb_ui_main import Ui_MainWindow

__author__ = "Dominic Lee"
__module_version__ = __version__ = 2.20

# ----- Logging Configuration -----
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_formatter = logging.Formatter(
    "%(asctime)s|%(name)s|%(levelname)s\n%(message)s\n")

log_handler = RotatingFileHandler(
    "MDB-Qt5.log", maxBytes=100000, backupCount=1)
log_handler.setLevel(logging.ERROR)
log_handler.setFormatter(log_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)

logger.addHandler(log_handler)
logger.addHandler(stream_handler)


class MDB(QtWidgets.QMainWindow):
    def __init__(self, db_name="Media-Database.db", parent=None):
        super(MDB, self).__init__(parent)
        # ===== Database =====
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(db_name)
        if not self.db.open():
            QtWidgets.QMessageBox.warning(
                self,
                "Media Database",
                "Error connecting to database:\n{}".format(
                    self.db.lastError().text()),
                QtWidgets.QMessageBox.Ok)
            sys.exit(1)

        if self.db.driver().hasFeature(QtSql.QSqlDriver.Transactions):
            logger.info("Database driver can commit and rollback.")
        self.create_tables()

        # ===== Create Models =====
        # main entries model
        self.model_media = QtSql.QSqlTableModel(self)
        self.model_media.setTable("media")
        self.model_media.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model_media.sort(1, QtCore.Qt.AscendingOrder)  # Column 1 is the 'title' column of the 'media' table.
        self.model_media.select()
        # proxy model for search feature.
        self.model_media_proxy = QtCore.QSortFilterProxyModel(self)
        self.model_media_proxy.setSourceModel(self.model_media)
        self.model_media_proxy.sort(1, QtCore.Qt.AscendingOrder)  # Column 1 is the 'title' column of the 'media' table.
        self.model_media_proxy.setFilterKeyColumn(1)
        self.model_media_proxy.setFilterCaseSensitivity(
            QtCore.Qt.CaseInsensitive)
        # genres model
        self.model_genres = QtSql.QSqlTableModel(self)
        self.model_genres.setTable("genres")
        self.model_genres.sort(1, QtCore.Qt.AscendingOrder)  # Column 1 is the 'genre' column of the 'genres' table.
        self.model_genres.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model_genres.select()
        # media types model
        self.model_types = QtSql.QSqlTableModel(self)
        self.model_types.setTable("media_types")
        self.model_types.sort(1, QtCore.Qt.AscendingOrder)  # Column 1 is the 'title' column of the 'media' table.
        self.model_types.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model_types.select()

        # ===== Create the UI =====
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lst_media_list.setModel(self.model_media_proxy)
        self.ui.lst_media_list.setModelColumn(1)  # Column 1 is the 'title' column of the 'media' table.
        self.ui.cb_genre.setModel(self.model_genres)
        self.ui.cb_genre.setModelColumn(1)  # Column 1 is the 'genre' column of the 'genres' table.
        self.ui.cb_media_type.setModel(self.model_types)
        self.ui.cb_media_type.setModelColumn(1)  # Column 1 is the 'type' column of the 'media_types' table.
        # List view selection model
        self.selection = self.ui.lst_media_list.selectionModel()
        # Sub-Windows
        self.ui_edit_genres = MDBEditGenres(self, self.model_genres)  # Give the genres model to the pop-up dialog.
        self.ui_edit_types = MDBEditTypes(self, self.model_types)  # Give the types model to the pop-up dialog.
        self.ui_converter = MDBConverter(self)

        # ===== Create Widget Mapper =====
        self.widget_mapper = QtWidgets.QDataWidgetMapper(self)
        self.widget_mapper.setModel(self.model_media_proxy)
        self.widget_mapper.setSubmitPolicy(QtWidgets.QDataWidgetMapper.AutoSubmit)
        self.widget_mapper.addMapping(self.ui.le_title, 1)  # 'title' column text
        self.widget_mapper.addMapping(self.ui.te_description, 2)  # 'description' column text
        self.widget_mapper.addMapping(self.ui.le_age_rating, 3)  # 'age_rating' column text
        self.widget_mapper.addMapping(self.ui.cb_genre, 4)  # 'genre' column text
        self.widget_mapper.addMapping(self.ui.sb_season, 5)  # 'season' column int
        self.widget_mapper.addMapping(self.ui.sb_disc_count, 6)  # 'disc_count' column int
        self.widget_mapper.addMapping(self.ui.cb_media_type, 7)  # 'media_type' column text
        self.widget_mapper.addMapping(self.ui.sb_play_time, 8)  # 'play_time' column int
        self.widget_mapper.addMapping(self.ui.te_notes, 9)  # 'notes' column text
        self.widget_mapper.toFirst()

        # ===== Display Entry Count =====
        self.count_entries_by_type()

        # ===== Create Signal/Slots =====
        logger.info("Creating Qt Signal/Slot Connections...")
        # Search Options:
        self.ui.rb_title.toggled.connect(
            lambda: self.model_media_proxy.setFilterKeyColumn(1))  # Title Column
        self.ui.rb_description.toggled.connect(
            lambda: self.model_media_proxy.setFilterKeyColumn(2))  # Description Column
        self.ui.rb_genre.toggled.connect(
            lambda: self.model_media_proxy.setFilterKeyColumn(4))  # Genre Column
        self.ui.rb_notes.toggled.connect(
            lambda: self.model_media_proxy.setFilterKeyColumn(9))  # Notes Column
        # File Menu:
        self.ui.actionQuit.triggered.connect(self.closeEvent)
        # View Menu:
        self.ui.actionClear_UI.triggered.connect(self.clear_ui)
        # Data Menu:
        self.ui.actionAdd_Entry.triggered.connect(self.add_entry)
        self.ui.actionDelete_Entry.triggered.connect(self.delete_entry)
        self.ui.actionEdit_Genres.triggered.connect(
            self.show_edit_genres_window)
        # self.ui.actionConvert_Genres.triggered.connect()
        self.ui.actionEdit_Media_Types.triggered.connect(
            self.show_edit_types_window)
        # self.ui.actionConvert_Types.triggered.connect()
        # Help Menu:
        self.ui.actionAbout.triggered.connect(
            lambda: QtWidgets.QMessageBox.information(
                self,
                f"About MDB {__version__}",
                f"Media Database created by {__author__}\nVersion: {__version__}",
                QtWidgets.QMessageBox.Ok))
        # Other UI Elements:
        self.ui.le_search_bar.textChanged.connect(
            self.model_media_proxy.setFilterRegExp)
        self.ui.actionDisplay_by_Type.triggered.connect(
            lambda: self.display_count(self.ui.actionDisplay_by_Type))
        self.ui.actionDisplay_by_Genre.triggered.connect(
            lambda: self.display_count(self.ui.actionDisplay_by_Genre))
        self.selection.selectionChanged.connect(
            self.display_selected_entry)
        logger.info("Qt Connections Done.")

    # ===== Database Methods =====
    def add_entry(self, event=None):
        """
        Add new entry to the model and set the widget mapper to display it ready for editing.

        :return: True/False depending on success.
        """
        try:
            row = self.model_media.rowCount()
            self.widget_mapper.submit()
            self.model_media.insertRows(row, 1)
            self.widget_mapper.toFirst()
            self.clear_ui()
            self.ui.le_title.setFocus()

            self.refresh_count()

            logger.info(f"Adding new media entry.")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.add_entry\n{err}\n")
            return False

    def delete_entry(self, event=None):
        """
        Delete currently selected entry.

        :param event:   Used to cover Qts signals.
        :return:        True/False depending on success.
        """
        try:
            delete_entry = QtWidgets.QMessageBox.warning(
                self,
                "Delete Media Entry?",
                f"Delete entry '{self.ui.le_title.text()}'?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if delete_entry == QtWidgets.QMessageBox.Yes:
                logger.info(f"Deleting media entry: {self.ui.le_title.text()}")
                self.model_media_proxy.removeRow(
                    self.selection.currentIndex().row())
                self.commit_changes()
                self.refresh_count()
                return True
        except Exception as err:
            logger.exception(f"Error in MDB.delete_entry\n{err}\n")
            return False

    def commit_changes(self):
        """
        Commit changes in the models to the database.

        :return: True/False depending on success.
        """
        try:
            self.db.transaction()
            self.model_media.submitAll()
            self.model_genres.submitAll()
            self.model_types.submitAll()
            self.db.commit()  # Save the changes.
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.commit_changes\n{err}\n")
            return False

    def count_all_entries(self, table):
        """
        Uses QSqlQuery to count all entries in the given table.

        :param table: Name of the table to count.
        :return:      An integer value of total entries in 'table' else None.
        """
        try:
            count = QtSql.QSqlQuery(f"SELECT COUNT(*) FROM {table}", self.db)
            count.first()
            logger.info(f"MDB.count_all_entries returning: {count.value(0)}")
            return count.value(0)
        except Exception as err:
            logger.exception(f"Error in MDB.count_all_entries\n{err}\n")
            return None

    def count_entries_by_genre(self):
        """
        Counts all distinct genres in the database and then
            counts the entries with that genre.

        :return: True/False depending on success.
        """
        try:
            output = f"Total Media Count: {self.count_all_entries('media')}\nCount By Genre:\n"
            genres = self.return_distinct_entries("media", "genre")

            while genres.next():
                count = QtSql.QSqlQuery(
                    f"SELECT COUNT(*) FROM media WHERE genre = '{genres.value(0)}'",
                    self.db)
                count.first()
                output += f"{genres.value(0)}: {count.value(0)}, "
            # Set label text directly or return it and set by another method?
            self.ui.lbl_entries_count.setText(output.strip(", "))
            # return output.strip(", ")
            logger.info(
                f"MDB.count_entries_by_genre Returning:\n{output.strip(', ')}")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.count_entries_by_genre\n{err}\n")
            return False

    def count_entries_by_type(self):
        """
        Counts all distinct media types in the database and then
            counts the entries with that type.

        :return: True/False depending on success.
        """
        try:
            output = f"Total Media Count: {self.count_all_entries('media')}\nCount By Type:\n"
            types = self.return_distinct_entries("media", "media_type")

            while types.next():
                count = QtSql.QSqlQuery(
                    f"SELECT COUNT(*) FROM media WHERE media_type = '{types.value(0)}'",
                    self.db)
                count.first()
                output += f"{types.value(0)}: {count.value(0)}, "
            # Set label text directly or return it and set by another method?
            self.ui.lbl_entries_count.setText(output.strip(", "))
            # return output.strip(", ")
            logger.info(
                f"MDB.count_entries_by_type Returning:\n{output.strip(', ')}")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.count_entries_by_type\n{err}\n")
            return False

    def return_distinct_entries(self, table, column):
        """
        Create a QSqlQuery object for distinct entries in 'table' & 'column'.

        :param table:   Name of the database table.
        :param column:  Name of the column in 'table'.
        :return:        Returns a QSqlQuery object for iteration else None.
        """
        try:
            logger.info(f"MDB.return_distinct_entries({table}, {column})")
            query = QtSql.QSqlQuery(
                f"SELECT DISTINCT {column} FROM {table} ORDER BY {column}", self.db)
            query.exec_()
            return query
        except Exception as err:
            logger.exception(f"Error in MDB.return_distinct_entries\n{err}\n")
            return None

    def create_tables(self):
        """
        Creates the database tables if they don't already exist.

        :return: True/False depending on success.
        """
        try:
            media_types = QtSql.QSqlQuery(
                """CREATE TABLE IF NOT EXISTS media_types (
                        id INTEGER PRIMARY KEY NOT NULL,
                        type VARCHAR)""", self.db)
            media_types.exec_()

            genres = QtSql.QSqlQuery(
                """CREATE TABLE IF NOT EXISTS genres (
                    id INTEGER PRIMARY KEY,
                    genre VARCHAR,
                    description VARCHAR,
                    examples VARCHAR)""")
            genres.exec_()

            media = QtSql.QSqlQuery(
                """CREATE TABLE IF NOT EXISTS media (
                    id INTEGER PRIMARY KEY,
                    title VARCHAR NOT NULL,
                    description VARCHAR,
                    age_rating VARCHAR,
                    genre VARCHAR,
                    season INTEGER,
                    disc_count INTEGER,
                    media_type VARCHAR,
                    play_time INTEGER,
                    notes VARCHAR)""")
            media.exec_()
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.create_tables\n{err}\n")
            return False

    # ===== UI Methods =====
    def clear_ui(self):
        """
        Clear the UI and widget mapper and refresh the display count.

        :return: True/False depending on success.
        """
        try:
            self.selection.clearSelection()
            self.widget_mapper.setCurrentIndex(-1)

            self.ui.le_search_bar.clear()
            self.ui.le_search_bar.setFocus()

            self.ui.le_title.clear()
            self.ui.te_description.clear()
            self.ui.le_age_rating.clear()
            self.ui.cb_genre.setCurrentIndex(0)
            self.ui.sb_season.setValue(0)
            self.ui.sb_disc_count.setValue(0)
            self.ui.cb_media_type.setCurrentIndex(0)
            self.ui.sb_play_time.setValue(0)
            self.ui.te_notes.clear()

            self.refresh_count()
        except Exception as err:
            logger.exception(f"Error in MDB.clear_ui\n{err}\n")

    def display_count(self, sender):
        """
        Used to select what count method is displayed.

        :param sender:  Which menu item triggered the method call.
        :return:        True/False depending on success.
        """
        try:
            if sender is self.ui.actionDisplay_by_Genre:
                logger.info("Displaying entry count by Genre.")
                self.ui.actionDisplay_by_Genre.setChecked(True)
                self.ui.actionDisplay_by_Type.setChecked(False)
                self.count_entries_by_genre()
            if sender is self.ui.actionDisplay_by_Type:
                logger.info("Displaying entry count by Media Type.")
                self.ui.actionDisplay_by_Genre.setChecked(False)
                self.ui.actionDisplay_by_Type.setChecked(True)
                self.count_entries_by_type()
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.display_count\n{err}\n")
            return False

    def display_selected_entry(self):
        """"""
        self.widget_mapper.setCurrentIndex(self.selection.currentIndex().row())
        self.refresh_count()
        return True

    def refresh_count(self):
        """
        Check to see what display count is being used and call the
        appropriate method to update the UI.

        :return: True/ False depending on success.
        """
        try:
            if self.ui.actionDisplay_by_Genre.isChecked():
                self.count_entries_by_genre()
            if self.ui.actionDisplay_by_Type.isChecked():
                self.count_entries_by_type()
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.refresh_count\n{err}\n")

    def show_converter_window(self):
        self.ui_converter.show()
        return True

    def show_edit_genres_window(self):
        self.ui_edit_genres.show()
        return True

    def show_edit_types_window(self):
        self.ui_edit_types.show()
        return True

    # ===== Other Methods =====
    def __str__(self):
        """"""
        count = self.count_all_entries("media")
        return f"Media Database powered by PyQt5\nDatabase has {count} entries."

    def closeEvent(self, event=None):
        """Overrides close event with custom quit message box."""
        choice = QtWidgets.QMessageBox.question(
            self, "Quit?", "Quit the program?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            self.commit_changes()
            logger.info(f"Programme quitting, last error:\n{self.db.lastError().text()}\n")
            self.db.close()  # Close connection to the database.
            event.accept()  # Quite the program.
        else:
            event.ignore()  # Don't quit the program.


class MDBEditGenres(QtWidgets.QDialog):
    def __init__(self, parent=None, model=None):
        super(MDBEditGenres, self).__init__(parent)
        # ===== Set-up Model =====
        if model is None:
            # This should never be seen.
            QtWidgets.QMessageBox.critical(
                self,
                "Model Error",
                "No model passed to edit genres dialog.",
                QtWidgets.QMessageBox.Ok)
        else:
            self.model_genres = model

        # ===== Set-up UI =====
        self.ui = Ui_dlg_edit_genres()
        self.ui.setupUi(self)
        self.ui.lst_genres.setModel(self.model_genres)
        self.ui.lst_genres.setModelColumn(1)  # 1 is 'genre' column of the 'genres' table.
        # List view selection model
        self.selection = self.ui.lst_genres.selectionModel()

        # ===== Create Widget Mapper =====
        self.widget_mapper = QtWidgets.QDataWidgetMapper(self)
        self.widget_mapper.setModel(self.model_genres)
        self.widget_mapper.setSubmitPolicy(QtWidgets.QDataWidgetMapper.AutoSubmit)
        self.widget_mapper.addMapping(self.ui.le_genre_name, 1)
        self.widget_mapper.addMapping(self.ui.te_genre_description, 2)
        self.widget_mapper.addMapping(self.ui.te_genre_examples, 3)

        # ===== Create Signal/Slots =====
        self.selection.selectionChanged.connect(self.display_selected_entry)
        # Buttons
        self.ui.btn_add_genre.clicked.connect(self.add_genre)
        self.ui.btn_delete_genre.clicked.connect(self.delete_genre)
        self.ui.btn_done.clicked.connect(lambda: self.hide())

    # ===== Database Methods =====
    def add_genre(self):
        """
        Add a new genre entry.

        :return: True/False depending on success.
        """
        try:
            row = self.model_genres.rowCount()
            self.widget_mapper.submit()
            self.model_genres.insertRows(row, 1)
            self.widget_mapper.toFirst()
            self.clear_ui()
            self.ui.le_genre_name.setFocus()
            logger.info("Adding new genre.")
            return True
        except Exception as err:
            logger.exception(f"Error in MDBEditGenres.add_genre\n{err}\n")
            return False

    def delete_genre(self):
        """"""
        try:
            delete_entry = QtWidgets.QMessageBox.warning(
                self,
                "Delete Genre?",
                f"Delete genre '{self.ui.le_genre_name.text()}'?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if delete_entry == QtWidgets.QMessageBox.Yes:
                logger.info(f"Deleting genre: {self.ui.le_genre_name.text()}")
                self.model_genres.removeRow(
                    self.selection.currentIndex().row())
            return True
        except Exception as err:
            logger.exception(f"Error in MDBEditGenre.delete_genre\n{err}\n")
            return False

    # ===== UI Methods =====
    def clear_ui(self):
        """"""
        self.selection.clearSelection()
        self.ui.le_genre_name.clear()
        self.ui.te_genre_description.clear()
        self.ui.te_genre_examples.clear()

    def display_selected_entry(self):
        self.widget_mapper.setCurrentIndex(self.selection.currentIndex().row())
        return True

    # ===== Other Methods =====
    def closeEvent(self, event=None):
        """"""
        self.model_genres.submitAll()
        self.hide()


class MDBEditTypes(QtWidgets.QDialog):
    def __init__(self, parent=None, model=None):
        super(MDBEditTypes, self).__init__(parent)
        # ===== Set-up Model =====
        if model is None:
            # This should never be seen.
            QtWidgets.QMessageBox.critical(
                self,
                "Model Error",
                "No model passed to edit types dialog.",
                QtWidgets.QMessageBox.Ok)
        else:
            self.model_types = model

        # ===== Set-up UI =====
        self.ui = Ui_dlg_edit_types()
        self.ui.setupUi(self)
        self.ui.lst_media_types.setModel(self.model_types)
        self.ui.lst_media_types.setModelColumn(1)  # 1 is 'type' column of the 'media_types' table.
        # Selection model
        self.selection = self.ui.lst_media_types.selectionModel()

        # ===== Create Signal/Slots =====
        self.ui.btn_done.clicked.connect(self.closeEvent)
        self.ui.btn_add_type.clicked.connect(self.add_type)
        self.ui.btn_delete_type.clicked.connect(self.delete_type)

    # ===== Database Methods =====
    def add_type(self):
        """"""
        try:
            row = self.model_types.rowCount()
            self.model_types.insertRows(row, 1)
            return True
        except Exception as err:
            logger.exception(f"Error in MDBEditTypes.delete_type\n{err}\n")
            return False

    def delete_type(self):
        try:
            delete_entry = QtWidgets.QMessageBox.warning(
                self,
                "Delete Media Type?",
                f"Delete media type?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if delete_entry == QtWidgets.QMessageBox.Yes:
                logger.info(f"Deleting media type?")
                self.model_types.removeRow(
                    self.selection.currentIndex().row())
                return True
        except Exception as err:
            logger.exception(f"Error in MDBEditTypes.delete_type\n{err}\n")
            return False

    # ===== Other Methods =====
    def closeEvent(self, event=None):
        """"""
        self.model_types.submitAll()
        self.hide()


class MDBConverter(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MDBConverter, self).__init__(parent)
        self.ui = Ui_dlg_converter()
        self.ui.setupUi(self)
        # ===== Create Widget Mapper =====
        # ===== Create Signal/Slots =====


if __name__ == "__main__":
    import sys


    def exception_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)


    sys.excepthook = exception_hook

    app = QtWidgets.QApplication(sys.argv)
    # Leave empty 'MDB()' for default 'Media-Database.db'
    # or supply database name 'MDB('TEST.db')' to access or create.
    window = MDB()
    window.show()

    sys.exit(app.exec_())
