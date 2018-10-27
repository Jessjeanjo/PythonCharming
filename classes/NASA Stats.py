#!C:/Python27/python.exe
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Created by Jessica Joseph 06 April 2015
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A program for playing processing temperature
data from a data entry person working for NASA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

from __future__ import print_function

#<========GLOBAL CONSTANTS=============>
VALID_RANGE = 33.34
PRESUMED_TEMP_AVG = -232.00205
TEMP_PROCESSED = 0
PERCENT_REJECTED = 1
AVERAGE_TEMPERATURE = 2
MAXIMUM_TEMPERATURE = 3
MINIMUM_TEMPERATURE = 4

#<================FUNCTIONS==============>

def getTransmissionAmnt():
    '''
        Returns the amount of transmissions that need to be processed.
        Takes no parameters'''
    transmissionAmnt = int(raw_input('How many transmissions to process? '))
    while transmissionAmnt < 1:
        transmissionAmt = int(raw_input('Sorry must be 1 or more. Try again: '))

    return transmissionAmnt

def processData(transNumb):
    '''
        Processes the Data based on the'''
    countNumber = 1; rejectedNumb = 0
    dataSetList = []; maxAndMinList = []; rejectedList = []; averageList = []

    while countNumber < transNumb+1:
        
        print('\nStart etering data for set %i and indicate you are finished by typing STOP'%(countNumber))

        dataSetItem = raw_input('')
        
        while dataSetItem != 'STOP':
            if (PRESUMED_TEMP_AVG-VALID_RANGE) <= float(dataSetItem) <= (PRESUMED_TEMP_AVG+VALID_RANGE):
                dataSetList.append(float(dataSetItem))
            else:
                print('[REJECTED: %.2f]' %(float(dataSetItem)))
                rejectedNumb += 1
                
            dataSetItem = raw_input('').upper()

        if dataSetList == []:
            rejectedPercent = 0
            maxTep = 'Not Applicable'
            minTemp = 'Not Applicable'
            
        else:
            rejectedPercent = (float(rejectedNumb)/float((len(dataSetList)+rejectedNumb)))*100
        
        maxTemp, minTemp = maxMinAverageCal(dataSetList)                
        printData(countNumber, dataSetList, rejectedPercent, maxTemp, minTemp)

        maxAndMinList.append(maxTemp); maxAndMinList.append(minTemp) 
        rejectedList.append(rejectedPercent)
        averageList.append(sum(dataSetList)/len(dataSetList))

        countNumber += 1; dataSetList = []; rejectedNumb = 0
    maxTempera, minTempera = maxMinAverageCal(maxAndMinList)
    print('\nOverall Stats:'\
          '\nNumber of data sets processed: %i' \
          '\nAverage of all temperatures processed: %.4f' \
          '\nMaximum temperature: %.2f' \
          '\nMinimum temperature: %.2f' \
          '\nPercent rejected data: %.2f' \
          %(transNumb, sum(averageList)/len(averageList),\
            maxTempera, minTempera, sum(rejectedList)/len(rejectedList)))
            
            
    
def maxMinAverageCal(lissy):
    '''
        Calculates and Returns the maximum, minimum, and average total
        of the list that is passed as a parameter.'''
    mnTemp = 0; mxTemp = -500; avgCount = 0
    for items in lissy:
        if items > mxTemp:
            mxTemp = items
        if mnTemp > items:
            mnTemp = items
    return mxTemp, mnTemp
    
def printData(count, lissy, rPercent, maxT, minT):
    '''
        Prints the statistics of the data. Takes 5 parameters'''
    print('Data Set %i\nStats:'\
              '\nNumber of temperatures processed: %i'\
              '\nPercent rejected: %.2f' \
              '\nAverage temperature: %.2f' \
              '\nMaximum temperature: %.2f' \
              '\nMinimum temperature: %.2f' \
              %(count, len(lissy), rPercent, sum(lissy)/len(lissy), maxT, minT))
def main():
    transmissionNumber = getTransmissionAmnt()
    processData(transmissionNumber)


if __name__ == '__main__':
    main()
