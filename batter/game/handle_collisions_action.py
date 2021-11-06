import sys
from game import constants
from game.point import Point
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (Cast object): The current game actors.
        """
        self._paddle = cast.paddle_parts
        self._ball = cast.ball
        self._bricks = cast.bricks
        self._check_brick_collision()
        self._check_paddle_collision()
        self._check_top_collision()
        self._check_side_collision()
        # self._check_bottom_collision()
        
    def _check_brick_collision(self):
        projected_pos = self._calc_ball_direction()
        for brick in self._bricks:
            if brick.get_position().equals(projected_pos):
                self._bricks.remove(brick)
                start_vel = self._ball.get_velocity()
                end_vel = start_vel.reverse_y()
                self._ball.set_velocity(end_vel)

    def _check_paddle_collision(self):
        projected_pos = self._calc_ball_direction()
        for paddle_part in self._paddle:
            if paddle_part.get_position().equals(projected_pos):
                start_vel = self._ball.get_velocity()
                end_vel = start_vel.reverse_y()
                self._ball.set_velocity(end_vel)

    def _check_top_collision(self):
        projected_pos = self._calc_ball_direction()
        y = 0
        for x in range(constants.MAX_X):
            position = Point(x, y)
            if position.equals(projected_pos):
                start_vel = self._ball.get_velocity()
                end_vel = start_vel.reverse_y()
                self._ball.set_velocity(end_vel)

    def _check_side_collision(self):
        projected_pos = self._calc_ball_direction()
        for i in range(2):
            if i == 0:
                x = 0
            else:
                x = constants.MAX_X
            for y in range(constants.MAX_Y):
                position = Point(x, y)
                if position.equals(projected_pos):
                    start_vel = self._ball.get_velocity()
                    end_vel = start_vel.reverse_x()
                    self._ball.set_velocity(end_vel)

    def _check_bottom_collision(self):
        projected_pos = self._calc_ball_direction()
        for bottom_part in self._bottom:
            if bottom_part.get_postition().equals(projected_pos):
                pass
            else:
                pass

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

