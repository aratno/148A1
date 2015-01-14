from random import randint
from math import *

#This is a file to test out A1 methods

max_number = 100
number = randint(0, max_number)
options = []

def setup():
    print('>>> setup begins')
    print('Number is: ' + str(number))

def fill_options():
    #Edit this to accept the options list as a parameter
    """
    Fills the 'options' list with all of the squares under 'number'
    For testing, it will print the last element of 'options' and its square.
    """
    for i in range(0, ceil(sqrt(max_number))):
        #print(i)
        if i**2 <= number:
            options.append(i)
        else:
            pass
    max_choice = options.index(len(options) - 1)
    print('Maximum choice is: ' + str(max_choice) + ', squared: ' + str(max_choice**2))

def display_options():
    #Mandate domain for input (no strings, only integers within range to be accepted)
    #Add proper formatting for digits to align to units place
    """
    Takes a list of options and returns the selected option.
    """
    print('>>> display_options begins')
    for i in options:
        print(str(i) + '. ' + str(i**2))
    selection = int(input('Select an index from above: '))
    print('Selection is: ' + str(selection) + ', which is: ' + str(options.index(selection)**2)) 

def continue_game():#Old parameters were 'target' and 'choice'
    #Unify naming conventions
    if number - choice < 0:
        pass #This shouldn't be possible
    else:
        number =- choice
        print('New number is: ' + number)
        #If this doesn't work, clear 'options' first
        fill_options()
        display_options()

#Testing Methods Below

print('-'*30)
setup()
fill_options()
display_options()
continue_game()
