# cse210-04
## File structure
/+game
++casting
---actor()
---cast()
---score(Actor) [2 players]
---snake(Actor) -> bike [2 players]
++directing
---director()
++scripting
---action()
---control_actors_action(Action) -> Modify hard coding [2 players]
---drawactorsaction(Action) -> Draw two player
---handle collisiions action(Action) -> Handle collitions with player, oponent and walls
---move actors action(Action) -> Get game_alive variable, add method for move player 1 and player 2
---script()
++services
---keyboard_service()
---video_service()
++shared
---color
---point
/main
/constant

##Functionality assignments
###Daniel Parra
-Everything about adding second player

###Joseph Perez
-Handle collitions with screen
-Stop game
-Boolean conditions

###Jonathan Uribe (Team Leader)
-Handle points
-Software testing

###Thomas Villalobos
-Handle player collitions and himself

###Gloria Rosado
-Add control for multiple players
-Readme
