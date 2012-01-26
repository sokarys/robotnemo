'''
Created on 12 janv. 2012

@author: Olivier
'''
import wx

class DrawPanel(wx.Panel):
    '''
    The draw panel to see the move of the robot
    '''
    
    def __init__(self, parent):
        '''
        Constructor
        '''
        wx.Panel.__init__(self, parent)
        
        #Position of the robot
        self.__mX = 0
        self.__mY = 0
        self.__mGyro = 0
        self.__mAccelero = 0
        self.__mText = ""
        wx.EVT_PAINT(self, self.OnPaint)
        

    def OnPaint(self, event):
        """the paint event, what we paint when refresh"""
        inDc = wx.PaintDC(self)
        inDc.Clear()
        inDc.BeginDrawing()
        self.DrawBotom(inDc)
        self.DrawRobot(inDc)
        self.DrawTest(inDc)
        inDc.EndDrawing()
        
        
    def DrawBotom(self, inDc):
        """Draw the table where the robot move"""
        inDc.SetPen(wx.Pen("red", 10))
        inDc.DrawRectangle(0,0,600,600)
    
    def DrawRobot(self, inDc):
        """"Draw the robot and use mX and mY"""
        inDc.SetPen(wx.Pen("black", 2))
        inDc.DrawCircle(self.__mX, self.__mY, 20)
    
    """GETTERS AND SETTERS"""
    def GetX(self):
        return self.__mX

    def GetY(self):
        return self.__mY
    
    def DrawTest(self, inDc):
        inDc.DrawText(self.__mText,10,10)
        
    def SetX(self, value):
        self.__mX = value
        self.Refresh()

    def SetY(self, value):
        self.__mY = value
        self.Refresh()
    