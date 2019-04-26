import os
import sys
import json
from scripts.gui import create_ui as UI
from PyQt5 import QtCore, QtGui, QtWidgets

hosts_path = "./config/hosts.json"


class TreeController(UI.CreateUI, QtWidgets.QMainWindow):
    def __init__(self):
        super(TreeController, self).__init__()
        self.create_ui(self)
        self.on_application_start()
        self.populate_local()
        self.populate_remote()

    def populate_local(self):
        path = '/'
        self.local_model = QtWidgets.QFileSystemModel()
        self.local_model.setRootPath((QtCore.QDir.rootPath()))
        self.local_model.setReadOnly(True)
        self.local_tree.setModel(self.local_model)
        self.local_tree.setRootIndex(self.local_model.index(path))
        self.local_tree.setSortingEnabled(True)
        self.local_tree.setAnimated(True)
        self.local_tree.setSelectionMode(self.local_tree.ExtendedSelection)
        self.local_tree.resizeColumnToContents(1)
        self.local_tree.resizeColumnToContents(2)
        self.local_tree.resizeColumnToContents(3)
        self.local_tree.setColumnWidth(0, 290)
        self.assign_events()

    def populate_remote(self):
        path = '/'
        self.remote_model = QtWidgets.QFileSystemModel()
        self.remote_model.setRootPath((QtCore.QDir.rootPath()))
        self.remote_model.setReadOnly(True)
        self.remote_tree.setModel(self.remote_model)
        self.remote_tree.setRootIndex(self.remote_model.index(path))
        self.remote_tree.setSortingEnabled(True)
        self.remote_tree.setAnimated(True)
        self.remote_tree.setSelectionMode(self.remote_tree.ExtendedSelection)
        self.remote_tree.resizeColumnToContents(1)
        self.remote_tree.resizeColumnToContents(2)
        self.remote_tree.resizeColumnToContents(3)
        self.remote_tree.setColumnWidth(0, 290)

    def sync_to_remote_event_click(self):
        paths = []
        items = self.local_tree.selectionModel().selectedIndexes()

        for item in items:
            if item.column() == 0:
                paths.append(item.model().filePath(item))

        print(paths)

    def sync_to_local_event_click(self):
        paths = []
        items = self.remote_tree.selectionModel().selectedIndexes()

        for item in items:
            if item.column() == 0:
                paths.append(item.model().filePath(item))

        print(paths)

    def hostname_on_change(self):
        global hosts_path

        with open(hosts_path) as f:
            hosts = json.load(f)

            selection = self.hostname.currentText()

            try:
                self.ip_address.setText(hosts[selection]["ip_address"])
                self.ssh_key.setText(hosts[selection]["ssh_path"])
                self.username.setText(hosts[selection]["username"])
            except KeyError:
                self.ip_address.setText("")
                self.ssh_key.setText("")
                self.username.setText("")

    def on_application_start(self):
        global hosts_path

        with open(hosts_path) as f:
            hosts = json.load(f)

            for k in hosts.keys():
                self.hostname.addItem(k)

    def assign_events(self):
        self.sync_to_remote.clicked.connect(self.sync_to_remote_event_click)
        self.hostname.currentTextChanged.connect(self.hostname_on_change)
        self.status_bar.showMessage("Events assigned successfully", 2000)


def main():
    app = QtWidgets.QApplication(sys.argv)
    tc = TreeController()
    tc.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
else:
    main()
