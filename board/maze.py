from typing import List, Dict
from point.point import Point
from helper.probability import Probability
from random import choice
import setting.game_settings as gs

CELLS = list()
for column in range(1, gs.board_dimension + 1):
    for row in range(1, gs.board_dimension + 1):
        cell = Point(row, column)
        CELLS.append((cell.X, cell.Y))

class Maze:
    """
    This class generates randomly the mazes location and shapes.
    there are some limitation for maze locations and shapes.
    there are two shapes for mazes. "L" and "reversed gama" 
    """
    @staticmethod
    def maze_generator(maze_number):
        mazes: Dict = dict()
        while len(mazes) < gs.maze_number:
            mazes.clear()
            line_with_maze: List = list()
            column_with_maze: List = list()
            for cell in CELLS:
                X: int
                Y: int
                X, Y = cell
                if len(mazes) == gs.maze_number:
                    break
                if (X != 1 and
                        X != gs.board_dimension and
                        X not in line_with_maze and
                        Y not in column_with_maze and
                        Y - 1 not in column_with_maze and
                        Y + 1 not in column_with_maze and
                        Y != gs.board_dimension):
                    if Probability.generate() < 10:
                        maze_shape = choice(["L", "reversed gama"])
                        mazes[cell] = maze_shape
                        line_with_maze.append(X)
                        column_with_maze.append(Y)
        return mazes

mazes = Maze.maze_generator(gs.maze_number)