from entities.resources.grass import Grass
from entities.resources.tree import Tree
from entities.resources.rock import Rock

class Map:
    def __init__(self, height, width):
        self.check_height_and_width(height, width)
        self.__height = height
        self.__width = width
        self.__entities = {}

    def get_entities(self):
        return self.__entities
    
    def get_entity(self, coords):
        try:
            if not self.is_valid_coords(coords):
                return None
        except ValueError:
            return None
        return self.__entities.get(coords)
    
    def put_entity(self, entity):
        self.__entities[entity.coords] = entity

    def del_entity(self, coords):
        if coords in self.__entities:
            del self.__entities[coords]

    def move_entity(self, start_coords, final_coords):
        if not self.is_valid_coords(final_coords):
            raise ValueError("Coordinates out of map bounds")
        
        if final_coords in self.__entities:
            raise ValueError("Target coordinates are occupied")
        
        entity = self.get_entity(start_coords)
        if entity is None:
            raise ValueError("No entity at start coordinates")
            
        self.del_entity(start_coords)
        entity.coords = final_coords
        self.put_entity(entity)

    def if_exist(self, coords):
        return coords in self.__entities
    
    def is_valid_coords(self, coords):
        x, y = coords
        return 0 <= x < self.__width and 0 <= y < self.__height
        
    def check_key(self, coords):
        if not self.is_valid_coords(coords):
            raise ValueError("Coordinates out of map bounds")
        if coords not in self.__entities:
            raise ValueError("No such entity")
        
    @classmethod
    def check_height_and_width(cls, height, width):
        if (not isinstance(height, int) or not isinstance(width, int)) or \
           (height <= 0 or width <= 0):
            raise ValueError("Wrong types or values for height, or width")

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height