from entities.base_classes.entity import Entity

class Creature(Entity):
    def __init__(self, x, y, health_bar, speed):
        """
        The base class from which all creatures will inherit
        Param x: parameter of object placement on map row
        Param y: parameter of object placement on map column
        Param health_bar: creatures health amount
        Param speed: The number of cells a creature can move in one turn.
        """
        super().__init__(x, y)
        self.check_value(health_bar)
        self.check_value(speed)
        self.__health_bar = health_bar
        self.__speed = speed
        self.__current_speed = speed
        self.__hunger = 0  # Добавляем голод

    @property
    def health_bar(self):
        return self.__health_bar
    
    @health_bar.setter
    def health_bar(self, value):
        self.__health_bar = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value
        
    @property
    def hunger(self):
        return self.__hunger
        
    @hunger.setter
    def hunger(self, value):
        self.__hunger = max(0, value)

    @property
    def current_speed(self):
        return self.__current_speed
    
    @current_speed.setter
    def current_speed(self, value):
        self.__current_speed = value
    
    def update_current_speed(self):
        self.__current_speed = self.__speed

    @classmethod
    def check_value(cls, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("Wrong type or value for health or speed")
        
    def make_move(self, map_obj):
        pass
        
    def update_state(self):
        self.hunger += 1
        if self.hunger > 3:  
            self.health_bar -= 10  
            self.hunger = 0