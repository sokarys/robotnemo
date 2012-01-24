'''
Created on 16 janv. 2012

@author: boulange
'''

  
from random import randint



def alea (min=1 , max=100) :
    
    return randint(min, max)

n_entre, n_mystere = 0, alea(min, max) 

def verif(n_entre, n_mystere) :
        
    if n_mystere < n_entre :
        print ("Moin")    
    elif n_mystere > n_entre :
        print ("Plus")
    else :
        print ("Nemo a trouver !\n")
    
while n_mystere == n_entre:
    print (" !\n ")
 
    