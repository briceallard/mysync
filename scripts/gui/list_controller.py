import wx
import os
import sys
import time


class list_controller(wx.ListCtrl):

    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, style=wx.LC_REPORT)

        self.InsertColumn(0, 'Filename')
        self.InsertColumn(1, 'Size', wx.LIST_FORMAT_RIGHT)
        self.InsertColumn(2, 'Modified')

        self.SetColumnWidth(0, 240)
        self.SetColumnWidth(1, 80)
        self.SetColumnWidth(2, 240)

        j = 1

        self.InsertItem(0, '..')
        self.SetItemImage(0, 5)

        files = os.listdir('.')

        for i in files:
            name = os.path.basename(i)
            size = os.path.getsize(i)
            modf = os.path.getmtime(i)

            self.InsertItem(j, name)
            self.SetItem(j, 1, str(size) + ' B')
            self.SetItem(j, 2, time.strftime(
                '%Y-%m-%d %H:%M', time.localtime(modf)))

            if j % 2 == 0:
                self.SetItemBackgroundColour(j, '#263238')

            j += 1
