import os
import sys
import json
from scripts.gui import create_ui as UI
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from sync_tools import sync_tool

hosts_path = "./config/hosts.json"


class TreeController(UI.CreateUI, QtWidgets.QMainWindow):
    def __init__(self):
        super(TreeController, self).__init__()

        self.create_ui(self)
        self.on_application_start()
        self.populate_local()
        self.connected = False

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
        path = self.sync.user.get_local_remote_mount()
        self.remote_model = QtWidgets.QFileSystemModel()
        self.remote_model.setRootPath(path)
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
        self.assign_events()

    def on_refresh_click(self):
        self.populate_remote()

    def sync_to_remote_event_click(self):
        paths = []
        items = self.local_tree.selectionModel().selectedIndexes()

        for item in items:
            if item.column() == 0:
                paths.append(item.model().filePath(item))

        print(paths)
        for path in paths:
            self.sync.push_to_server(path)

        self.on_refresh_click()
        self.status_bar.showMessage("File Transfer Complete", 3000)

    def sync_to_local_event_click(self):
        local_paths = []
        remote_paths = []
        local_items = self.local_tree.selectionModel().selectedIndexes()
        remote_items = self.remote_tree.selectionModel().selectedIndexes()

        for item in local_items:
            if item.column() == 0:
                local_paths.append(item.model().filePath(item))

        for item in remote_items:
            if item.column() == 0:
                remote_paths.append(item.model().filePath(item))

        print(remote_paths)
        for remote_path in remote_paths:
            for local_path in local_paths:
                self.sync.pull_from_server(remote_path, local_path)

        self.on_refresh_click()
        self.status_bar.showMessage("File Transfer Complete", 3000)

    def hostname_on_change(self):
        global hosts_path

        with open(hosts_path) as f:
            hosts = json.load(f)

            selection = self.hostname.currentText()

            try:
                self.ip_address.setText(hosts[selection]["server_ip"])
                self.ssh_key.setText(hosts[selection]["ssh_path"])
                self.username.setText(hosts[selection]["user_name"])
            except KeyError:
                self.ip_address.setText("")
                self.ssh_key.setText("")
                self.username.setText("")

    def on_connect_click(self):
        if not self.connected:
            self.sync = sync_tool()
            self.sync.mount_remote_server()
            self.connect.setText('Disconnect')
            self.populate_remote()
            self.connected = True
            self.status_bar.showMessage("Connection Successful", 3000)

        elif self.connected:
            self.sync.unmount_remote_directory()
            self.connect.setText('Connect')
            self.connected = False
            self.status_bar.showMessage("Connection Failed", 3000)

        else:
            print('Erroooooor')

    def on_application_start(self):
        global hosts_path

        with open(hosts_path) as f:
            hosts = json.load(f)

            for k in hosts.keys():
                self.hostname.addItem(k)

    def assign_events(self):
        self.sync_to_remote.clicked.connect(self.sync_to_remote_event_click)
        self.sync_to_local.clicked.connect(self.sync_to_local_event_click)
        self.refresh.clicked.connect(self.on_refresh_click)
        self.hostname.currentTextChanged.connect(self.hostname_on_change)
        self.connect.clicked.connect(self.on_connect_click)
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
