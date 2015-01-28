import math
import random
from SubtractSquares import SubtractSquares

a = SubtractSquares(100, ['Player 1', 'Player 2'])

def print_title(game):
    """

    """
    print('+' + '-'*len(game.title) + '+')
    print('|' + game.title + '|')
    print('+' + '-'*len(game.title) + '+')

def print_instructions(game):
    """

    """
    print('\n' + game.instructions + '\n') 

def print_turn(game):
    """

    """
    print('~ {}\'s turn'.format(game.players[0]))

def print_state(game):
    """

    """
    print('The game state is:\n{}'.format(game.game_state))

print_title(a)
print_instructions(a)
#while a.state > 0:
print_target(a)
print_turn(a)
