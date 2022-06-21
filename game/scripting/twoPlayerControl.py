from game.scripting.action import Action
import constants
from game.shared.point import Point
from game.scripting.control_actors_action import ControlActorsAction
class twoPlayerControls(ControlActorsAction):
    def __init__(self, keyboard_service,player,controls):
        super().__init__(keyboard_service)
        self._keyboard_service2 = keyboard_service
        self._direction2 = Point(constants.CELL_SIZE, 0)
        self._player = player
        self._controls = controls
    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
       #Player 1 Controls
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
        
        bike = cast.get_first_actor(self._player)
        bike.turn_head(self._direction)
        
        # #Player 2 Controls
        # if self._keyboard_service2.is_key_down('j'):
        #     self._direction2 = Point(-constants.CELL_SIZE, 0)
        
        # # right
        # if self._keyboard_service2.is_key_down('l'):
        #     self._direction2 = Point(constants.CELL_SIZE, 0)
        
        # # up
        # if self._keyboard_service2.is_key_down('i'):
        #     self._direction2 = Point(0, -constants.CELL_SIZE)
        
        # # down
        # if self._keyboard_service2.is_key_down('k'):
        #     self._direction2 = Point(0, constants.CELL_SIZE)
        
        # bike = cast.get_first_actor("player_2")
        # bike.turn_head(self._direction2)
