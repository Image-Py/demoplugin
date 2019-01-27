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
		if IPy.get_ips() is None: return
		IPy.get_ips().img[:] = 255-IPy.get_ips().img
		IPy.get_ips().update()