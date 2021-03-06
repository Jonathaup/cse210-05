import constants
from game.shared.color import Color
from game.shared.point import Point
from game.casting.actor import Actor
class Limit(Actor):
    def __init__(self):
        super().__init__()
        self._boolean = True
    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x())
        y = (self._position.get_y() + self._velocity.get_y())
        "Estabishes a border eliminating the wrapping feature"
        if y > constants.MAX_Y - 20:
            y = constants.MAX_Y - 20

        if x > constants.MAX_X - 10:
            x = constants.MAX_X - 10
        if y < 5:
            y = 5
        if x < 10:
            x = 10
        self._position = Point(x, y)
   
    def set_boolean(self, boolean):
        #Sets a boolean to control some part of the game
         self._boolean = boolean
   
    def get_boolean(self):
         #Get that boolean status
        return self._boolean


        
