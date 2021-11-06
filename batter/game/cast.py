from game.actor import Actor
from game import constants
from game.point import Point

class Cast:

    def __init__(self):
        self._setup_base_actors()

    def _setup_base_actors(self):
        self.setup_paddle()
        self.setup_bricks()
        self.setup_ball()

    def setup_paddle(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y - 1)
        position = Point(x, y)
        paddle = Actor()
        paddle.set_text("===========")
        paddle.set_position(position)
        self._paddle = paddle
    
    def setup_bricks(self):
        self._bricks = []
        for x in range(5, 75):
            for y in range(2, 6):
                position = Point(x, y)
                brick = Actor()
                brick.set_text("*")
                brick.set_position(position)
                self._bricks.append(brick)
    
    def setup_ball(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)
        velocity = Point(1, -1)
        ball = Actor()
        ball.set_text("@")
        ball.set_position(position)
        ball.set_velocity(velocity)
        self._ball = ball
    
    def make_debug(self, input_serv):
        self._input = input_serv
        debug = Actor()
        debug.set_position(Point(0, 0))
        self._debug = debug

    @property
    def paddle(self):
        return self._paddle
    
    @property
    def bricks(self):
        return self._bricks
    
    @property
    def ball(self):
        return self._ball
    
    @property
    def cast_list(self):
        if __debug__:
            formatted_cast = [[self._paddle], [self._ball], self._bricks, [self._debug]]
        else:
            formatted_cast = [[self._paddle], [self._ball], self._bricks]
        return formatted_cast
    
    @property
    def debug(self):
        return self._debug
    
    @debug.setter
    def debug(self, debug):
        self._debug.set_text(debug)
