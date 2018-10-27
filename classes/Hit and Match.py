#!C:/Python27/python.exe
'''
Programmer: JESSICA JOSEPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
HIT AND MATCH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Compares the cards of a users deck to the
house's card(the computer) and returns how
many user cards are in the houses' cards as a
match. And if the cards are the same value and
in the same position, returns the number as a hit.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The house cards will be chosen at random.
IF two house cards are the same then an internal error will launch
and there will be a system exit out of the program. The user will be
asked to input their cards, however if the cards are the same then
the user will be given an invalid try error message and the program
will go on. 

'''

from __future__ import print_function

#<================IMPORTING================>
import random; import sys;

#<===========RETRIEVING GOOD CARDS========>
def  retrieveGoodUserCards():
    ''' Obtains and returns the users' desired cards.
    The card numbers will range from 0 to 9
    '''
    leftUserCard = int(raw_input('\nEnter digit for left position: '))
    middleUserCard =  int(raw_input('Enter digit for middle position: '))
    rightUserCard =  int(raw_input('Enter digit for right position: '))

    if sameSetTest(leftUserCard, middleUserCard, rightUserCard):
        print('Sorry, that is an invalid try. \nCome back and play again sometime.')
        playOneHitAndMatchGame()
        return None, None, None         #Returning ( None, None, None ) so that you aren't returning a NoneType 
    else:
        return leftUserCard, middleUserCard, rightUserCard


def  retrieveGoodHouseCards():
    ''' Obtains and returns the users' desired cards.
    The card numbers will range from 0 to 9
    '''
    leftHouseCard = random.randint(0, 9)
    middleHouseCard =  random.randint(0, 9) 
    rightHouseCard =  random.randint(0, 9)
    
    if  sameSetTest(leftHouseCard, middleHouseCard, rightHouseCard):
        print('\nWe are sorry but the game has malfunction. \nEnding...')
        sys.exit(17)            #A TraceBack Error will not be displayed, however the program will be exited
        
    else:
        return leftHouseCard, middleHouseCard, rightHouseCard
        

#<==============TESTING CARD VALIDITY===========>
    
def sameSetTest(cardOne, cardTwo, cardThree):
    ''' Tests a set of values to see if any values appear more than once within the set
    Returns a bool expression. Takes three parameters.
    '''
    return cardOne == cardTwo or cardTwo == cardThree or cardThree == cardOne


#<===============HIT/MATCH FUNCTIONS==============>

def numbOfMatches(userOne, userTwo, userThree, houseOne, houseTwo, houseThree):
    '''Calculates the number of matches a person receives'''
    matchNumb =0
    
    if userOne == houseOne or userOne == houseTwo or userOne == houseThree:
         matchNumb += 1
         
    if userTwo == houseOne or userTwo == houseTwo or userTwo == houseThree:
        matchNumb += 1
        
    if userThree == houseOne or userThree == houseTwo or userThree == houseThree:
        matchNumb += 1
    
    return matchNumb

def numbOfHit(userOne, userTwo, userThree, houseOne, houseTwo, houseThree):
    '''Calculates the number of hits a Person receives'''
    
    hitNumb = 0
    
    if userOne == houseOne:
        hitNumb += 1
        
    if userTwo == houseTwo:
        hitNumb += 1
        
    if userThree == houseThree:
        hitNumb += 1

    return hitNumb

#<====================DISPLAYING===================>

def dispHitAndMatch(numbOfHit, numbOfMatch):
    ''' Displays the hit and match values '''
    print('%i hits\n%i matches' %(numbOfHit, numbOfMatch))

def playOneHitAndMatchGame():
    ''' Runs the Hit and Match Game'''
    raw_input('\nWelcome to the Hit && Match Game\nhit any key to start playing...')
    hCardOne, hCardTwo, hCardThree = retrieveGoodHouseCards()
    sameSetTest(hCardOne, hCardTwo, hCardThree)
    uCardOne, uCardTwo, uCardThree = retrieveGoodUserCards()
    matchNumb = numbOfMatches(uCardOne, uCardTwo, uCardThree, hCardOne, hCardTwo, hCardThree)
    hitNumb = numbOfHit(uCardOne, uCardTwo, uCardThree, hCardOne, hCardTwo, hCardThree)
    dispHitAndMatch(hitNumb, matchNumb)
    print('Come back and play again sometime.')        

       
def main():
    while True:
        playOneHitAndMatchGame()

if __name__ == '__main__':
    main()
