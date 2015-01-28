import math
import random
from SubtractSquares import SubtractSquares

a = SubtractSquares(100, ['Player 1', 'Player 2'])

def print_title(self):
    """

    """
    print('+' + '-'*len(self.title) + '+')
    print('|' + self.title + '|')
    print('+' + '-'*len(self.title) + '+')

def print_turn(self):
    """

    """
    print('~ {}\'s turn ~'.format(self.players[0]))

print_title(a)
print_turn(a)
