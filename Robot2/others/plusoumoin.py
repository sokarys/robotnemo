'''
Created on 16 janv. 2012

@author: boulange
'''

  
from random import randint



def alea (min , max) :
    return randint(min, max)
min, max = 1, 100
n_entre, n_mystere = 0, alea(min, max) 

def verif(n_entre, n_mystere) :
  if n_mystere < n_entre :
    print ("Moin")
  elif n_mystere > n_entre :
    print ("Plus")
  else :
    print ("Nemo a trouver !\n")
        

 
    