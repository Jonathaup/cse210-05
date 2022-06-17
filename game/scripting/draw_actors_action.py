from game.scripting.action import Action
from game.shared.point import Point

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        p1_score = cast.get_first_actor("score_player_1")
        p2_score = cast.get_first_actor("score_player_2")
        p2_score.set_position(Point(800,1))
        #food = cast.get_first_actor("foods")
        p1_bike = cast.get_first_actor("player_1")
        p2_bike = cast.get_first_actor("player_2")
        p1_segments = p1_bike.get_segments()
        p2_segments = p2_bike.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        #self._video_service.draw_actor(food)
        self._video_service.draw_actors(p1_segments)
        self._video_service.draw_actors(p2_segments)
        self._video_service.draw_actor(p1_score)
        self._video_service.draw_actor(p2_score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()