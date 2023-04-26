from painless.helper.tools import Tools
from dungeons_dragons.controller import GameCharacter


class Sweet:
    @staticmethod
    def generate_sweet(name, icon, dragons_location, player):
        sweet_location = Tools.random_point()
        while (
            sweet_location in dragons_location
            or sweet_location == player.location
        ):
            sweet_location = Tools.random_point()
        sweet = GameCharacter("booster", sweet_location, icon)
        return sweet
