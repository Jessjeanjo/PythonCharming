#!C:/Python27/python.exe
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Programmer:JESSICA JOSEPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~
A module of functions that will create
the lines of a text flag
~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

 

def sameFullLine(designPattern, lineLength):
    '''Prints a full line of 5 characters, all of which are the same character.
    This parameter requires a single character which should be a string'''
    fullLineDesign = designPattern * lineLength
    return fullLineDesign

def repeatingPat(char1, char2, char3):
    '''Prints 3 subunits which contain a repeated character.
    There are three parameters, they require a single character which should be a string'''
    subUnitLength = 5
    subUnitOne = char1 * subUnitLength
    subUnitTwo = char2 * subUnitLength
    subUnitThree = char3 * subUnitLength
    print(subUnitOne + subUnitTwo + subUnitThree)

def alternatingPat(char1,char2,char3,char4,char5,char6):
    '''Prints 3 subunits which contain alternating characters.
    There are six parameters, they require a single character which should be a string'''
    
    subUnitOne = (char1 + char2)*2 + char1
    subUnitTwo = (char3 + char4)*2 + char3
    subUnitThree = (char5 + char6)*2 + char5
    print(subUnitOne + subUnitTwo + subUnitThree)
    
def repeatingAndAlternatePat(begOrEnd,char1,char2,char3,char4):
    '''Prints one subunit with alternating characters and the remaining two subunits which have a single
    repeating character. For the first parameter please enter one if you would like the alternating subunit
    to go at the beginning. Enter 2 if you would like the alternating subunit to go at the end. 
    The remaining parameters must be a single string character'''

    subUnitLength = 5
    subUnitOne = (char1 + char2)*2 + charac1
    subUnitTwo = char3 * subUnitLength
    subUnitThree = char4 * subUnitLength
    '''print(subUnitOne + subUnitTwo + subUnitThree)if begOrEnd == 1 else print(subUnitTwo + subUnitThree + subUnitOne) '''


def palinPattern(char1,char2,char3,char4,char5,char6,char7,char8,char9):
    '''Prints a 12321 Pattern, there are nine parameters.Parameters 1 to 3 are for subunit 1,
    Parameters 4 to 6 are for subunit 2, Parameters 7 to 9 are for subunit 3.
    These parameters must be a single string character
    '''
    subUnitOne = char1 + char2 + char3 + char2 + char1
    subUnitTwo = char4 + char5 + char6 + char5 + char4
    subUnitThree = char7 + char8 + char9 + char8 + char7
    print(subUnitOne + subUnitTwo + subUnitThree)




