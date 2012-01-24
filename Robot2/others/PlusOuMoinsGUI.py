# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec  2 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class PlusOuMoinsGUI
###########################################################################

class PlusOuMoinsGUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Jeu du plus ou moins", pos = wx.DefaultPosition, size = wx.Size( 574,448 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nombre : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self._mTextEnter = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self._mTextEnter, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self._mVerifier = wx.Button( self, wx.ID_ANY, u"Verifier", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self._mVerifier, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self._mGenerer = wx.Button( self, wx.ID_ANY, u"Generer un nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self._mGenerer, 0, wx.ALL, 5 )
		
		self._mButtonSolution = wx.Button( self, wx.ID_ANY, u"Voir Solution", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self._mButtonSolution, 0, wx.ALL, 5 )
		
		bSizer1.Add( bSizer3, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self._mMessage = wx.StaticText( self, wx.ID_ANY, u"Resultat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._mMessage.Wrap( -1 )
		bSizer2.Add( self._mMessage, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self._mVerifier.Bind( wx.EVT_BUTTON, self.OnVerif )
		self._mGenerer.Bind( wx.EVT_BUTTON, self.OnGenerer )
		self._mButtonSolution.Bind( wx.EVT_BUTTON, self.OnSolution )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnVerif( self, event ):
		event.Skip()
	
	def OnGenerer( self, event ):
		event.Skip()
	
	def OnSolution( self, event ):
		event.Skip()
	

