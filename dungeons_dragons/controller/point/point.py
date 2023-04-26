class Point:
    """
    This class initialize points thats can be use as a
    location for game characters
    """
    def __init__(self, X_coordinate, Y_coordinate):
        self.X = X_coordinate
        self.Y = Y_coordinate

    def __str__(self):
        return f'({self.X}, {self.Y})'

    def __repr__(self):
        return f'({self.X}, {self.Y})'

    @property
    def X(self) -> str:
        return self.__X

    @X.setter
    def X(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError('The value must be integer!')
        if value < 0:
            raise ValueError("The value can't be negative!")
        self.__X = value

    @property
    def Y(self) -> str:
        return self.__Y

    @Y.setter
    def Y(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError('The value must be integer!')
        if value < 0:
            raise ValueError("The value can't be negative!")
        self.__Y = value

    @property
    def coordinate(self):
        return [self.X, self.Y]
