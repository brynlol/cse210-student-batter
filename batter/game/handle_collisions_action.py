from game import constants
from game.point import Point
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        # TODO:
        """Executes the action using the given actors.

        Args:
            cast (Cast object): The current game actors.
        """
        self._paddle = cast.paddle
        self._ball = cast.ball
        self._bricks = cast.bricks
        self._check_brick_collision()
        
    def _check_brick_collision(self):
        projected_pos = self._calc_ball_direction()
        for brick in self._bricks:
            if brick.get_position().equals(projected_pos):
                self._bricks.remove(brick)

    def _calc_ball_direction(self):
        ball_pos = self._ball.get_position()
        ball_vel = self._ball.get_velocity()
        if ball_vel.get_x() < 0:
            x = -1
        if ball_vel.get_x() > 0:
            x = 1
        if ball_vel.get_y() < 0:
            y = -1
        if ball_vel.get_y() > 0:
            y = 1
        return ball_pos.add(Point(x, y))

        




"""Example from RFK:        
        marquee = cast["marquee"][0] # there's only one
        robot = cast["robot"][0] # there's only one
        artifacts = cast["artifact"]
        marquee.set_text("")
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                description = artifact.get_description()
                marquee.set_text(description) 
        """