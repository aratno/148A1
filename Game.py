class Game:
    """A generic class for game objects."""
    
    def __init__(self, how_to_play, initial_state, initial_moves, winner):
        self.how_to_play = how_to_play
        self.state = initial_state
        self.options = initial_moves
        self.next_to_move = 0
        self.turns = 0
        self.winner = None
        
    def change_state(self, move):
        """Given the move, this function produces a new state."""
        
        self.generic_change_state()
        #calls the generic change state function
        
        new_state = f(move)
        new_options = g(move)
        #the new state and new set of options will be SOME function of the move made
        
        self.state = new_state
        self.options = new_options
    
    def generic_change_state(self):
        """A generic game state change that applies to all games."""
        
        self.turns += 1
        self.next_to_move = self.turns%2         