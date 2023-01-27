import os
from board.maze import mazes
from helper.enums import color
from termcolor2 import colored
from typing import Dict, Optional
import setting.game_settings as gs
os.system('color')

mazes = mazes

class Board:
    """
    This class create the main borad of game
    """
    @staticmethod
    def vertical_line(vcolor: Optional[str] = color.board_color) -> str:
        """
        This method draws vertical line --> "|"
        """
        output = colored("|", vcolor)
        return output

    @staticmethod
    def horizontal_line(icon: str, hcolor: str) -> str:
        """
        This method draws horizontal lines --> "___"
        if there is any characters in line, puts it between the lines
        like this --> "_x_" 
        """
        colored_underscore = colored("_", hcolor)
        if icon == "_":
            character = colored_underscore
        else:
            character = colored(f"{icon}", color.user_color)
        output = f"{colored_underscore}{character}{colored_underscore}"
        return output

    @classmethod
    def generate_cell(cls, icon: Optional[str] = "_",
    vcolor: Optional[str] = color.board_color,
    hcolor: Optional[str] = color.board_color) -> str:
        cell = f"{cls.vertical_line(vcolor)}{cls.horizontal_line(icon, hcolor)}"
        return cell

    @classmethod
    def create_board(cls, board_dimension: int = gs.board_dimension, shown_character: Dict = {}):
        """
        This method uses horizontal_line and vertical_line and generate_cell
        to draw whole map. and considers where the characters are. like this -->
         _______________
        |___|___|___|___|
        |___|___|___|___|
        |___|_X_|___|___|
        |___|___|___|___|

        here "X" is located in [2, 2] coordinates.

        """
        maze_shape = ""
        up_line = (colored((" " + "_" * (board_dimension * 4 - 1)), color.board_color))
        print(up_line)
        for column in range(board_dimension, 0, -1):
            line = ""
            gama_maze = False
            if maze_shape == "reversed gama":
                gama_maze = True
            for row in range(1, board_dimension + 1):
                ver_color = color.board_color
                hor_color = color.board_color
                if ((row, column) in mazes.keys() and
                        mazes[(row, column)] == "L"):
                    ver_color = color.maze_color
                    hor_color = color.maze_color
                if ((row, column - 1) in mazes.keys() and
                        mazes[(row, column - 1)] == "reversed gama"):
                    hor_color = color.maze_color
                    gama_row = row + 1
                    maze_shape = "reversed gama"
                if (gama_maze is True and
                        row == gama_row):
                    ver_color = color.maze_color
                    gama_maze = False
                    maze_shape = ""
                if (row, column) in shown_character.keys():
                    considered_character = shown_character[(row, column)]
                    mesh = cls.generate_cell(icon=considered_character,
                        vcolor=ver_color, hcolor=hor_color)
                else:
                    mesh = cls.generate_cell(vcolor=ver_color, hcolor=hor_color)
                line += f"{mesh}"
                if row == board_dimension:
                    line += cls.vertical_line()
            print(line)