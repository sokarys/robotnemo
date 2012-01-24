'''
Created on 16 janv. 2012

@author: boulange
'''

  
from random import randint



n_entre, n_mystere = 0, randint(1, 100) 

def verif(n_entre, n_mystere) :
    if n_mystere < n_entre :
        print ("Moin") 
    elif n_mystere > n_entre :
        print ("Plus")
    else :
        print ("Nemo a trouver !\n")
        return True
    
    return False

def entree_nombre():
    return int(raw_input("Entrez un nb\n"))

while True:
    n_entre = entree_nombre()
    if verif(n_entre, n_mystere):
        break
 
 

#import math
#import random
#import os
#class Game(object):
#    def __init__(self):
#        self.__randNumber = int(random.random()*100)
#        self.__NbPlayer = self.__randNumber + 1
#        print "Number:", self.__randNumber
#        
#    def run(self):
#        while self.__NbPlayer != self.__randNumber:
#            try:
#                self.__NbPlayer = int(raw_input("Entrez un nb\n"))
#            except:
#                exit("Erreur, merci de rentrer un nombre fin du programme")
#            print self.__NbPlayer , self.__randNumber
#            if self.__NbPlayer < self.__randNumber :
#                print "+"
#            elif self.__NbPlayer > self.__randNumber :
#                print "-"
#            else:
#                print "win"
#        
##Normalement il y a un if pour verif si on est dans le programme principale
#game = Game()
#game.run()