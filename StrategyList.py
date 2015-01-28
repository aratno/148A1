class StrategyList:
    """A generic strategy class.
    
    This class does not have __init__, __str__, __repr__, and __eq__ methods because it is simply a superclass for subclasses that include the strategies.
    """
    
    def default_strategy(game):
        """A basic strategy method.
        """
        
        raise NotImplementedError('Need a subclass.')