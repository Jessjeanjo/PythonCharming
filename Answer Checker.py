#!C:/Python27/python.exe
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Programmer: JESSICA JOSEPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Answer Checker
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Determines whether a given addition or
subtraction problem was solved correctly
~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
from __future__ import print_function

def checkAnswer(numbOne, numbTwo, resultNumb, strOperator):
    '''
        Determines if a given addition or subtraction problem was
        solved correctly.
        Takes four parameters.'''
    if strOperator == '+' :
        print((numbOne + numbTwo) == resultNumb)
    else: 
        print((numbOne - numbTwo) == resultNumb)


def main():
    firstNumb = int(raw_input('Enter your first digit: '))
    secondNumb = int(raw_input('Enter your first digit: '))
    resNumb = int(raw_input('Enter your first digit: '))
    operatorStr = raw_input('Enter your first digit: ')
    checkAnswer( firstNumb, secondNumb, resNumb, operatorStr)

if __name__ == '__main__':
    main()
