import random
from game.cast import Cast
from game.director import Director
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.move_player_action import MovePlayerAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):

    # create the cast (seperate containing object)
    cast = Cast()
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    move_player_action = MovePlayerAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script['input'] = control_actors_action
    script['player'] = move_player_action
    script['movement'] = move_actors_action
    script['collision'] = handle_collisions_action
    script['output'] = draw_actors_action

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)