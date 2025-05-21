from entities.base_classes.creature import Creature
from search_algorithm.bfs import Bfs
from entities.resources.grass import Grass
import random

class Herbivore(Creature):
    """
    A class of herbivore that searches for and eats grass.
    Uses BFS to find the path to the nearest grass.
    """
    def __init__(self, x, y, health_bar, speed):
        super().__init__(x, y, health_bar, speed)
        self.__path = None
        self.__path_ttl = 0  # Time to live for path

    def make_move(self, map_obj):
        """Herbivore turn"""
        if self.__path_ttl <= 0 or not self.__path:
            self.__path = self.find_grass(map_obj)
            self.__path_ttl = 3
        else:
            self.__path_ttl -= 1

        if self.__path is None:
            return
            
        next_coords = self.__path[0]
        
        if self.is_grass(next_coords, map_obj):
            if self.eat_grass(next_coords, map_obj):
                self.__path = None 
                return
        
        try:
            map_obj.move_entity(self.coords, next_coords)
            self.__path.pop(0)  
            if not self.__path:  
                self.__path = None
        except ValueError:
            self.__path = None

    def find_grass(self, map_obj):
        """Searcing path to grass"""
        bfs = Bfs()
        return bfs.bfs_find_path(self.coords, self.is_grass, map_obj)

    def is_grass(self, coords, map_obj):
        """Checks if object is grass"""
        entity = map_obj.get_entity(coords)
        return isinstance(entity, Grass)

    def eat_grass(self, coords, map_obj):
        grass = map_obj.get_entity(coords)
        if isinstance(grass, Grass):
            map_obj.del_entity(coords)
            try:
                map_obj.move_entity(self.coords, coords)
                print("Травоядное сьело траву")
            except ValueError:
                return False
            
            self.health_bar = min(self.health_bar + 30, 100)
            self.hunger = 0
            return True
        return False