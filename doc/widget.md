# <span id = "Widget">Widget</span>

Widget插件加载为一块面板，其实是继承与wx.Panel的一个ui对象，这给了我们非常大的自由空间，但代价是，我们无法隔绝UI，必须直接编写wxpython代码。例如右侧的导航栏，鹰眼就是widget扩展出的，而之前见到过的宏录制器同样也是widget。



## <span id = "画笔工具">画笔工具</span>

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

由于wxpython的内容本身比较多，如有必要自己编写widget，那么免不了对wxpython进行系统性学习，这里仅仅给出一个最简单的例子。



**widget的加载方式**

1. 文件必须以_wgt.py结尾，类名必须叫Plugin，继承于wx.Panel（一个文件只能实现一个工具）
2. 文件可以位于widgets目录下的一级子菜单内，启动时会按照层级加载到右侧组件栏。也可以位于menus或其子菜单下，当用户点击菜单时加载面板。



## <span id = "Tool的运行机制">Tool的运行机制</span>

widgets本质上就是一个wx.Panel的子类，必须有title字段作为插件名称，其他的，就是wxpython编程，这里不做详细讨论。

**mouse_down(self, ips, x, y, btn, ******key):** 鼠标按下时触发，ips是当前作用图像的ImagePlus封装类，可以通过ips.img获取当前图像，也可以ips.lut, ips.roi, ips.unit获取图像的索引表，roi，比例尺和单位等附加信息。x, y是当前鼠标在数据坐标系下的位置，btn触发事件的鼠标按键，0:无，1:左键，2:中键，3:右键。可以通过key['alt'], key['ctrl'], key['shift']获取相应功能键是否按下，通过key['canvas']获取触发事件的Canvas对象。

**mouse_up(self, ips, x, y, btn, ******key):** 鼠标抬起时触发，具体参数与mouse_down相同。

**mouse_move(self, ips, x, y, btn, ******key):** 鼠标移动时触发，具体参数与mouse_down相同。

**mouse_wheel(self, ips, x, y, btn, ******key):** 鼠标滚轮滚动时触发，具体参数与mouse_down相同。

