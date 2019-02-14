# Widget Plugin

The Widget plugin is loaded as a panel, which is a actually a ui object that inherits from `wx.Panel`, this gives us a lot of free space, but at the cost of not being able to isolate the UI, we must write `wxpython` code directly. For example, the navigation bar on the right side, the eagle eye is extended by the `widget`, and the Macro recorder that I have seen before is also a `widget`.

## Widget Demo

```python
from imagepy import IPy
import wx

class Plugin ( wx.Panel ):
    title = 'Widget Demo'
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent)
        sizer = wx.BoxSizer( wx.VERTICAL )
        self.lable = wx.StaticText( self, wx.ID_ANY, 'This is a widgets demo')
        self.lable.Wrap( -1 )
        sizer.Add( self.lable, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        self.btn_invert = wx.Button( self, wx.ID_ANY, 'Invert curent image')
        sizer.Add( self.btn_invert, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.SetSizer( sizer )
        self.Layout()
        self.Fit()
        # Connect Events
        self.btn_invert.Bind( wx.EVT_BUTTON, self.on_invert)

    def on_invert(self, event):
        ips = IPy.get_ips()
        if ips is None: return
        ips.img[:] = 255-ips.img
        ips.update()
```

Since `wxpython` has more content itself, if you need to write your own `widget`, you will inevitably learn systematically about `wxpython`. Here is just a simple example.

![14](http://idoc.imagepy.org/demoplugin/27.png)

<div align=center>widget</div><br>

**widget loading method**

1. The file end with `_wgt.py`, the class name must be called `Plugin`, inherited from `wx.Panel`(one file can only implement one widget)
2. The file can be located in the first level submenu under the `widgets` directory, and will be loaded into the right component bar according to the level when starting. It can also be located under menus or its submenus, which loads the panel as a floating window when the user clicks on the menu.

![14](http://idoc.imagepy.org/demoplugin/26.png)

<div align=center>Widget Demo</div><br>

## Widget opterating mechanism

Widgets are essentially a subclass of `wx.Panel`. There must be a `title` field as the plugin name. Others are `wxpython` programming. By writing the `UI` and adding events, we don't discuss it in detail here.
