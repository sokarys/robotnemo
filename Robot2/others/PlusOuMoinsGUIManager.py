'''
Created on 24 janv. 2012

@author: Olivier
'''
from others.PlusOuMoinsGUI import PlusOuMoinsGUI
from random import randint
import wx



class PlusOuMoinsGUIManager(PlusOuMoinsGUI):
    '''
    Game More or Less with a GUI!
    '''

    def __init__(self,parent):
        '''
        Constructor
        '''
        PlusOuMoinsGUI.__init__(self, parent) #Parent init
        self.__mEntre = 0  #the user number 
        self.__mCounter = 0 #the number of try
        self.OnGenerer(None) #create a new number at find
        
    def OnVerif(self, event):
        """
        Event when press the button _mVerifier
        """
        try:
            self.__mEntre = int(self._mTextEnter.GetValue()) #get the value of the number from the text field
            self.__mCounter = self.__mCounter + 1 #add 1 to the counter
        except:
            self._mMessage.SetLabel("Please enter a number between 1 and 100.")
            
        if self.__mMystere < self.__mEntre :
            self._mMessage.SetLabel(str(self.__mCounter) + " : Moins") #modify the Label with the good message
        elif self.__mMystere > self.__mEntre :
            self._mMessage.SetLabel(str(self.__mCounter) + " : Plus")
        else :
            self._mMessage.SetLabel(str(self.__mCounter) + " : You Win")
        
    
    def OnGenerer(self, event):
        """
        Event when press the button _mGenerer
        """
        self.__mMystere = randint(1, 100) #generate a random int between 1 and 100
        self.__mCounter = 0 #set the try counter at 0
        self._mMessage.SetLabel("Nombre generer")
    
    def OnSolution(self, event):
        """
        Event when press the button _mSolution
        """
        self._mMessage.SetLabel("Le nombre est : " + str(self.__mMystere))
        

def main():
    """
    Run the main GUI
    """
    app = wx.PySimpleApp()
    frame = PlusOuMoinsGUIManager(None)
    frame.Fit()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__" :
    """
    Call the function to start the main program 
    """
    main()
    
    
    
    