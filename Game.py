class Game:
    """A generic class for game state objects."""
    
    def __init__(self, players, title):
        """ (Game, str, int) -> NoneType
        
        
        Initialize a game state object.
        """
        
        self.players = players
        self.next_to_move = 0
        self.winner = None
        self.options = []
        self.title = title
        
    def __eq__(self, other):
        """(Game, Game) -> Bool
        
        Determine whether two game states are equal.
        """
        
        raise NotImplementedError('Need a specific game to determine equality.')
    
    def __str__(self):
        """ (Game) -> str
        
        Return a string representation of the game state.
        """
        
        raise NotImplementedError('Need a specific game to return string.')
    
    def __repr__(self):
        """ (Game) -> str
        
        Represent the game state.
        """
        
        raise NotImplementedError('Need a specific game to represent.')