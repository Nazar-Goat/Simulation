from actions.action import Action
from entities.resources.grass import Grass
import random

class RegrowAction(Action):
    """Action to add new resources to the map"""
    def __init__(self, grass_growth_rate=2):
        self.__grass_growth_rate = grass_growth_rate
        
    def execute(self, map_obj):
        grass_count = sum(1 for entity in map_obj.get_entities().values() 
                          if isinstance(entity, Grass))
        
        for _ in range(self.__grass_growth_rate):
            if  grass_count >= 10:
                break  
                
            x = random.randint(0, map_obj.width - 1)
            y = random.randint(0, map_obj.height - 1)
                
            for _ in range(10):
                if not map_obj.if_exist((x, y)):
                    map_obj.put_entity(Grass(x, y))
                    grass_count += 1
                    print("Добавлена новая трава")
                    break
                x = random.randint(0, map_obj.width - 1)
                y = random.randint(0, map_obj.height - 1)