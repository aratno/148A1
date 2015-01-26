from random import randint

class StrategyList:
    def basic_strategy(game):
        """(Game) -> int
        
        Take a game object and produce a random choice from the options.
        """

        return randint(1, len(game.options))