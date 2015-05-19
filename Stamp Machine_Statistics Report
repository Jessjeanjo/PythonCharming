#!C:/Python27/python.exe
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Programmer: JESSICA JOSEPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~
A stamp machine code with an added statistics
report for what went on during the run. This report is 
only seen at the end of the run when it is stopped
by the manager (or the maintenance person - they'll
just ignore this output, of course - or be confused by it!).
~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

from __future__ import print_function

#<====================IMPORTING==================>
import sys ; import random;

#<================GLOBAL CONSTANTS=============>

SEVENTYFOURC = .74 ;   THIRTYTWOC = .32 ;   SIXC = .06 ;

#<=================WELCOME BANNER===============>
def welcomeBanner():
    '''Prints a welcome banner'''    
    print('''
 ----------------------------------------------
|      Welcome to the snakStamp Machine!       |
|  We dispense only 74, 32, and 6 cent stamps. |
|   We give only coins in change  (no bills).  |
 ----------------------------------------------''')


#<=======================GETTING MY INPUTS==================>

def getInputs():
    '''Retrieves inputs'''
    firstName = raw_input('\nWhat is your first name? ')
    lastName = raw_input('What is your last name? ')
    return firstName, lastName

def getStampAmount():
    ''' Retrieves the stamp amounts'''
    stamps74Amount = raw_input('\nHow many 74 cent stamps would you like? ')
    stamps32Amount = raw_input('How many 32 cent stamps would you like? ')
    stamps6Amount = raw_input('How many 6 cent stamps would you like? ')
    return stamps74Amount, stamps32Amount, stamps6Amount

#<===========================CALCULATING THE BILL===============>

def calBill(stamp74Amnt, stamp32Amnt, stamp6Amnt):
    '''Calculates and Prints the amount of coins given and the their total value'''
    stamp74Tot = float(stamp74Amnt) * SEVENTYFOURC
    stamp32Tot = float(stamp32Amnt) * THIRTYTWOC
    stamp6Tot = float(stamp6Amnt) * SIXC
    stampTotal = stamp74Tot + stamp32Tot +stamp6Tot
    stampCoinTot = int(stamp74Amnt) + int(stamp32Amnt) + int(stamp6Amnt)
    
    print('\nThe price of your %i stamps is $ %.2f' %( stampCoinTot, stampTotal))
    return stampTotal

#<=======================QUANTITY OF BILLS===================>
def quantityOfCoins(amountOfUSDollars):
    '''Returns the amount of coins you will receive'''
    dollarCoins = amountOfUSDollars - amountOfUSDollars%1
    dollarCoinRemainder = amountOfUSDollars%1
    quarterCoins = (dollarCoinRemainder - dollarCoinRemainder%.25)/.25
    quarterCoinsRemainder = dollarCoinRemainder%.25
    dimeCoins = (quarterCoinsRemainder - quarterCoinsRemainder%.10)/.10
    dimeCoinsRemainder = quarterCoinsRemainder%.10
    nickleCoins = (dimeCoinsRemainder - dimeCoinsRemainder%.05)/.05
    nickleCoinsRemainder = dimeCoinsRemainder%.05
    pennyCoins = (nickleCoinsRemainder - nickleCoinsRemainder%.01)/.01
    pennyCoinsRemainder = nickleCoinsRemainder%.01
    return (dollarCoins, quarterCoins, dimeCoins, nickleCoins, pennyCoins)

def moneyCal(firstName, lastName, billTotal):
    '''Thanks the User and returns their change in coins. There are three parameters'''
    billToReceive = int(raw_input('\nHow many dollars will you be giving us? '))
    amntToCal = billToReceive-billTotal
    print('\nThank you. Just a moment please...\n\nThanks %s %s, your change is' %(firstName, lastName))

    dollarCoins, quarterCoins, dimeCoins, nickleCoins, pennyCoins = quantityOfCoins(amntToCal)
    if dollarCoins > 0: print('%i dollar coin(s)' %(dollarCoins))
    if quarterCoins > 0: print('%i quarter(s)' %(quarterCoins))
    if dimeCoins > 0: print('%i dime(s)' %(dimeCoins))
    if nickleCoins > 0: print('%i nickle(s)' %(nickleCoins))
    if pennyCoins > 0: print('%i penny(ies)' %(pennyCoins))
        
#<===================TAKING THE SURVEY, GIVING THE PRIZE=============>

def surveyPrompt(namE):
    '''Prompts a user to give a rating. There is one parameter.'''
    print('''
---======================================---
--- Thank you for using our stamp machine ---
---======================================---
\nCONGRATULATIONS %s!\n\nYou have been chosen to help us evaluate our machine.\n''' 
    'For helping you will have a chance to win a prize.\n' %(namE))
    ratingB = int(raw_input('Please rate our machine by entering a number between 1 and 10,\n with 10 benig really great and 1 being horrible: '))
    print('Thank you for using our stamp machine.')
    return ratingB


#<=============================THE PRIZE=====================>
def getPrize(ratE, billTotal):
    '''Retrieves and Displays the prize'''
    if ratE == random.randint(1,1000):
        print('You win $50')
    elif ratE == 2 or ratE == 4 or ratE == 7 or (17.25 <= ratE <= 58.42):
        print('You win $2.33')
    elif 1.37 <= ratE < 17.25:
        print('You win 37 cents')
    else:
        print('You win 3 cents')

#<=========================STATISTICS=========================>
def stampStatisticsRun():
    firstName, lastName = getInputs()
    customerCount = 0
    largestPurchase = 0
    smallestPurchase = 100000000
    sumOfPurchases = 0
    sameCoinCount = 0

    while firstName != 'manager' :
        welcomeBanner()
        stamp74Amnt, stamp32Amnt, stamp6Amnt = getStampAmount()
        stampTotal = calBill(stamp74Amnt, stamp32Amnt, stamp6Amnt)
        moneyCal(firstName, lastName, stampTotal)
        ratE = surveyPrompt(firstName)
        getPrize(ratE, stampTotal)
   
        firstName, lastName = getInputs()            
        customerCount += 1
        
        if stampTotal > largestPurchase:
            largestPurchase = stampTotal
        if stampTotal < smallestPurchase:
            smallestPurchase = stampTotal
        if (stamp32Amnt == stamp74Amnt) or (stamp32Amnt == stamp6Amnt):
            sameCoinCount += 1
            
        sumOfPurchases += stampTotal

    print('\nTotal Customer Count: %i'%(customerCount))
    print('Largest Purchase: %.2f' %(largestPurchase))
    print('Smallest Purchase: %.2f' %(smallestPurchase))
    print('Average Purchase: %.2f' %((sumOfPurchases)/customerCount))
    print('Percentage of Same Number of 32 cent stamps with others: %.0f'%((float(sameCoinCount)/float(customerCount))*100))
    
def main():
    stampStatisticsRun()
        
        
        
if __name__ =='__main__':
    main()
