import wx
import os
from scripts.gui.list_controller import list_controller


class mysync_frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(mysync_frame, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):

        self.splitter = wx.SplitterWindow(self, 300, style=wx.SP_BORDER)
        self.splitter.SetMinimumPaneSize(50)

        p1 = list_controller(self.splitter)
        p2 = list_controller(self.splitter)
        self.splitter.SplitVertically(p1, p2)

        self.Bind(wx.EVT_SIZE, self.splitter_on_size)
        self.Bind(wx.EVT_SPLITTER_DCLICK, self.splitter_on_double_click, id=300)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.splitter, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        sb = self.CreateStatusBar()
        sb.SetStatusText(os.getcwd())

        self.SetSize((1000, 800))
        self.SetTitle('MySync')
        self.Centre()

    def on_quit(self, e):
        self.Close()

    def splitter_on_size(self, e):
        size = self.GetSize()
        self.splitter.SetSashPosition(size.x / 2)

        e.Skip()

    def splitter_on_double_click(self, e):
        size = self.GetSize()
        self.splitter.SetSashPosition(size.x / 2)


def main():
    app = wx.App()
    ex = mysync_frame(None)
    ex.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
