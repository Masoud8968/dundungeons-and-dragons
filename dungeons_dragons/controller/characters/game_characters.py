import setting.game_settings as gs
from dungeons_dragons.view.maze import mazes
from .base_character import BaseCharacter


class GameCharacter(BaseCharacter):
    """
    This is game characters class.
    it inherit from base character.
    any instance of this class can move in the direction that gets.
    """
    def __init__(self, name, location, icon):
        super().__init__(name)
        self.location = location
        self.icon = icon

    def __str__(self):
        statement = f"I am a {self.name}. and I'm in {self.location} coordinate" # noqa E501
        return statement

    def __repr__(self):
        # statement = f"I am a {self.name}. and I'm in {self.location} coordinate" # noqa E501
        statement = f"{self.location}"
        return statement

    def move_character(self, direction):
        X, Y = self.location
        if direction == "up" or direction == "8":
            first_condition = Y == gs.board_dimension
            coordinate = (X, Y + 1)
            second_condition = (coordinate in mazes.keys() and
                                mazes[coordinate] == "L")
            coordinate = (X, Y)
            third_condition = (coordinate in mazes.keys() and
                               mazes[coordinate] == "reversed gama")
            if first_condition or second_condition or third_condition:
                move = "restrict"
            else:
                Y += 1
                move = "up"
        elif direction == "down" or direction == "2":
            first_condition = Y == 1
            coordinate = (X, Y - 1)
            second_condition = (coordinate in mazes.keys() and
                                mazes[coordinate] == "reversed gama")
            coordinate = (X, Y)
            third_condition = (coordinate in mazes.keys() and
                               mazes[coordinate] == "L")
            if first_condition or second_condition or third_condition:
                move = "restrict"
            else:
                Y -= 1
                move = "down"
        elif direction == "right" or direction == "6":
            first_condition = X == gs.board_dimension
            coordinate = (X + 1, Y)
            second_condition = (coordinate in mazes.keys() and
                                mazes[coordinate] == "L")
            coordinate = (X, Y)
            third_condition = (coordinate in mazes.keys() and
                               mazes[coordinate] == "reversed gama")
            if first_condition or second_condition or third_condition:
                move = "restrict"
            else:
                X += 1
                move = "right"
        elif direction == "left" or direction == "4":
            first_condition = X == 1
            coordinate = (X - 1, Y)
            second_condition = (coordinate in mazes.keys() and
                                mazes[coordinate] == "reversed gama")
            coordinate = (X, Y)
            third_condition = (coordinate in mazes.keys() and
                               mazes[coordinate] == "L")
            if first_condition or second_condition or third_condition:
                move = "restrict"
            else:
                X -= 1
        self.location = [X, Y]
        return self.location

