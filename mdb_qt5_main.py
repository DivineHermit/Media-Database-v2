import logging
from logging.handlers import RotatingFileHandler
from PyQt5 import (QtSql, QtWidgets, QtCore)
from mdb_ui_main import Ui_MainWindow
from mdb_ui_edit_genres import Ui_edit_genres_window
from mdb_ui_edit_media_types import Ui_edit_media_types_window
from mdb_ui_entries_converter import Ui_Converter

__author__ = "Dominic Lee"
__module_version__ = __version__ = 0.10

# ----- Logging Configuration -----
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_formatter = logging.Formatter("%(asctime)s|%(name)s|%(levelname)s\n%(message)s\n")

log_handler = RotatingFileHandler("MDB-Qt5.log", maxBytes=100000, backupCount=1)
log_handler.setLevel(logging.ERROR)
log_handler.setFormatter(log_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)

logger.addHandler(log_handler)
logger.addHandler(stream_handler)


class MDB(QtWidgets.QMainWindow):
    f"""
    Media Database PyQt5
    Version: {__version__}
    Author : {__author__}
    """
    # Constants for readability (Used to identify table columns):
    MEDIA_ID, MEDIA_TITLE, MEDIA_DESCRIPTION, MEDIA_AGE_RATING, \
        MEDIA_GENRE, MEDIA_SEASON, MEDIA_DISC_COUNT, MEDIA_TYPE, \
        MEDIA_PLAY_TIME, MEDIA_NOTES = range(10)

    GENRE_ID, GENRE_TITLE, GENRE_DESCRIPTION, GENRE_EXAMPLES = range(4)

    TYPES_ID, TYPES_TITLE = range(2)
    # Constants for Qt settings & readability:
    ASCENDING, DESCENDING = QtCore.Qt.AscendingOrder, QtCore.Qt.DescendingOrder
    ON_ROW_CHANGE = QtSql.QSqlTableModel.OnRowChange
    ON_FIELD_CHANGE = QtSql.QSqlTableModel.OnFieldChange

    def __init__(self, parent=None, database="Media-Database.db"):
        """"""
        super(MDB, self).__init__(parent)
        logger.info("MDB __init__ started...")
        # ===== Creating Database Connection =====
        logger.info("Creating connection to database...")
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(database)
        if not self.db.open():
            QtWidgets.QMessageBox.warning(
                self,
                "Media Database",
                "Error connecting to database:\n{}".format(self.db.lastError().text()),
                QtWidgets.QMessageBox.Ok)
            sys.exit(1)
        self.create_tables()
        logger.info("Connected to {0}: {1}".format(database, self.db.isOpen()))

        # ===== Create Models =====
        logger.info("Creating models...")
        self.model_media = QtSql.QSqlTableModel(self)
        self.configure_model_media()

        self.model_media_proxy = QtCore.QSortFilterProxyModel(self)
        self.configure_model_media_proxy()

        self.model_genres = QtSql.QSqlTableModel(self)
        self.configure_model_genres()

        self.model_types = QtSql.QSqlTableModel(self)
        self.configure_model_types()
        logger.info("Models Done.")

        # ===== Create the UI =====
        logger.info("Creating UI...")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lst_media_list.setModel(self.model_media_proxy)
        self.ui.lst_media_list.setModelColumn(self.MEDIA_TITLE)
        self.ui.cb_genre.setModel(self.model_genres)
        self.ui.cb_genre.setModelColumn(self.GENRE_TITLE)
        self.ui.cb_media_type.setModel(self.model_types)
        self.ui.cb_media_type.setModelColumn(self.TYPES_TITLE)
        # Sub-windows
        self.edit_genres = MDBEditGenres(parent=self)
        self.edit_media_types = MDBEditMediaTypes(parent=self)

        logger.info("UI Done.")

        # ===== Create Widget Mapper =====
        logger.info("Creating widget mapper...")
        self.widget_mapper = QtWidgets.QDataWidgetMapper(self)
        self.configure_widget_mapper()
        logger.info("Mapper Done.")

        # ===== Finally =====
        self.selection = self.ui.lst_media_list.selectionModel()
        self.count_entries_by_type()
        self.create_connections()

        logger.info("MDB __init__ Done.")

    # ===== Configuration Methods =====
    def configure_widget_mapper(self):
        """
        Settings to allow the UI to display entries from the media model.
        :return: True/False depending on success.
        """
        try:
            logger.info("Configuring Widget Mapper Settings...")
            self.widget_mapper.setModel(self.model_media_proxy)
            self.widget_mapper.setSubmitPolicy(QtWidgets.QDataWidgetMapper.AutoSubmit)
            self.widget_mapper.addMapping(self.ui.le_title, self.MEDIA_TITLE)
            self.widget_mapper.addMapping(self.ui.te_description, self.MEDIA_DESCRIPTION)
            self.widget_mapper.addMapping(self.ui.le_age_rating, self.MEDIA_AGE_RATING)
            self.widget_mapper.addMapping(self.ui.cb_genre, self.MEDIA_GENRE)
            self.widget_mapper.addMapping(self.ui.sb_season, self.MEDIA_SEASON)
            self.widget_mapper.addMapping(self.ui.sb_disc_count, self.MEDIA_DISC_COUNT)
            self.widget_mapper.addMapping(self.ui.cb_media_type, self.MEDIA_TYPE)
            self.widget_mapper.addMapping(self.ui.sb_play_time, self.MEDIA_PLAY_TIME)
            self.widget_mapper.addMapping(self.ui.te_notes, self.MEDIA_NOTES)
            self.widget_mapper.toFirst()
            logger.info("Widget Mapper Configuration Done.")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.configure_widget_mapper\n{err}")
            return False

    def configure_model_media(self):
        """
        Setup the models data source and configuration.
        :return: True/False depending on success.
        """
        try:
            logger.info("Configuring media model...")
            self.model_media.setTable("media")
            self.model_media.setEditStrategy(self.ON_ROW_CHANGE)
            self.model_media.sort(self.MEDIA_TITLE, self.ASCENDING)
            self.model_media.select()
            logger.info("Media model configuration done.")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.configure_model_media\n{err}")
            return False

    def configure_model_media_proxy(self):
        """
        Setup the models data source and configuration.
        :return: True/False depending on success.
        """
        try:
            logger.info("Configuring media proxy model...")
            self.model_media_proxy.setSourceModel(self.model_media)
            self.model_media_proxy.sort(self.MEDIA_TITLE, self.ASCENDING)
            self.model_media_proxy.setFilterKeyColumn(self.MEDIA_TITLE)
            self.model_media_proxy.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
            logger.info("Media Proxy model configuration done.")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.configure_model_media_proxy\n{err}")
            return False

    def configure_model_genres(self):
        """
        Setup the models data source and configuration.
        :return: True/False depending on success.
        """
        try:
            logger.info("Configuring genres model...")
            self.model_genres.setTable("genres")
            self.model_genres.sort(self.GENRE_TITLE, self.ASCENDING)
            self.model_media.select()
            logger.info("Genres model configuration done.")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.configure_model_genres\n{err}")
            return False

    def configure_model_types(self):
        """
        Setup the models data source and configuration.
        :return: True/False depending on success.
        """
        try:
            logger.info("Configuring media types model...")
            self.model_types.setTable("media_types")
            self.model_types.sort(self.TYPES_TITLE, self.ASCENDING)
            self.model_media.select()
            logger.info("Media Types model configuration done.")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.configure_model_types\n{err}")
            return False

    def create_connections(self):
        """
        Create Qt Signal/Slot Connections.
        :return: True/False depending on success.
        """
        try:
            logger.info("Creating Qt Signal/Slot Connections...")
            # Search Options:
            self.ui.rb_title.toggled.connect(
                lambda: self.model_media_proxy.setFilterKeyColumn(self.MEDIA_TITLE))
            self.ui.rb_description.toggled.connect(
                lambda: self.model_media_proxy.setFilterKeyColumn(self.MEDIA_DESCRIPTION))
            self.ui.rb_genre.toggled.connect(
                lambda: self.model_media_proxy.setFilterKeyColumn(self.MEDIA_GENRE))
            self.ui.rb_notes.toggled.connect(
                lambda: self.model_media_proxy.setFilterKeyColumn(self.MEDIA_NOTES))
            # File Menu:
            self.ui.actionQuit.triggered.connect(self.closeEvent)
            # View Menu:
            self.ui.actionClear_UI.triggered.connect(self.clear_ui)
            # Data Menu:
            self.ui.actionAdd_Entry.triggered.connect(self.add_entry)
            self.ui.actionDelete_Entry.triggered.connect(self.delete_entry)
            self.ui.actionUpdate_Entry.triggered.connect(self.update_entry)
            self.ui.actionEdit_Genres.triggered.connect(self.show_genres_window)
            # self.ui.actionConvert_Genres.triggered.connect()
            self.ui.actionEdit_Media_Types.triggered.connect(self.show_types_window)
            # self.ui.actionConvert_Types.triggered.connect()
            # Help Menu:
            self.ui.actionAbout.triggered.connect(
                lambda: QtWidgets.QMessageBox.information(
                    self,
                    f"About MDB {__version__}",
                    f"Media Database created by {__author__}\nVersion: {__version__}",
                    QtWidgets.QMessageBox.Ok))
            # Other UI Elements:
            self.ui.le_search_bar.textChanged.connect(self.model_media_proxy.setFilterRegExp)
            self.ui.actionDisplay_by_Type.triggered.connect(lambda: self.display_count(self.ui.actionDisplay_by_Type))
            self.ui.actionDisplay_by_Genre.triggered.connect(lambda: self.display_count(self.ui.actionDisplay_by_Genre))
            self.selection.selectionChanged.connect(self.display_selected_entry)
            logger.info("Qt Connections Done.")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.create_connections\n{err}")
            return False

    # ===== Database Methods =====
    def add_entry(self, event=None):
        """
        Add new entry to the model and set the widget mapper to display it ready for editing.

        :return: True/False depending on success.
        """
        try:
            row = self.model_media.rowCount()
            self.widget_mapper.submit()
            self.model_media.insertRow(row)
            self.widget_mapper.setCurrentIndex(row)
            self.ui.le_title.setFocus()
            logger.info(f"Adding new database entry: {self.ui.le_title.text()}\n"
                        f"New Count: {self.count_all_entries('media')}")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.add_entry\n{err}")
            return False

    def delete_entry(self, event=None):
        """
        Delete currently selected entry.

        :param event:   Used to cover Qts signals.
        :return:        True/False depending on success.
        """
        try:
            logger.info(f"Deleting Entry.")
            delete_entry = QtWidgets.QMessageBox.warning(
                self,
                "Delete MDB Entry?",
                f"Delete selected entry?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if delete_entry == QtWidgets.QMessageBox.Yes:
                self.model_media_proxy.removeRow(self.selection.currentIndex().row())
                return True
        except Exception as err:
            logger.exception(f"Error in MDB.delete_entry\n{err}")
            return False

    def update_entry(self, event=None):
        """"""
        # is this need, won't the model auto update?
        pass

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
            logger.exception(f"Error in MDB.count_all_entries\n{err}")
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
            logger.info(f"MDB.count_entries_by_genre Returning:\n{output.strip(', ')}")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.count_entries_by_genre\n{err}")
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
            logger.info(f"MDB.count_entries_by_type Returning:\n{output.strip(', ')}")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.count_entries_by_type\n{err}")
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
            logger.exception(f"Error in MDB.return_distinct_entries\n{err}")
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
            logger.exception(f"Error in MDB.create_tables\n{err}")
            return False

    # ===== UI Methods =====
    def clear_ui(self, event=None):
        """
        Clear all the UI widgets.

        :return: True/False depending on success.
        """
        # ===== Widgets =====
        try:
            self.ui.le_search_bar.clear()
            self.ui.le_title.clear()
            self.ui.te_description.clear()
            self.ui.le_age_rating.clear()
            self.ui.cb_genre.setCurrentIndex(0)
            self.ui.sb_season.clear()
            self.ui.sb_disc_count.setValue(1)
            self.ui.cb_media_type.setCurrentIndex(0)
            self.ui.sb_play_time.setValue(0)
            self.ui.te_notes.clear()
            # ===== Other Bits =====
            self.widget_mapper.setCurrentIndex(-1)
            self.ui.le_search_bar.setFocus()
            if self.ui.actionDisplay_by_Genre.isChecked():
                self.count_entries_by_genre()
            if self.ui.actionDisplay_by_Type.isChecked():
                self.count_entries_by_type()
            logger.info("UI Cleared.")
            return True
        except Exception as err:
            logger.exception(f"Error in MDB.clear_ui\n{err}")
            return False

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
            logger.exception(f"Error in MDB.display_count\n{err}")
            return False

    def display_selected_entry(self):
        """
        When an item in the media list is selected sends the index
            to the mapper so it can display the entry on the UI.

        :return:    True/False depending on success.
        """
        try:
            self.widget_mapper.setCurrentIndex(self.selection.currentIndex().row())
            return True
        except Exception as err:
            logger.info(f"Error in MDB.display_selected_entry\n{err}")
            return False

    def show_genres_window(self):
        """"""
        self.edit_genres.show()

    def show_types_window(self):
        """"""
        self.edit_media_types.show()

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
            self.db.close()         # Close connection to the database.
            event.accept()          # Quite the program.
        else:
            event.ignore()          # Don't quit the program.


class MDBEditGenres(QtWidgets.QMainWindow):
    """"""
    # Constants for Qt settings & readability:
    GENRE_ID, GENRE_TITLE, GENRE_DESCRIPTION, GENRE_EXAMPLES = range(4)
    ASCENDING, DESCENDING = QtCore.Qt.AscendingOrder, QtCore.Qt.DescendingOrder
    ON_ROW_CHANGE = QtSql.QSqlTableModel.OnRowChange
    ON_FIELD_CHANGE = QtSql.QSqlTableModel.OnFieldChange

    def __init__(self, database="Media-Database.db", parent=None):
        super(MDBEditGenres, self).__init__(parent)
        # ===== Connection to Database =====
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(database)
        # ===== Create UI =====
        self.ui = Ui_edit_genres_window()
        self.ui.setupUi(self)
        # ===== Models =====
        self.model_genres = QtSql.QSqlTableModel(self)
        self.model_genres.setTable("genres")
        self.model_genres.setEditStrategy(self.ON_FIELD_CHANGE)
        self.model_genres.sort(self.GENRE_TITLE, self.ASCENDING)
        self.model_genres.select()
        # ===== Widget Mapper =====
        self.widget_mapper = QtWidgets.QDataWidgetMapper()
        self.widget_mapper.setModel(self.model_genres)
        self.ui.lst_genres.setModel(self.model_genres)
        self.ui.lst_genres.setModelColumn(self.GENRE_TITLE)
        self.widget_mapper.addMapping(self.ui.le_genre_name, self.GENRE_TITLE)
        self.widget_mapper.addMapping(self.ui.te_genre_description, self.GENRE_DESCRIPTION)
        self.widget_mapper.addMapping(self.ui.te_genre_examples, self.GENRE_EXAMPLES)
        # ===== Finally =====
        self.selection = self.ui.lst_genres.selectionModel()
        self.create_connections()

    # ===== Configuration Methods =====
    def create_connections(self):
        """"""
        # ===== Buttons =====
        self.ui.btn_done.clicked.connect(self.closeEvent)
        # ===== Other Elements =====
        self.selection.selectionChanged.connect(self.display_selected_entry)
        return True

    # ===== Database Methods =====
    def add_genre(self):
        """"""
        pass

    def delete_genre(self):
        """"""
        pass

    # ===== UI Methods =====
    def display_selected_entry(self):
        """
        When an item in the list is selected sends the index
            to the mapper so it can display the entry on the UI.

        :return:    True/False depending on success."""
        try:
            self.widget_mapper.setCurrentIndex(self.selection.currentIndex().row())
            return True
        except Exception as err:
            logger.info(f"Error in MDBEditGenres.display_selected_entry\n{err}")
            return False

    # ===== Other Methods =====
    def closeEvent(self, event=None):
        """Overrides close event to just hide the window."""
        self.hide()


class MDBEditMediaTypes(QtWidgets.QMainWindow):
    # TODO: Logging...
    # Constants for Qt settings & readability:
    TYPES_ID, TYPES_TITLE = range(2)
    ASCENDING, DESCENDING = QtCore.Qt.AscendingOrder, QtCore.Qt.DescendingOrder
    ON_ROW_CHANGE = QtSql.QSqlTableModel.OnRowChange
    ON_FIELD_CHANGE = QtSql.QSqlTableModel.OnFieldChange

    def __init__(self, database="Media-Database.db", parent=None):
        super(MDBEditMediaTypes, self).__init__(parent)
        # ===== Connection to Database =====
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(database)
        # ===== Models =====
        self.model_types = QtSql.QSqlTableModel(self)
        self.model_types.setTable("media_types")
        self.model_types.setEditStrategy(self.ON_FIELD_CHANGE)
        self.model_types.sort(self.TYPES_TITLE, self.ASCENDING)
        self.model_types.select()
        # ===== Create UI =====
        self.ui = Ui_edit_media_types_window()
        self.ui.setupUi(self)
        self.ui.lst_media_types.setModel(self.model_types)
        self.ui.lst_media_types.setModelColumn(self.TYPES_TITLE)
        # ===== Widget Mapper =====
        self.widget_mapper = QtWidgets.QDataWidgetMapper(self)
        self.widget_mapper.addMapping(self.ui.le_type_name, self.TYPES_TITLE)
        # ===== Finally =====
        self.selection = self.ui.lst_media_types.selectionModel()
        self.create_connections()

    # ===== Configuration Methods =====
    def create_connections(self):
        """"""
        # ===== Buttons =====
        self.ui.btn_done.clicked.connect(self.closeEvent)
        # ===== Other Elements =====
        self.selection.selectionChanged.connect(self.display_selected_entry)
        return True

    # ===== Database Methods =====
    def add_media_type(self):
        pass

    def delete_media_type(self):
        pass

    # ===== UI Methods =====
    def display_selected_entry(self):
        """
        When an item in the list is selected sends the index
            to the mapper so it can display the entry on the UI.

        :return:    True/False depending on success.
        """
        try:
            self.widget_mapper.setCurrentIndex(self.selection.currentIndex().row())
            return True
        except Exception as err:
            logger.info(f"Error in MDBEditMediaTypes.display_selected_entry\n{err}")
            return False

    # ===== Other Methods =====
    def closeEvent(self, event=None):
        self.hide()


if __name__ == "__main__":
    import sys

    def exception_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)

    sys.excepthook = exception_hook

    app = QtWidgets.QApplication(sys.argv)
    window = MDB()
    window.show()

    sys.exit(app.exec_())
