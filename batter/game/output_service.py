import sys
from game import constants
from asciimatics.widgets import Frame

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen
        
    def clear_screen(self):
        """Clears the Asciimatics buffer for the next rendering.

        Args:
            self (OutputService): An instance of OutputService
        """ 
        self._screen.clear_buffer(7, 0, 0)
        self._draw_border()
    
    def _draw_border(self):
        """ Draws the border around the screen.
        
        Args:
            self (OutputService): An instance of OutputService
        """
        top_border = '╔' + ("═" * (constants.MAX_X - 1)) + '╗'
        bottom_border = '╚' + ("═" * (constants.MAX_X - 1)) + '╝'
        self._screen.print_at(top_border, 0, 0, 7)
        self._screen.print_at(bottom_border, 0, constants.MAX_Y, 7)
        for y in range(1, constants.MAX_Y):
            self._screen.print_at('║', 0, y, 7)
            self._screen.print_at('║', constants.MAX_X, y, 7)
        
    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            self (OutputService): An instance of OutputService
            actor (Actor): The actor to render.
        """ 
        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(text, x, y, 7) # WHITE

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService
        
        """ 
        self._screen.refresh()    