# cse210-05
Project Group week 9

# Cycle 
It is a game where the players try to cut each other off using cycles that leave a trail behind them. 

# Rules
    Players can move up, down, left and right...
        Player one moves using the W, S, A and D keys.
        Player two moves using the I, K, J and L keys.
    Each player's trail grows as they move.
    Players try to maneuver so the opponent collides with their trail.
    If a player collides with their opponent's trail...
        A "game over" message is displayed in the middle of the screen.
        The cycles turn white.
        Players keep moving and turning but don't run into each other.

## File structure
```
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
```

## Funcionality Contributors:
---

### Daniel Parra
- Everything about adding second player [X]
- Reset position of the objects [X]
- Set the direction of the cycle [X]
- Score Objects [X]
- Added controls as config file format [X]
- Class Bike [X]
- Removed Food Class from the code [X]

### Joseph Perez 
josephemilioperezpilier@gmail.com
- Handle collitions with screen [X]
- Stop game [X]
- Boolean conditions [X]
- Reset Button [X]
- Class Limit [X]
- Class twoPlayersControl [X]

### Jonathan Uribe (Team Leader)
- Handle points [X]
- Software testing [X]

### Thomas Villalobos
vil22003@byui.edu
- Handle player collitions and himself [X]
- Software testing [X]

### Gloria Rosado
- Add control for multiple players [X]
- Readme [X]

## Programs Required
* Python 3.10.1
* raylib
