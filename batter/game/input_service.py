import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for left, right.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}
        self._keys[97] = Point(-1, 0) # a
        self._keys[100] = Point(1, 0) # d
        
    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            direction = self._keys.get(event.key_code, Point(0, 0))
            # This key has to be held for multiple frames to be detected
            if event.key_code == 27 or event.key_code == -1:
                direction = 'exit'
        return direction