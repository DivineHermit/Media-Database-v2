# Media-Database-v2
This is a remake of Media Database v1 that uses PyQt5's model/view code style.

Making use of:
  QtCore.QSortFilterProxyModel()
  QtSql.QSqlDatabase.addDatabase("QSQLITE")
  QtSql.QSqlTableModel()
  QtWidgets.QDataWidgetMapper()

The UI has been modified slightly due to changes in the way some of the MDB-v1 features now work (e.g. the search feature now uses QSortFilterProxyModel while the MDB-v1 used an SQL query or the database).
