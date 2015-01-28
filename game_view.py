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
    print('Type help({}) for help.'.format(game.title))

def print_instructions(game):
    """

    """
    width = 2 + len(game.title)
    for i in range(width):
        print

def print_turn(game):
    """

    """
    print('~ {}\'s turn'.format(game.players[0]))

print_title(a)
print_turn(a)
