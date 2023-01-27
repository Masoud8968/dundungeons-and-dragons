from random import randint, choice, sample
from characters.game_characters import GameCharacter
from helper.probability import Probability
from helper.tools import Tools
import setting.game_settings as gs

class Dragon(GameCharacter):
    """
    This is Dragon class.
    this class inherit from Base character.
    any instance of this class can move randomly with move method.
    also they can get player location and move in two condition.
    follow player and escape from player.
    it depends on the situation.
    """
    def move(self, dragon_location, dragon_old_location):
        while dragon_location == dragon_old_location:
            chosen_direction = choice(gs.VALID_MOVES)
            dragon_location = self.move_character(chosen_direction)

    def follow_mode_move(self, player_location):
        dragon_dist = Tools.calculate_distance(self.location, player_location)
        dragon_old_dist = dragon_dist
        dragon_current_location = self.location
        dragon_old_location = self.location.copy()        
        if dragon_dist > 7:
            dragon_current_location = self.move(dragon_current_location, dragon_old_location)
        elif dragon_dist <= 7 and dragon_dist > 4:
            if Probability.generate() <= 30:
                random_moves = sample(gs.VALID_MOVES, 4)
                for num in range(4):
                    chosen_direction = random_moves[num]
                    self.location = dragon_old_location.copy()
                    dragon_current_location = self.move_character(chosen_direction)
                    if Tools.calculate_distance(player_location, dragon_current_location)\
                        < dragon_old_dist:
                        break
                    elif num == 3:
                        self.location = dragon_old_location.copy()
                        dragon_current_location =\
                            self.move(dragon_current_location, dragon_old_location)
            else:
                dragon_current_location = self.move(dragon_current_location, dragon_old_location)
        elif dragon_dist <= 4:
            if Tools.calculate_distance(player_location, self.location) != 0:
                if Probability.generate() <= 90:
                    random_moves = sample(gs.VALID_MOVES, 4)
                    for num in range(4):
                        chosen_direction = random_moves[num]
                        self.location = dragon_old_location.copy()
                        dragon_current_location = self.move_character(chosen_direction)
                        if Tools.calculate_distance(player_location, dragon_current_location)\
                            < dragon_old_dist:
                            break
                        elif num == 3:
                            self.location = dragon_old_location.copy()
                            dragon_current_location =\
                                self.move(dragon_current_location, dragon_old_location)
                else:
                    dragon_current_location = self.move(dragon_current_location, dragon_old_location)
        return self.location

    def escape_mode_move(self, player_location):
        dragon_dist = Tools.calculate_distance(self.location, player_location)
        dragon_old_dist = dragon_dist
        dragon_current_location = self.location
        dragon_old_location = self.location.copy()        
        if dragon_dist > 7:
            dragon_current_location = self.move(dragon_current_location, dragon_old_location)
        elif dragon_dist <= 7 and dragon_dist > 4:
            if Probability.generate() <= 30:
                random_moves = sample(gs.VALID_MOVES, 4)
                for num in range(4):
                    chosen_direction = random_moves[num]
                    self.location = dragon_old_location.copy()
                    dragon_current_location = self.move_character(chosen_direction)
                    if Tools.calculate_distance(player_location, dragon_current_location)\
                        > dragon_old_dist:
                        break
                    elif num == 3:
                        self.location = dragon_old_location.copy()
                        dragon_current_location =\
                            self.move(dragon_current_location, dragon_old_location)
            else:
                dragon_current_location = self.move(dragon_current_location, dragon_old_location)
        elif dragon_dist <= 4:
            if Tools.calculate_distance(player_location, self.location) != 0:
                if Probability.generate() <= 70:
                    random_moves = sample(gs.VALID_MOVES, 4)
                    for num in range(4):
                        chosen_direction = random_moves[num]
                        self.location = dragon_old_location.copy()
                        dragon_current_location = self.move_character(chosen_direction)
                        if Tools.calculate_distance(player_location, dragon_current_location)\
                            > dragon_old_dist:
                            break
                        elif num == 3:
                            self.location = dragon_old_location.copy()
                            dragon_current_location =\
                                self.move(dragon_current_location, dragon_old_location)
                else:
                    dragon_current_location = self.move(dragon_current_location, dragon_old_location)
        return self.location



