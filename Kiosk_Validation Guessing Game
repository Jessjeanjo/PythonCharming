#!C:/Python27/python.exe
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Programmer: JESSICA JOSEPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A infinite guessing game that asks the user to 
type a single character (one button on the keyboard) and
returns that digit - as a str - when it is valid.

A valid input is within 2 of a passed in "middle" digit
- or- it's valid if it is one of these non-digits:
'#', '%', or '@'.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For example 
If the passed in "middle" digit is 4, then the only 
valid digits are: 2, 3, 4, 5, and 6. The user is not 
shown this "middle" digit so it's more like a guessing game
for the user to figure out how to enter a valid input.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

from __future__ import print_function

#<============IMPORTING============>
import random
#<==========GETTING USER INPUTS=======>

def getInput():
    '''
        Returns a single character which the user inputs. '''
    
    divisorNumb = 1
    userCharacter = raw_input('Enter a single character: ')

    while len(userCharacter) != 1:
        userCharacter = raw_input('Sorry, try again:  ')        

    return userCharacter
        
#<==========GETTING MIDDLE DIGIT=========>

def getMiddleDigit():
    '''
        Returns a randomly generate number between the
        value of 2 and 7 inclusive. '''

    return random.randint(2, 7)

#<================VALIDITY TESTING=========>

def createValidScope(middleDigit):
    '''
        Generates a valid scope (+ and -) 2 based off of the
        middle digit passed through as a parameter'''

    standardDeviation = 2 #helps create the validation range
    return range(middleDigit - standardDeviation, (middleDigit + standardDeviation) +1)

def userInputValidity(userInput, middleRange):
    '''
        Validates whether the user's input is  within the
        valid range of the middle digits'''
    
    if userInput == '@' or userInput == '%' or userInput == '#':
        print(userInput)
    elif int(userInput) in (middleRange):
        print(userInput)
    else:
        print('Sorry your number is not valid')


def main():
    while True:
        userInput = getInput()
        middleDig = getMiddleDigit()
        validRange = createValidScope(middleDig)
        userInputValidity(userInput, validRange)


#<===============CALLING============>

if __name__ == '__main__':
    main()
