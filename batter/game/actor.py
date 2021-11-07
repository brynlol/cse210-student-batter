from game import constants
from game.point import Point

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Actor): An instance of Actor
        """
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_position(self):
        """Gets the actor's position in 2d space.

        Args:
            self (Actor): An instance of Actor
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.

        Args:
            self (Actor): An instance of Actor
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.

        Args:
            self (Actor): An instance of Actor
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            self (Actor): An instance of Actor
            position (Point): The given position.
        """
        self._position = position
    
    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            self (Actor): An instance of Actor
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            self (Actor): An instance of Actor
            position (Point): The given velocity.
        """
        if type(velocity) is Point:
            self._velocity = velocity