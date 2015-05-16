#!C:/Python27/python.exe
'''

Programmer: JESSICA JOSEPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Class Average
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Finds your class average based off of
three test scores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''

from __future__ import print_function


def main():
    className = raw_input('What is your class name? ')
    testAveOne = int(raw_input('\tWhat did you get on your first exam? '))
    testAveTwo = int(raw_input('\tWhat did you get on your second exam? '))
    testAveThree = int(raw_input('\tWhat did you get on your third exam? '))

    print('%s\n%i' %(className, ((testAveOne + testAveTwo + testAveThree)/3)))
    
       

if __name__ == '__main__':
    main()
