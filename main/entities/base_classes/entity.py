class Entity:
    def __init__(self, x, y):
        """
        The root class from which all other classes inherit.
        Param x: parameter of object placement on map row
        Param y: parameter of object placement on map column
        Param __coords: tuple with object coordinates on game pole
        """
    
        self.__x, self.__y = self.check_coords(x, y)
        self.__coords = (self.__x, self.__y)

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.check_value(value)
        self.__x = value
        self.__coords = (self.__x, self.__y)

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.check_value(value)
        self.__y = value
        self.__coords = (self.__x, self.__y)

    @property
    def coords(self):
        return self.__coords
    
    @coords.setter
    def coords(self, new_coords):
        x, y = new_coords
        self.check_coords(x, y)
        self.__x = x
        self.__y = y
        self.__coords = (self.__x, self.__y)

    @classmethod
    def check_value(cls, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Wrong type or variable value")

    @classmethod
    def check_coords(cls, x, y):
        if not isinstance(x, int) or not isinstance(y, int) or \
           x < 0 or y < 0:
            raise ValueError("Wrong types or values for coordinates")
        return x, y