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
        
        new_state = f(move)
        new_options = g(move)
        #the new state and new set of options will be SOME function of the move made
        
        turns += 1
        next_to_move = turns%2       
        
        self.state = new_state
        self.options = new_options
        
    def get_options(self):
        """Given the game state, this function produces the options for the next player in a readable form."""
        
        options_display = h(self.options)
        #this will be a function that takes the list or dictionary of options and produces a readable/printable list
        
        return options_display