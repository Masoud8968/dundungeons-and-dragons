from enum import StrEnum

from termcolor2 import colored


class color(StrEnum):
    board_color = "yellow"
    maze_color = "red"
    user_color = "magenta"


class emoji(StrEnum):
    normal_player = colored("\u0001", "light_green")
    dragon = colored("¶", "blue")
    door = "\u0004"
    boosted_player = colored("\u0002", "green")
    booster = colored("\u0003", "light_red")
    separator = colored("\u0003", "green")
