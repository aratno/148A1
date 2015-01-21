import random
import math

title = 'Subtract Squares'
width = 100
max_target = 100 
user_input = None
game_state = random.randint(0, max_target)
options = [] 
player = 0

def print_bar(length):
    """
    int -> None
    Prints a length of hyphens ('-') to separate vertical elements.
    """
    print(('-' * length) if type(length) is int else ('-' * 10))

def get_options(game_state):
    """
    int -> list
    Given a game state, find the list of possible moves.
    """
    output = []
    for i in range(1, math.ceil(math.sqrt(max_target))):
            if i**2 <= game_state:
                output.append(i)
            else:
                break
    return output

def get_input(message = 'Please enter your choice below.\n'):
    """
    None -> int
    Returns the user's choice (of index) from the 'options' list of possible moves.
    """
    choice = input(message)
    try:
        return int(choice)
    except ValueError:
        return get_input('Sorry, I didn\'t understand that input. Please enter an integer below.\n') 

print('Welcome to {}.'.format(title))
options.append(get_options(game_state))
while game_state > 0:
    print('\nPlayer {}\'s turn.'.format((player % 2) + 1))
    print('The target is {}.'.format(game_state))
    print('The options are:')
    print('bugtest: ' + str(options))
    options = get_options(game_state)
    for i in options:
        print('{}. {}'.format(i, options[i]))
    game_state -= options[get_input()]
    player += 1
print('Game over. Player {} wins.'.format((player % 2) + 1))
