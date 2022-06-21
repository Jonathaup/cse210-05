from game.scripting.action import Action
from game.casting.limit import Limit

class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        game = cast.get_first_actor("Game")
        print(game.get_boolean())
        if game.get_boolean() == True:
            for actor in actors:
                actor.move_next()


