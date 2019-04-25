import os
import sys
from scripts.gui import create_ui as UI
from PyQt5 import QtCore, QtGui, QtWidgets


class TreeController(UI.CreateUI, QtWidgets.QMainWindow):
    def __init__(self):
        super(TreeController, self).__init__()
        self.create_ui(self)
        self.populate_local()
        self.populate_remote()

    def populate_local(self):
        path = '/'
        self.local_model = QtWidgets.QFileSystemModel()
        self.local_model.setRootPath((QtCore.QDir.rootPath()))
        self.local_tree.setModel(self.local_model)
        self.local_tree.setRootIndex(self.local_model.index(path))
        self.local_tree.setSortingEnabled(True)
        self.local_tree.setAnimated(True)
        self.local_tree.setDragEnabled(True)
        self.local_tree.setAcceptDrops(True)
        self.local_tree.resizeColumnToContents(1)
        self.local_tree.resizeColumnToContents(2)
        self.local_tree.resizeColumnToContents(3)
        self.local_tree.setColumnWidth(0, 175)

    def populate_remote(self):
        path = '/'
        self.remote_model = QtWidgets.QFileSystemModel()
        self.remote_model.setRootPath((QtCore.QDir.rootPath()))
        self.remote_tree.setModel(self.remote_model)
        self.remote_tree.setRootIndex(self.remote_model.index(path))
        self.remote_tree.setSortingEnabled(True)
        self.remote_tree.setAnimated(True)
        self.remote_tree.setDragEnabled(True)
        self.remote_tree.setAcceptDrops(True)
        self.remote_tree.resizeColumnToContents(1)
        self.remote_tree.resizeColumnToContents(2)
        self.remote_tree.resizeColumnToContents(3)
        self.remote_tree.setColumnWidth(0, 175)


def main():
    app = QtWidgets.QApplication(sys.argv)
    tc = TreeController()
    tc.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
else:
    main()
