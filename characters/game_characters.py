from random import randint
from typing import Dict, List
from point.point import Point
import setting.game_settings as gs
from board.maze import mazes
from characters.base_character import BaseCharacter

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
        statement = f"I am a {self.name}. and I'm in {self.location} coordinate"
        return statement

    def __repr__(self):
        # statement = f"I am a {self.name}. and I'm in {self.location} coordinate"
        statement = f"{self.location}"
        return statement

    def  move_character(self, direction):
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
                restrict_dir = "up"
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
                restrict_dir = "down"
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
                restrict_dir = "right"
            else:
                X += 1
                move = "right"          
        elif direction == "left" or direction == "4":
            first_condition = X == 1
            coordinate = (X - 1, Y)
            second_condition = (coordinate in mazes.keys() and
                mazes[coordinate] == "reversed gama")
            coordinate =  (X, Y)
            third_condition = (coordinate in mazes.keys() and
                mazes[coordinate] == "L")
            if first_condition or second_condition or third_condition:
                move = "restrict"
                restrict_dir = "left"
            else:
                X -= 1
                move = "left"
        self.location = [X, Y]
        return self.location



