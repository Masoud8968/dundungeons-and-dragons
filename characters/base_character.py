from typing import Optional
from helper import exceptions as exc

class BaseCharacter:
    """
    This is Base class of any characters that exist in game world.
    all of characters like user(the person that wants to play the game),
    dragon(the player's enemy),
    game characters (like player (the character that user controls him ),
    and some other characters)inherit from this class
    """
    def __init__(self, name: str, family: Optional[str] = ' '):
        self.name = name
        self.family = family

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise exc.NameLengthError()      
        self.__name = value

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        if value[0].isdigit():
            raise exc.FamilyLengthError()       
        self.__family = value



