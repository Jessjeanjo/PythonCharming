#!C/Python27/python.exe
'''
Created by Jessica Joseph | 2015 May 05

A program that transfers information from one file
to another. Also Manages Records and prints project summaries.
'''
from __future__ import print_function

import os.path

SEPARATOR = '*****'


def processInputFile():
    '''
        Returns a successfully open for read file object'''

    inputFileName = raw_input('Enter the name of your input file: ').lower()
    
    while not os.path.exists(inputFileName):
        inputFileName = raw_input('\nSorry that file does not exists.'\
                             '\nEnter a new file name: ').lower()
                             
    fileHandle = open(inputFileName, 'r')
    
    return fileHandle


def processOutputFile():
    '''
        Returns a successfully open for read file object'''

    outputFile = raw_input('Enter the name of your output file: ')


    if not os.path.exists(outputFile):
        fileHandle = open(outputFile, 'w')
    else: 
        overwriteOrNah = raw_input('This file currently exist. Do you want to wipe out this'\
                                   'pre-existing file?'\
                                   '\nEnter y for yes or n for no').lower()
        overwriteOutPuts = ['y','n']

        while overwriteOrNah not in overwriteOutPuts:
            overwriteOrNah = raw_input('That is not a valid input, please try again: ').lower()

        if overwriteOrNah == 'y':
            fileHandle = open(outputFile, 'w')
        else:
            fileName = raw_input('Please enter a new file name')
            fileHandle = open(fileName, 'w')

    return fileHandle
    


def getBtwnString():
    '''
        fvpekwvpo'''
    return raw_input('Enter your between word: ')



def transferProcess(inputFile, outputFile, btwnStr):
    '''
        wogjwirg'''
    for line in inputFile:
        spltLine = line.split()
        joinLine = btwnStr.join(spltLine)
        
        outputFile.write(joinLine)

    outputFile.close()
    inputFile.close()


def pauseTheScreen():
    '''
        sldivowev'''
    raw_input('Enter any key to continue')

def reverseTransferProcess():
    '''
        JIJOU'''
    print('\n\nTime to reverse the process')
    inputFileHandle = processInputFile()
    outputFileHandle = processOutputFile()
    betweenString = getBtwnString()
    
    testFi = inputFileHandle.readline()
    
    while testFi != '':
        
        unspltLine = testFi.split(betweenString)
        joinLine = ' '.join(unspltLine)
              
        
        outputFileHandle.write(joinLine+'\n')
        testFi = inputFileHandle.readline()
    inputFileHandle.close()
    outputFileHandle.close()


def creatingRecordInputFile():
    recordNumb = int(raw_input('How many records are you inputting? '))
    fileName = raw_input('What would you like to call the record file? ').txt

    writingFile = open(fileName, 'w')
    for record in range(recordNumb):
        projNumb = raw_input('Enter the project number: ')

        writingFile.write(projNumb+'\n')
        for numb in range(int(projNumb)):
            writingFile.write(raw_input('')+'\n')
        writingFile.write(SEPARATOR+'\n')

    writingFile.close()

def projectSummary():
    readingHandle = open(raw_input('Enter the record file name '), 'r')
    writingHandle = open(raw_input('Enter the summary file name '), 'w')
    floatCounter = 0

    uniqueNumb = readingHandle.readline().strip()
    bob = readingHandle.readline().strip()
        
    while bob != SEPARATOR and bob != '':
        floatCounter += float(bob)
        bob = readingHandle.readline().strip()

    writingHandle.write(uniqueNumb + ':   '+str(floatCounter))
        

        
    

def main():
    inputFileHandle = processInputFile()
    outputFileHandle = processOutputFile()
    betweenString = getBtwnString()
    transferProcess(inputFileHandle, outputFileHandle, betweenString)
    pauseTheScreen()
    reverseTransferProcess()
    creatingRecordInputFile()
    '''projectSummary()'''
    
    

if __name__ == '__main__':
    main()
