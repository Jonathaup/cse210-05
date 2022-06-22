from game.scripting.action import Action
import constants
from game.shared.point import Point
from game.scripting.control_actors_action import ControlActorsAction

class twoPlayerControls(ControlActorsAction):
    def __init__(self, keyboard_service, player, controls):
        super().__init__(keyboard_service)

        self._player = player
        self._controls = controls
    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
       #Players Controls
        # left
        if self._keyboard_service.is_key_down(self._controls[0]):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down(self._controls[1]):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down(self._controls[2]):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down(self._controls[3]):
            self._direction = Point(0, constants.CELL_SIZE)
        #Reset the position of the objects, clear the list of segments and restore movement
        if self._keyboard_service.is_key_down("r"):
            to_clear_p1 = cast.get_first_actor('player_1').get_segments()
            to_clear_p2 = cast.get_first_actor('player_2').get_segments()
            to_clear_p1.clear()
            to_clear_p2.clear()
            cast.get_first_actor('player_1')._prepare_body(150)
            cast.get_first_actor('player_2')._prepare_body(750)
            cast.get_first_actor("Game").set_boolean(True)
            script.get_actions("update")[1].set_is_game_over()
            self._direction = Point(0, -constants.CELL_SIZE)
        bike = cast.get_first_actor(self._player)
        bike.turn_head(self._direction)