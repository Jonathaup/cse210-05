import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.bike import Bike
from game.casting.limit import Limit
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.twoPlayerControl import twoPlayerControls
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    #cast.add_actor("foods", Food())
    cast.add_actor("player_1", Bike(constants.GREEN,150))
    cast.add_actor("player_2", Bike(constants.RED,750))
    cast.add_actor("score_player_1", Score("Player One"))
    cast.add_actor("score_player_2", Score("Player Two"))
    cast.add_actor("Game", Limit())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", twoPlayerControls(keyboard_service,"player_1",constants.PLAYER_1_CONTROLS))
    script.add_action("input", twoPlayerControls(keyboard_service,"player_2",constants.PLAYER_2_CONTROLS))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()