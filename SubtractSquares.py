from Game import Game
from math import floor, sqrt

class SubtractSquares(Game):
    '''A class of subtract square game state objects.
    
    Inherits from the generic Game class. Type state.instructions for any 
    game state to view the instructions.
    '''  
    
    def __init__(self, max_choice, players):
        ''' (SubtractSquares, int, list) -> None
        
        Initialize a subtract squares game state.
        max_choice is the initial state of the game
        players is the list of players' names
        '''
        
        instructions = 'Subtract Squares is a two-player game. Below are \
the instructions:\n1. A positive whole number is picked randomly by \
the computer (we \nwill call this the target).\n2. A player picks a \
perfect square to subtract from the target, and \nthe difference \
becomes the new target.\n3. The next player picks a perfect square \
to subtract from the \ntarget, again producing a new target.\n4. \
Players alternate turns until there are no longer any \
perfect \nsquares that can be subtracted from the target. Whomever \
is to play \nnext when this happens loses.'
        
        Game.__init__(self, players, 'Subtract Squares', instructions)
        self.state = max_choice
            
    def __eq__(self, other):
        ''' (SubtractSquares, SubtractSquares) -> Bool
        
        Determine whether two game states are equal.
        
        >>> a = SubtractSquares(78, ['Kasra', 'Abe'])
        >>> b = SubtractSquares(65, ['Kasra', 'Abe'])
        >>> a == b
        False
        >>> b = SubtractSquares(78, ['Kasra', 'Soheil'])
        >>> a == b
        True
        '''
        
        return self.state == other.state
    
    def __str__(self):
        ''' (SubtractSquares) -> str
        
        Return a string representation of the game state.
        
        >>> a = SubtractSquares(78, ['Kasra', 'Soheil'])
        >>> print(str(a))
        Subtract Square 78, Kasra
        '''
        
        return 'Subtract Square {}, {}'.format(self.state, self.players[0])
    
    def __repr__(self):
        ''' (SubtractSquares) -> str
        
        Represent the game state.
        
        >>> a = SubtractSquares(78, ['Kasra', 'Soheil'])
        >>> a
        SubtractSquares(78, ['Kasra', 'Soheil'])
        '''
        
        return 'SubtractSquares({}, {})'.format(self.state, self.players)
    
    def change_state(self, choice):
        ''' (SubtractSquares, int) -> NoneType
        
        Take a choice and change the game state to a new one.
        
        >>> a = SubtractSquares(102, ['Kasra', 'Soheil'])
        >>> a.change_state(8)
        >>> a
        SubtractSquares(21, ['Soheil', 'Kasra'])
        '''
        
        self.state -= self.available_moves()[choice] #changes the state
        self.players.reverse() #reverses the player list
        
    def available_moves(self):
        '''(SubtractSquares) -> list
        
        Return the available moves given the current game state.
        
        >>> a = SubtractSquares(78, ['Kasra', 'Soheil'])
        >>> a.available_moves()
        [1, 4, 9, 16, 25, 36, 49, 64]
        '''
        
        return [i**2 for i in range(1, int(floor(sqrt(self.state))) + 1)] 
    
    def current_player(self):
        '''(SubtractSquares) -> str
        
        Return which player from the list is next to play.
        
        >>> a = SubtractSquares(100, ['Kasra', 'Soheil'])
        >>> a.current_player()
        'Kasra'
        '''
        
        return self.players[0]
    
    def game_over(self):
        '''(SubtractSquares) -> bool
        
        Return whether the game is over.
        
        >>> a = SubtractSquares(100, ['Kasra', 'Soheil'])
        >>> a.game_over()
        False
        >>> a.change_state(9)
        >>> a.game_over()
        True
        '''
        
        return self.state == 0
    
    def winner(self):
        '''(SubtractSquares) -> str
        
        Return which player from the list is the winner.
        
        >>> a = SubtractSquares(100, ['Kasra', 'Soheil'])
        >>> a.winner()
        >>> a.change_state(9)
        >>> a.winner()
        'Kasra'
        '''
        
        if self.game_over():
            return self.players[1]
        else:
            return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()