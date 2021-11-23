# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer1.SetMinSize( wx.Size( 0,-1 ) )
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"                           Vælg antal holdmedlemmer", wx.Point( 100,-1 ), wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Skriv jeres holdnavn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.HoldNavnBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.HoldNavnBox, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		AntalMedlemmerBoxChoices = [ u"3", u"4" ]
		self.AntalMedlemmerBox = wx.ComboBox( self, wx.ID_ANY, u"4", wx.Point( 50,-1 ), wx.DefaultSize, AntalMedlemmerBoxChoices, 0 )
		self.AntalMedlemmerBox.SetSelection( 1 )
		bSizer2.Add( self.AntalMedlemmerBox, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Skriv navne på holdmedlemmer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.Navn1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.Navn1, 0, wx.ALL, 5 )

		self.Navn2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.Navn2, 0, wx.ALL, 5 )

		self.Navn3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.Navn3, 0, wx.ALL, 5 )

		self.Navn4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.Navn4, 0, wx.ALL, 5 )

		self.GemNavneKnap = wx.Button( self, wx.ID_ANY, u"Gem Navne", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.GemNavneKnap, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.AntalMedlemmerBox.Bind( wx.EVT_COMBOBOX, self.HideOrShow )
		self.GemNavneKnap.Bind( wx.EVT_BUTTON, self.GemNavne )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HideOrShow( self, event ):
		event.Skip()

	def GemNavne( self, event ):
		event.Skip()


