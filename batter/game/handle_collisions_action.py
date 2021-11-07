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
            self (HandleCollisionsAction): An instance of HandleCollisionsAction
            cast (Cast object): The current game actors.
        """
        self._paddle = cast.paddle_parts
        self._ball = cast.ball
        self._bricks = cast.bricks
        self._check_brick_collision()
        self._check_paddle_collision()
        self._check_top_collision()
        self._check_side_collision()
        alive = self._check_bottom_collision()
        return alive
        
    def _check_brick_collision(self):
        """ Check if the ball collides with a brick. If it does, remove the brick and divert the ball
        
        Args:
            self (HandleCollisionsAction): An instance of HandleCollisionsAction
        """
        projected_pos = self._calc_ball_direction()
        for brick in self._bricks:
            if brick.get_position().equals(projected_pos):
                self._bricks.remove(brick)
                start_vel = self._ball.get_velocity()
                end_vel = start_vel.reverse_y()
                self._ball.set_velocity(end_vel)

    def _check_paddle_collision(self):
        """ Check if the ball collides with the paddle. If it does, divert the ball in another direction. 
                
        Args:
            self (HandleCollisionsAction): An instance of HandleCollisionsAction
        """
        projected_pos = self._calc_ball_direction()
        for paddle_part in self._paddle:
            if paddle_part.get_position().equals(projected_pos):
                start_vel = self._ball.get_velocity()
                end_vel = start_vel.reverse_y()
                self._ball.set_velocity(end_vel)

    def _check_top_collision(self):
        """ Check if the ball collides with the top of the screen. If it does, divert the ball in another direction
                
        Args:
            self (HandleCollisionsAction): An instance of HandleCollisionsAction
        """
        projected_pos = self._calc_ball_direction()
        y = 0
        for x in range(constants.MAX_X):
            position = Point(x, y)
            if position.equals(projected_pos):
                start_vel = self._ball.get_velocity()
                end_vel = start_vel.reverse_y()
                self._ball.set_velocity(end_vel)

    def _check_side_collision(self):
        """ Check if the ball collides with the side of the screen. If it does, divert the ball in another direction
                
        Args:
            self (HandleCollisionsAction): An instance of HandleCollisionsAction
        """
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
        """ Check if the ball collides with the bottom of the screen. If it does, exit the game.
                
        Args:
            self (HandleCollisionsAction): An instance of HandleCollisionsAction
        """
        projected_pos = self._calc_ball_direction()
        y = constants.MAX_Y
        for x in range(constants.MAX_X):
            position = Point(x, y)
            if position.equals(projected_pos):
                return True
        return False

    def _calc_ball_direction(self):
        """ Calculate the direction of the ball.

        Args:
            self (HandleCollisionsAction): An instance of HandleCollisionsAction
        
        Returns:
            point: the point the ball will reach next. An instance of Point.
         """
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

