#!C:/Python27/python.exe
'''
Programmer: JESSICA JOSEPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Superhero
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Displays three superheros the 
user gives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

from __future__ import print_function

def main():
  heroNumbOne = raw_input('What is the name of your first superhero? ')
  heroNumbTwo = raw_input('What is the name of your second superhero? ')
  heroNumbThree = raw_input('What is the name of your third superhero? ')

  print('Superhero #1: %s\nSuperhero #2: %s\nSuperhero #3: %s\n' %(heroNumbOne, heroNumbTwo, heroNumbThree))
  
if __name__ == '__main__': 
  main()
