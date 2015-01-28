from Game import Game
import math

class SubtractSquares(Game):
    """A class of subtract square game state objects.
    
    Inherits from the generic Game class.
    
    Subtract Squares is a two-player game. Below are the instructions:
    1. A positive whole number is picked randomly by the computer (we will call this the target).
    2. A player picks a perfect square to subtract from the target, and the difference becomes the new target.
    3. The next player picks a perfect square to subtract from the target, again producing a new target.
    4. Players alternate turns until there are no longer any perfect squares that can be subtracted from the target. Whoever is to play next when this happens loses.
    
    """
    
    def __init__(self, max_choice, players):
        """ (SubtractSquares, int, list) -> None
        
        Initialize a subtract squares game state.
        """
        
        Game.__init__(self, players, 'Subtract Squares')
        self.state = max_choice

        for i in range(1, math.ceil(math.sqrt(self.state))):
            self.options.append(i**2)
            
            
    def __eq__(self, other):
        """ (SubtractSquares, SubtractSquares) -> Bool
        
        Determine whether two game states are equal.
        
        >>> a = SubtractSquares(78, ['Kasra', 'Abe'])
        >>> b = SubtractSquares(65, ['Kasra', 'Abe'])
        >>> a == b
        False
        >>> b = SubtractSquares(78, ['Kasra', 'Soheil'])
        >>> a == b
        True
        """
        
        return self.state == other.state
    
    def __str__(self):
        """ (SubtractSquares) -> str
        
        Return a string representation of the game state.
        
        >>> a = SubtractSquares(78, ['Kasra', 'Soheil'])
        >>> print(str(a))
        78: Kasra
        """
        
        return '{}: {}'.format(self.state, self.players[0])
    
    def __repr__(self):
        """ (SubtractSquares) -> str
        
        Represent the game state.
        
        >>> a = SubtractSquares(78, ['Kasra', 'Soheil'])
        >>> a
        SubtractSquares: max number = 78, next to move is Kasra.
        """
        
        return 'SubtractSquares: max number = {}, next to move is {}.'.format(self.state, self.players[0])


if __name__ == '__main__':
    import doctest
    doctest.testmod()