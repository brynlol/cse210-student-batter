from game.actor import Actor
from game import constants
from game.point import Point

class Cast:
    """ The Responsiblity of Cast is to set and get the base actors.
    
    Stereotype:
        Information Holder """
    def __init__(self):
        """ Class Constructor 
        
        Args:
            self (Cast): An instance of Cast
        """
        self._setup_base_actors()

    def _setup_base_actors(self):
        """ Call methods for setting up the paddle, bricks, and ball 
        
        Args:
            self (Cast): An instance of Cast
        """
        self.setup_paddle()
        self.setup_bricks()
        self.setup_ball()

    def setup_paddle(self):
        """ Sets up the paddle by adding its parts to a list and setting the the text and position
        
        Args:
            self (Cast): An instance of Cast
        """
        self._paddle_parts = []
        start_x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y - 1)
        for x in range(start_x, start_x + 11):
            position = Point(x, y)
            paddle = Actor()
            if x == start_x:
                paddle.set_text('╾')
            elif x == start_x + 10:
                paddle.set_text('╼')
            else:
                paddle.set_text('─')
            paddle.set_position(position)
            self._paddle_parts.append(paddle)
    
    def setup_bricks(self):
        """ Sets the bricks by adding each brick to list and setting the the text and position 
        
        Args:
            self (Cast): An instance of Cast
        """
        self._bricks = []
        for x in range(5, 75):
            for y in range(2, 6):
                position = Point(x, y)
                brick = Actor()
                brick.set_text("*")
                brick.set_position(position)
                self._bricks.append(brick)
    
    def setup_ball(self):
        """ Sets up the ball by setting the text and position of the ball 
        
        Args:
            self (Cast): An instance of Cast
        """
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)
        velocity = Point(1, -1)
        ball = Actor()
        ball.set_text("@")
        ball.set_position(position)
        ball.set_velocity(velocity)
        self._ball = ball

    @property
    def paddle_parts(self):
        """ Get all paddle parts
        
        Args:
            self (Cast): An instance of Cast
        
        Returns:
            List: the parts of the paddle which are Actors """
        return self._paddle_parts
    
    @property
    def bricks(self):
        """ Get the bricks
        
        Args:
            self (Cast): An instance of Cast
        
        Returns:
            list: the individual bricks which are Actors """
        return self._bricks
    
    @property
    def ball(self):
        """ Gets the ball
        
        Args:
            self (Cast): An instance of Cast
        
        Returns:
            ball: an instance of Actor """
        return self._ball
    
    @property
    def cast_list(self):
        """ Gets the cast to be displayed
        
        Args:
            self (Cast): An instance of Cast
        
        Returns:
            list: list of Actors to be displayed """
        formatted_cast = [self._paddle_parts, [self._ball], self._bricks]
        return formatted_cast
    
    @property
    def npc_list(self):
        return [[self._ball], self._bricks]
