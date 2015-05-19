#!C:/Python27/pyhton.exe
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Programmer: JESSICA JOSEPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~
A program that allows the user to create a list
and curiously prints the passed in list of values,
one per line where each line looks like this:

--- (3)

The quantity of hyphens before the value is printed is same as the value
~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

from __future__ import print_function
import random
    
def powerList(lowerBound, upperBound, exponent=2):
    '''
        Returns a list where the values are the powers of a number
        Takes 3 parameter. The exponent has a default parameter of 2'''
    while int(exponent) < 0:
        exponent = int(raw_input('\nYour value must be greater than zero.' \
                                 '\nTo use our random default value type 1, otherwise Try Again: '))
        if exponent == 1:
            exponent = random.randint(0, 9)        
        
    return [number**exponent for number in range(lowerBound, upperBound)]

def sequenceValues(powerLissy):
    '''
        Takes one parameter, a list. Prints the values of that list as a
        line that looks like: --- (3)'''

    for number in powerLissy:
        for i in range (number):
            print('-', end ='')
        print(number, end ='\n')

def main():
    while True:
        lowerValue = int(raw_input('Enter your starting value: '))
        upperValue = int(raw_input('Enter your ending value: '))+1
        exponent = int(raw_input('Enter your exponent value: '))
        powerLissy = powerList(lowerValue, upperValue, exponent)
        sequenceValues(powerLissy)

if __name__ == '__main__':
    main()
