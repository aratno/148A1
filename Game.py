class Game:
    '''A generic class for game state objects.
    '''
    
    def __init__(self, players, title, instru):
        ''' (Game, str, int) -> NoneType
        
        
        Initialize a game state object.
        '''
        
        self.players = players
        self.title = title
        self.instructions = instru    
    
    def __eq__(self, other):
        '''Game, Game) -> Bool
        
        Determine whether two game states are equal.
        '''
        
        raise NotImplementedError('Need a specific game to determine \
        equality.')
    
    def __str__(self):
        ''' (Game) -> str
        
        Return a string representation of the game state.
        '''
        
        raise NotImplementedError('Need a specific game to return string.')
   
    def __repr__(self):
        ''' (Game) -> str
        
        Represent the game state.
        '''
        
        raise NotImplementedError('Need a specific game to represent.')
    
    def change_state(self, choice):
        ''' (Game, int) -> NoneType
        
        Take a choice and change the game state to a new one.
        '''
        
        raise NotImplementedError('Need a specific game to change state.')
    
    def available_moves(self):
        ''' (Game) -> list
        
        Return the available moves given the current game state.
        '''
        
        raise NotImplementedError('Need a specific game.')
        
           
    def current_player(self):
        ''' (Game) -> str
        
        Return which player from the list is next to play.
        '''
        
        raise NotImplementedError('Need a specific game.')
        
    def game_over(self):
        ''' (Game) -> bool
        
        Return whether or not the game is over.
        '''
        
        raise NotImplementedError('Need a specific game.')
        
    def winner(self):
        ''' (Game) -> int
        
        Return which player from the list is the winner.
        '''
        
        raise NotImplementedError('Need a specific game.')