#!C:/Python27/python.exe
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~
Created by Jessica Joseph 03 April 2015
~~~~~~~~~~~~~~~~~~~~~~~~~~
a program that will generate the shopping list
for the designated shopper to take to the grocery store.
~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

from __future__ import print_function

GROCERY_STORE = ["milk", "chocolate covered cherries", "apple", "orange", "banana",\
                    "corn on the cob", "kampyo sushi", "asparagus", "avocado", "alfalfa",\
                    "acorn squash", "almond package", "arugala bunch", "artichoke", \
                    "applesauce", "wasabi", "udon noodles", "tunafish can", "apple juice",\
                    "avocado sushi", "bruscetta", "bagel", "barley", "bisque", "bluefish", \
                    "bread", "broccoli", "buritto", "babaganoosh", "cabbage", "chocolate cake"\
                    , "red velvet cake", "strawberry short cake", "carrots", "celery", "cheese"\
                    , "catfish", "chowder", "clams", "coffee", "corn", "crab", "curry", "cereal"\
                    , "chimichanga", "dumpling", "donut", "egg", "enchilada", "eggroll", \
                    "english muffin", "edimame", "eelSushi", "o toro sashimi", "fajita",\
                    "falafel", "fondu", "french toast", "french dip", "garlic", "ginger",\
                    "gnocchi", "granola", "grape", "green bean", "guacamole", "gumbo", "grits",\
                    "graham crackers", "halibut", "honey", "huenos rancheros", "hash browns",\
                    "hummus", "chocolate ice cream", "strawberry ice cream", \
                    "cherry garcia ice cream", "puri", "veggie kurma", "jambalaya", "kale", \
                    "ketchup", "kiwi", "kidney beans pckg", "great northern beans pckg",\
                    "lobster", "linguine", "lasagna", "pepperoni pizza", "mushroom pizza",\
                    "pancakes", "quesadilla", "quiche", "spinach", "spaghetti", "tater tots",\
                    "toast", "waffles", "walnuts", "peanuts", "hazelnuts", "cranberries",\
                    "yogurt", "ziti", "zucchini", "canteloupe", "figs", "salt", "pepper", \
                    "nutmeg", "yucca", "shichimi"]

#<=====================PART ONE============================>
def doNotBuy():
    ''' creates a do not buy list '''
    notBuyList = []
    print('As the Designated Shopper you can choose to not buy certain items.'\
          '\nWhen you are done inputting type done.')
    notBuyItem = raw_input('Enter the food items you will NOT buy: ').lower()
    
    while notBuyItem != 'done':
        notBuyList.append(notBuyItem)
        notBuyItem = raw_input('Enter the food items you will NOT buy: ').lower()

    return notBuyList


def groceryList(DNBList):
    ''' creates a valid grocery list'''
    groceryList = []
    
    print('\nMaking your Grocery List!')
    groceryItem = raw_input('Enter the food items you neeed: ').lower()

    while groceryItem != 'shop':
        if groceryItem not in DNBList:
            if groceryItem in GROCERY_STORE:
                groceryList.append(groceryItem)
            else:
                print('Sorry this item is not available')
        else:
            print('Sorry this item cannot be brought')
        groceryItem = raw_input('Enter the food items you will buy: ')
        
    return groceryList
    
#<=====================PART TWO============================>
def sortAndCount(Lissy):
    ''' sorts and counts items in a list'''
    Lissy.sort()
    sortedPair = []; sortedCountList = []
    while Lissy != []:
        sortedPair.append(Lissy[0]); sortedPair.append(Lissy.count(Lissy[0]))
        sortedCountList.append(sortedPair)
        
        for item in range(Lissy.count(Lissy[0])):
            Lissy.remove(Lissy[0])
            sortedPair = []
            
    return sortedCountList

def printGroceryList(sortedList):
    ''' prints out the grocery list'''
    print(
        '%s\n%10s%10s\n%s' %('\n--FAMILY SHOPPING LIST--',\
                             'FOOD'+' '*(10-len('FOOD')),
                             'QUANTITY TO BUY'+' '*(10-len('QUANTITY TO BUY')),\
                             '-'*25))
    return [print('%20s%20s' %(item[0]+' '*(20-len(item[0])), str(item[1])+\
                      ' '*(20-len(str(item[1]))))) for item in sortedList]
    

#<=====================PART THREE============================>
def groceryMenu():
    ''' creates the grocery menu '''
    while True:
        menuChoice = raw_input(
    "\nType the corresponding number for your choice. Note: Create the DS's I won-t buy list first\n"
    '1. Add a food item to the shopping list\n'
    "2. Create the Designated Shopper's I-won't-buy list\n"
    '3. Display an Alphabetic list of all avaliable foods\n'
    '4. Quit and print shopping list in alphabetical order\n')
        if menuChoice == '1':
            try:
              groceryLissy = groceryList(notBuyList)
              sortedGroceryList = sortAndCount(groceryLissy)
            except UnboundLocalError :
              print('\nThe Designated Shopper has not yet created their "I won\'t buy" list'\
                    '\nPlease createthe Designated Shopper list, FIRST!\n')
              menuChoice
        elif menuChoice == '2':
            notBuyList = doNotBuy()
        elif menuChoice == '3':
            GROCERY_STORE.sort
            print(GROCERY_STORE)
        else:
            try:
              printGroceryList(sortedGroceryList)
              return False
            except UnboundLocalError:
              options = raw_input('\nThere are no items on the shopping list :)'\
                        '\nDo you want to add items to your list now or just quit?'\
                        '\nType "finish" to quit and "add" to add: ').lower()
              if options == 'finish':
                return False
              else:
                try:
                  groceryLissy = groceryList(notBuyList)
                  sortedGroceryList = sortAndCount(groceryLissy)
                except UnboundLocalError :
                  print('\nThe Designated Shopper has not yet created their "I won\'t buy" list'\
                    '\nPlease createthe Designated Shopper list, FIRST!\n')
                  menuChoice
    

def main():
    groceryMenu()

if __name__ == '__main__':
    main()
    
