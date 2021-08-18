# Exercise #2

# Write a class Rocket - a simulator for a rocket ship in a game.
# The __init__() method doesn't take any arguments but sets the x and y positions to zero.

# Rocket class has 5 methods:

# move_up() - will increment y position by 1
# move_right() - will increment x position by 1
# mode_down() - will decrement y position by 1
# move_left() - will decrement x position by 1
# current_position() - will print the  current position of the Rocket

class Rocket:
    """Rocket class - a simulator for a rocket ship in a game."""

    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def current_position(self):
        print("Current position of the rocket: X: " + str(self.x) + "; Y:" + str(self.y))


Souyz_Rocket = Rocket()
Souyz_Rocket.current_position()
Souyz_Rocket.move_up()
Souyz_Rocket.move_right()
Souyz_Rocket.current_position()
Souyz_Rocket.move_down()
Souyz_Rocket.move_left()
Souyz_Rocket.current_position()
