import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycles collide
    with their trail, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self.is_game_over = False
        self._message = Actor()

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self.is_game_over:
            self._handle_grow_trail(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
            game = cast.get_first_actor("Game")

    def _handle_grow_trail(self, cast):
        """Grow trails as they move.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        p1_bike = cast.get_first_actor("player_1")
        p1_bike.grow_tail(1)
        p2_bike = cast.get_first_actor("player_2")
        p2_bike.grow_tail(1)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycles collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        #Handdle collision and points
        score1 = cast.get_first_actor("score_player_1")
        score2 = cast.get_first_actor("score_player_2")
        p1_bike = cast.get_first_actor("player_1")
        p2_bike = cast.get_first_actor("player_2")
        head = p1_bike.get_segments()[0]
        segments = p1_bike.get_segments()[1:]
        head2 = p2_bike.get_segments()[0]
        segments2 = p2_bike.get_segments()[1:]
        for segmentz in [segments,segments2]:
            for segment in segmentz:
                if head.get_position().equals(segment.get_position()):
                    self.is_game_over = True
                    score2.add_points(1)
                    self._message.set_text('Player 2 Wins!\nPress "R" for a New Game')
                    self._message.set_color(constants.WHITE)
                    head2.set_color(constants.YELLOW)
                    for segment in segments2:
                        segment.set_color(constants.YELLOW)
                if head2.get_position().equals(segment.get_position()):
                    self.is_game_over = True
                    score1.add_points(1)
                    head.set_color(constants.YELLOW)
                    self._message.set_text('Player 1 Wins!\nPress "R" for a New Game')
                    self._message.set_color(constants.WHITE)
                    for segment in segments:
                        segment.set_color(constants.YELLOW)

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycles, display a message.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self.is_game_over:
            game = cast.get_first_actor("Game")
            p1_bike = cast.get_first_actor("player_1")
            p2_bike = cast.get_first_actor("player_2")
            segments = p1_bike.get_segments()
            segments2 = p2_bike.get_segments()
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)
            
            self._message.set_position(position)
            cast.add_actor("messages", self._message)
            game.set_boolean(None)

    def set_is_game_over(self):
        """Set the status of the game, if false means the game is running
            if True game is over
        """
        self.is_game_over = False
        self._message.set_text("")
