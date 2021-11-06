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

    @property
    def paddle_parts(self):
        return self._paddle_parts
    
    @property
    def bricks(self):
        return self._bricks
    
    @property
    def ball(self):
        return self._ball
    
    @property
    def cast_list(self):
        formatted_cast = [self._paddle_parts, [self._ball], self._bricks]
        return formatted_cast
    
    @property
    def npc_list(self):
        return [[self._ball], self._bricks]
