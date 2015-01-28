import math
import random
from SubtractSquares import SubtractSquares

a = SubtractSquares(100, ['Player 1', 'Player 2'])

def print_title(game):
    """
    (Game) -> None

    Prints the title of the game in a box made up of ASCII characters.

    >>>print_title(a)
    +---------------+
    |SubtractSquares|
    +---------------+
    """

    print('+' + '-'*len(game.title) + '+')
    print('|' + game.title + '|')
    print('+' + '-'*len(game.title) + '+')

def print_instructions(game):
    """
    (Game) -> None

    Prints the instructions of a game in a new line. Also, parses a string and inserts newlines to improve readability.

    >>>print_instructions(a)

   Subtract Squares is a two-player game. Below are the instructions:
   1. A positive whole number is picked randomly by the computer (we will call this the target).
   2. A player picks a perfect square to subtract from the target, and the difference becomes the new target.
   3. The next player picks a perfect square to subtract from the target, again producing a new target.
   4. Players alternate turns until there are no longer any perfect squares that can be subtracted from the target. Whomever is to play next when this happens loses. 

    """
    print('\n' + game.instructions + '\n') 

def print_turn(game):
    """
    (Game) -> None

    Prints a notice of the next player to move.

    >>>print_turn(a)
    ~ Player 1's turn
    """
    print('~ {}\'s turn'.format(game.players[0]))

def print_state(game):
    """
    (Game) -> None

    Prints the state of the game.

    >>>print_state(a)
    The game state is:
    100
    """
    print('The game state is:\n{}'.format(game.state))

def print_options(game):
    """
    (Game) -> None

    Prints the possible moves for the current game state, with digits right aligned for readability.

    >>>print_options(a)
     1.   1
     2.   4
     3.   9
     4.  16
     5.  25
     6.  36
     7.  49
     8.  64
     9.  81
    10. 100
    """
    output = ''
    for i in range(len(game.options)):
        output += (' '*(len(str(len(game.options))) - len(str(i))) + str(i + 1) + '. ' + ' '*(len(str(max(game.options))) - len(str(game.options[i]))) + str(game.options[i]) + '\n' )
    print(output)

def get_input(game):
    """
    
    """
    player_input = input('{}: Please enter a number between {} and {}, inclusive.\n'.format(game.players[0], 1, len(game.options)))
    int_able = False #Checks if the user input can converted to an integer
    try:
        int(player_input)
        int_able = True
    except ValueError:
        int_able = False
    if int_able and (int(player_input) in range(1, len(game.options) + 1)): 
        print('Job well done.')
    else:
        print('Sorry, that input didn\'t work.')
        get_input(game)

print_title(a)
print_instructions(a)
print_state(a)
print_turn(a)
print_options(a)
get_input(a)
