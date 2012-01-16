'''
Created on 12 janv. 2012

@author: Olivier
'''
from gui.RobotGUI import RobotGUI
import wx
from gui.Robot import Robot

class RobotGUIManager(RobotGUI):
    '''
    The Main windows of the Robot software
    '''
    def __init__(self, parent):
        '''
        Constructor
        '''
        RobotGUI.__init__(self, parent)
        self.__mConnected = False
        self.__mRobot = Robot()
        
    
    def OnConnect(self, event):
        self.__mConnected = event.IsChecked()
        if self.__mConnected:
            self.__mRobot.Connect()
        else:
            self.__mRobot.Disconnect()
        
    def OnQuit(self, event):
        exit()
    
    def OnChar(self, event):
        if self.__mConnected:
            key = event.GetKeyCode()
            if key == 90: #Z
                self._mDrawPanel.SetY(self._mDrawPanel.GetY()-1)
                print "up"
            if key == 83: #S
                self._mDrawPanel.SetY(self._mDrawPanel.GetY()+1)
                print "down"
            if key == 81: #Q
                self._mDrawPanel.SetX(self._mDrawPanel.GetX()-1)
                print "left"
            if key == 68: #D
                self._mDrawPanel.SetX(self._mDrawPanel.GetX()+1)
                print "right"
                
    def OnMotion(self, event):
        if self.__mConnected:
            self._mDrawPanel.SetY(event.GetY())
            self._mDrawPanel.SetX(event.GetX())
    
def main():
    app = wx.PySimpleApp()
    frame = RobotGUIManager(None)
    frame.Fit()
    frame.Show()
    app.MainLoop()
    
if __name__ == '__main__':
    main()