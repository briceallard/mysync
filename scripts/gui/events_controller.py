import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from scripts.gui import create_ui as UI
from scripts.gui import tree_controller as TC


class EventsController(UI.CreateUI, QtWidgets.QMainWindow):
    def __init__(self):
        super(EventsController, self).__init__()

        self.assign_events()

    def event_tree_doubleClick(self, index):
        path = self.sender().model().filePath(index)
        print(path)

    def event_tree_dragEnter(self, index):
        path = self.sender().model().filePath(index)
        print(path)

    def assign_events(self):
        self.local_tree.doubleClicked.connect(self.event_tree_doubleClick)
        self.local_tree.dragEnterEvent.connect(self.event_tree_dragEnter)
        print('Events assigned successfully')
