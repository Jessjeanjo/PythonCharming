#!C:/Python27/python.exe
'''
Programmer: JESSICA JOSEPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
KIOSK REPEATING NAME GAME
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
An infinite game that prints out a person's
name the amount of times they desire.
Sometimes the manager's need to update or
fix the system. If the  name entered is 
Sally, Bob, or Joe the game is killed and 
loop is exited.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


'''

from __future__ import print_function

import sys

def getInput():
    '''
        Obtains and returns the amount of times
        the user wants their name printed and their
        name.'''
    numbOfTimes = int(raw_input('How many times would you like to play? '))
    userName = raw_input('What is your name? ')

    return numbOfTimes, userName

def kioskGame(repNumb, userName):
    '''
        Takes two parameters, a repeat number
        and name respectively. Prints Thanks, (username)
        for the repeat number'''
    for x in range(0, repNumb):
        print('Thanks, %s' %(userName))


def main():
    while True:
        repeatNumb, userName = getInput()
        kioskGame(repeatNumb, userName)
        if userName == 'Sally' or userName == 'Joe' or userName == 'Bob':
            sys.exit(17)
       

if __name__ == '__main__':
    main()
