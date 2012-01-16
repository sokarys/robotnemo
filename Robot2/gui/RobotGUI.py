# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec  2 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from DrawPanel import DrawPanel

ID_CONNECT = 1000
ID_QUIT = 1001

###########################################################################
## Class RobotGUI
###########################################################################

class RobotGUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 800,800 ), wx.Size( 800,800 ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.connect = wx.MenuItem( self.file, ID_CONNECT, u"Connect", wx.EmptyString, wx.ITEM_CHECK )
		self.file.AppendItem( self.connect )
		
		self.file.AppendSeparator()
		
		self.quit = wx.MenuItem( self.file, ID_QUIT, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.quit )
		
		self.m_menubar1.Append( self.file, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self._mStatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self._mDrawPanel = DrawPanel(self)
		bSizer1.Add( self._mDrawPanel, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.OnConnect, id = self.connect.GetId() )
		self.Bind( wx.EVT_MENU, self.OnQuit, id = self.quit.GetId() )
		self._mDrawPanel.Bind( wx.EVT_KEY_DOWN, self.OnChar )
		self._mDrawPanel.Bind( wx.EVT_MOTION, self.OnMotion )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnConnect( self, event ):
		event.Skip()
	
	def OnQuit( self, event ):
		event.Skip()
	
	def OnChar( self, event ):
		event.Skip()
	
	def OnMotion( self, event ):
		event.Skip()
	

