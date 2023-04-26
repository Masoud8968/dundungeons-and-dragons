import os
from math import dist
from random import randint
import setting.game_settings as gs
from dungeons_dragons.controller.point import Point
from painless.helper.enums import emoji


class Tools:
    @staticmethod
    def calculate_distance(character1_location, character2_location) -> float:
        distance = abs(dist(character1_location, character2_location))
        return distance

    @staticmethod
    def random_point():
        random_point = Point(randint(1, gs.board_dimension), randint(1, gs.board_dimension))
        return random_point.coordinate

    @classmethod
    def initialize_dragons_location(cls, dragon_number, player_location):
        dragon_loc = player_location
        dragons_location = list()
        for num in range(dragon_number):
            while (cls.calculate_distance(player_location, dragon_loc) < 5 or
                    dragon_loc in dragons_location):
                dragon_loc = cls.random_point()
            dragons_location.append(dragon_loc)
            dragon_loc = player_location
        return dragons_location

    @staticmethod
    def shown_character(player, dragons):
        characters = {tuple(player.location): player.icon}
        for dragon in dragons:
            characters[tuple(dragon.location)] = dragon.icon
        return characters
