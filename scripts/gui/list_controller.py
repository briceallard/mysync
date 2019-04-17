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
        self.SetColumnWidth(2, 180)

        images = ['images/icon_folder.png',
                  'images/icon_file.png',
                  'images/icon_back.png']

        self.il = wx.ImageList(16, 16)

        for i in images:
            self.il.Add(wx.Bitmap(i))

        self.SetImageList(self.il, wx.IMAGE_LIST_SMALL)

        j = 1

        self.InsertItem(0, '..')
        self.SetItemImage(0, 2)

        files = os.listdir('.')

        for i in files:
            name = os.path.basename(i)
            size = os.path.getsize(i)
            modf = os.path.getmtime(i)

            self.InsertItem(j, name)
            self.SetItem(j, 1, str(size) + ' B')
            self.SetItem(j, 2, time.strftime(
                '%Y-%m-%d %H:%M', time.localtime(modf)))

            if os.path.isdir(i):
                self.SetItemImage(j, 0)
            else:
                self.SetItemImage(j, 1)

            if j % 2 == 0:
                self.SetItemBackgroundColour(j, '#263238')

            j += 1
