import math
import random

game_state = 121
options = []
options.extend(range(1, int(math.sqrt(game_state)) + 1))
title = 'Subtract Squares'
players = ['Abe', 'Kasra']

print('game_state: {}'.format(game_state))
print('options: {}'.format(options))

#Create a 'SubtractSquares' object called 'a'
#a = SubtractSquares(game_state, players)
#while a.game_state > 0:
#   a = SubtractSquares(game_state, a.players)

def print_title(title):
    print('+' + '-'*len(title) + '+')
    print('|' + title + '|')
    print('+' + '-'*len(title) + '+')

title = 'Subtract Squares'
print_title('  ' + title + '  ') 
