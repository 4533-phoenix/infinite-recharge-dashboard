import os

import wx

class DriverAssistPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.load_standby_image()
        self.build()

    def load_standby_image(self):
        directory = os.path.dirname(__file__)
        filepath = os.path.join(directory, '../assets/war-starscape.png')

        self.image = wx.Image(
            filepath,
            wx.BITMAP_TYPE_PNG
        )

    def build(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.canvas = AutoSizeBitmap(self, self.image)
        self.canvas.SetSize((320, 240))

        sizer.Add(self.canvas, 1, flag=wx.EXPAND)

        self.SetSizer(sizer)


class AutoSizeBitmap(wx.Window):
    """
    A subclass of wx.Window that will hold an image (much like a StaticBitmap),
    but re-size it to fit the current size of the Window
   """
    def __init__(self, parent, image):
        """
        initialize an AutoSizeBitmap
        :param parent: parent Window for this window
        :param image: a wx.Image that you want to display
        """
        super().__init__(parent)

        self.orig_image = image
        self.bitmap = None
        self.prev_size = self.Size

        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnSize(self, evt=None):
        size = self.Size
        if size[0] > 0 and size[1] > 0:
            img = self.orig_image.Copy()
            img.Rescale(*size)
            self.bitmap = img.ConvertToBitmap()
            self.Refresh()

    def OnPaint(self, evt=None):
        dc = wx.PaintDC(self)
        try:
            dc.DrawBitmap(self.bitmap, 0, 0)
        except ValueError:
            pass
