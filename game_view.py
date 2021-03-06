from time import sleep
from random import randint
from SubtractSquares import SubtractSquares
from BasicStrategy import BasicStrategy

class game_view:
    '''A class for playing an arbitrary two-player, sequential,
    perfect-information game.
    
    This class does not have __init__, __str__, __repr__, or __eq__
    methods because it only serves as the user interface for a game and is 
    thus dependent on user input, making such methods unfeasible.
    '''
    
    def print_title(game):
        ''' (Game) -> None
    
        Prints the title of the game in a box made up of ASCII characters.
        
        >>> a = SubtractSquares(100, ['Player', 'CPU'])
        >>> game_view.print_title(a)
        +----------------+
        |Subtract Squares|
        +----------------+
        +----------------+
        '''
    
        print('+' + '-'*len(game.title) + '+')
        print('|' + game.title + '|')
        print('+' + '-'*len(game.title) + '+')
        print('+' + '-'*len(game.title) + '+')
    
    def print_instructions(game):
        ''' (Game) -> None
    
        Prints the instructions of a game in a new line.
        
        >>> a = SubtractSquares(100, ['Player', 'CPU'])
        >>> game_view.print_instructions(a)
        <BLANKLINE>
        Subtract Squares is a two-player game. Below are the instructions:
        1. A positive whole number is picked randomly by the computer (we 
        will call this the target).
        2. A player picks a perfect square to subtract from the target, and 
        the difference becomes the new target.
        3. The next player picks a perfect square to subtract from the 
        target, again producing a new target.
        4. Players alternate turns until there are no longer any perfect 
        squares that can be subtracted from the target. Whomever is to play 
        next when this happens loses.
        <BLANKLINE>
        '''
        
        print('\n' + game.instructions + '\n') 
    
    def print_turn(game):
        ''' (Game) -> None
    
        Prints a notice of the next player to move.
        
        >>> a = SubtractSquares(100, ['Player 1', 'Player 2'])
        >>> game_view.print_turn(a)
        ~ Player 1's turn
        '''
        
        print('~ {}\'s turn'.format(game.players[0]))
    
    def print_state(game):
        ''' (Game) -> None
    
        Prints the state of the game.
        
        >>> a = SubtractSquares(100, ['Player 1', 'Player 2'])
        >>> game_view.print_state(a)
        +--------------------------+
        |  The game state is: 100  |
        +--------------------------+
        '''
        
        message = '  The game state is: {}  '.format(game.state)
        print('+' + '-'*len(message) + '+')
        print('|' + message + '|')
        print('+' + '-'*len(message) + '+')
    
    def print_options(game):
        ''' (Game) -> None
    
        Prints the possible moves for the current game state, with digits 
        right aligned for readability.
        
        >>> a = SubtractSquares(100, ['Player 1', 'Player 2'])
        >>> game_view.print_options(a)
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
        '''
        
        for i in range(len(game.available_moves())):
            print('{}{}. {}{}'.format(' '*(1 + len(str(len(game.available_moves()))) \
            - len(str(i + 1))), i + 1, ' '*(len(str(max(game.available_moves()))) - \
            len(str(game.available_moves()[i]))), game.available_moves()[i]))
    
    def get_input(game):
        ''' (Game) -> None
        
        Recursively ask for input, ensure that input is legal for the game.
        If input is legal, change the game state.
        '''
        
        player_input = \
        input('{}: Please enter a number between {} and {}, inclusive.\n'.\
        format(game.current_player(), 1, len(game.available_moves())))
        int_able = False 
        try: #Check if the user input can converted to an int
            int(player_input)
            int_able = True
        except ValueError:
            int_able = False
        if int_able and (int(player_input) in range(1, len(game.available_moves()) \
        + 1)): 
            game.change_state(int(player_input) - 1)
        else:
            print('Sorry, that input didn\'t work.')
            game_view.get_input(game)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(' _  _  ____  __     ___  __   _  _  ____ ' + '\n' +
          '/ )( \(  __)(  )   / __)/  \ ( \/ )(  __)' + '\n' +
          '\ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _) ' + '\n' +
          '(_/\_)(____)\____/ \___)\__/ \_)(_/(____)')
    a = SubtractSquares(randint(100, 1000), ['Player', 'CPU'])
    game_view.print_title(a)
    game_view.print_instructions(a)
    while not a.game_over():
        game_view.print_state(a)
        game_view.print_turn(a)
        if a.players[0] == 'Player':
            game_view.print_options(a)
            game_view.get_input(a)
        else:
            sleep(2)
            choice = BasicStrategy.default_strategy(a) - 1
            print("~ CPU chooses {}".format(a.available_moves()[choice]))
            a.change_state(choice)
    print('  ___   __   _  _  ____     __   _  _  ____  ____ ' + '\n' +
          ' / __) / _\ ( \/ )(  __)   /  \ / )( \(  __)(  _ \ ' + '\n' +
          '( (_ \/    \/ \/ \ ) _)   (  O )\ \/ / ) _)  )   /' + '\n' +
          ' \___/\_/\_/\_)(_/(____)   \__/  \__/ (____)(__\_)')
    print('{} Wins!'.format(a.winner()))
