from Game import Game

class Subtract_squares(Game):
    """A class of subtract square game objects.
    
    Inherits from the generic Game class.
    
    """
    
    def change_state(self, choice):
        """ (Game) -> None
        
        Given the move, produce a new state.
        
        'move' is the number inputted by the user
        'self.state' is the max number
        
        """
        
        self.generic_change_state()
        #change the number of turns, next to move
        
        self.state -= self.options[choice]
        #change the game state
        
        options = []
        for i in range(1, math.ceil(math.sqrt(self.state))):
            options.append(i**2)
        self.options = options
        #produce a new list of options
        
    