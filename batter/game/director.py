from time import sleep
from game import constants
import threading

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (Cast object): The current game actors.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._exit = False
        self._update_active = True
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        # Initial draw before starting updates
        self._cue_action('output')

        # Create the update thread
        update_t = threading.Timer(0.05, self._do_update)

        # Start the update thread
        update_t.start()

        # Do IO updates on the main thread
        while not self._exit:
            self._exit = self._cue_returnable_action('input')
            if type(self._exit) is not bool:
                self._exit = False
            if self._exit:
                break
            self._cue_action('player')
            self._cue_action('output')
            # Maximum delay before the paddle wall collision doesn't work
            # This is done to balance CPU time with reduced input lag
            sleep(0.016)
        
        # Stop the update thread if it's alive on game exit
        if update_t.is_alive():
            self._exit = True
            update_t.join()

    def _do_update(self):
        """Preforms game updates for NPCs at a set delay.
        """
        while not self._exit:
            self._cue_action('movement')
            self._exit = self._cue_returnable_action('collision')
            sleep(constants.FRAME_LENGTH)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        self._script[tag].execute(self._cast)

    def _cue_returnable_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        return self._script[tag].execute(self._cast)