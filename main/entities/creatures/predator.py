from entities.base_classes.creature import Creature
from entities.creatures.herbivore import Herbivore
from search_algorithm.bfs import Bfs
import random

class Predator(Creature):
    """
    A predator creature that hunts herbivores.
    Uses BFS for pathfinding and has attack mechanics.
    """
    def __init__(self, x, y, health_bar, speed, bite_power):
        super().__init__(x, y, health_bar, speed)
        self.__bite_power = bite_power
        self.__path = None
        self.__path_ttl = 0

    def make_move(self, map_obj):
        """Predator step"""
        if self.__path_ttl <= 0 or not self.__path:
            self.__path = self.find_prey(map_obj)
            self.__path_ttl = 3
        else:
            self.__path_ttl -= 1
            
        
        if self.__path is None:
            return
            
        next_coords = self.__path[0]
        
        if self.is_prey(next_coords, map_obj):
            print("Хищник нашел травоядного")
            if self.attack(next_coords, map_obj):
                print("Хищник сьел травоядного")
                self.__path = None  
                return
        
        try:
            map_obj.move_entity(self.coords, next_coords)
            self.__path.pop(0) 
            if not self.__path:  
                self.__path = None
        except ValueError:
            self.__path = None

    def find_prey(self, map_obj):
        """Search path to prey"""
        bfs = Bfs()
        return bfs.bfs_find_path(self.coords, self.is_prey, map_obj)

    def is_prey(self, coords, map_obj):
        entity = map_obj.get_entity(coords)
        return isinstance(entity, Herbivore)

    def attack(self, coords, map_obj):
        prey = map_obj.get_entity(coords)
        if isinstance(prey, Herbivore):
            prey.health_bar -= self.bite
            print("Хищник атаковал")
            
            if prey.health_bar <= 0:
                map_obj.del_entity(coords)
                try:
                    map_obj.move_entity(self.coords, coords)
                except ValueError:
                    return False

                self.health_bar = min(self.health_bar + 20, 100)
                self.hunger = 0
                return True
        return False  

    @property
    def bite(self):
        return self.__bite_power