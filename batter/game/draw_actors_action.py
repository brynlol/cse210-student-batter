from game.action import Action

class DrawActorsAction(Action):
    """ A code template for drawing actors. 
        The responsibility of this class of objects is to draw to the screen
        
    Stereotype: 
        Controller
        
    Attributes:
        _output_service: an instance of Output_Service
    """
    def __init__(self, output_service):
        """Class Contructor.
        
        Args:
            self (DrawActorsAction): An instance of DrawActorsAction
            
            output_service (OutputService): An instance of OutputService
    """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (Cast object): The current game actors.
        """ 
        self._output_service.clear_screen()
        for group in cast.cast_list:
            self._output_service.draw_actors(group)
        self._output_service.flush_buffer()