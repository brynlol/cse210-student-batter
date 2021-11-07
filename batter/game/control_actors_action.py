from game import constants
from game.action import Action
from game.actor import Actor
from game.point import Point

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            self (ControlActorsAction): An instnace of ControlActorsAction
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            self (ControlActorsAction): An instnace of ControlActorsAction
            cast (Cast object): The current game actors.
        """
        try:
            direction = self._input_service.get_direction()
            paddle_parts = cast.paddle_parts
            paddle_far_left = paddle_parts[0].get_position().get_x() == 1
            paddle_far_right = paddle_parts[-1].get_position().get_x() == constants.MAX_X - 1
            if paddle_far_left and direction.get_x() == -1:
                direction = Point(0, 0)
            if paddle_far_right and direction.get_x() == 1:
                direction = Point(0, 0)
            for sect in paddle_parts:
                if type(sect) is Actor:
                    sect.set_velocity(direction)
        except AttributeError:
            pass
        exit_condition = self._exit()
        return exit_condition
    
    def _exit(self):
        """Check whether the button for exiting was pressed.

        Args:
            self (ControlActorsAction): An instnace of ControlActorsAction

        Returns:
            bool: whether exit condition was met
        """
        direction = self._input_service.get_direction()
        if direction == 'exit':
            return True
        return False
