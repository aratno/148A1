from random import randint
from StrategyList import StrategyList

class BasicStrategy(StrategyList):
    """A class containing a basic strategy that inherits from the generic strategy class.
    
    This class does not have __init__, __str__, __repr__, and __eq__ methods because it simply contains methods that correspond to different strategies.
    """
    
    def default_strategy(game):
        """(Game) -> int
        
        Take a game object and produce a random choice from the options.
        """

        return randint(1, len(game.options))