from random import randint

class BasicStrategy(StrategyList):
    """A class containing a basic strategy that inherits from the generic strategy class."""
    
    def basic_strategy(game):
        """(Game) -> int
        
        Take a game object and produce a random choice from the options.
        """

        return randint(1, len(game.options))    