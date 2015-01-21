from random import randint

class StrategyList:
    def basic_strategy(game):
        """Takes a game object and produces a random choice from the options."""
        
        options = game.options
        choice = randint(1, len(options))     
        
        return choice