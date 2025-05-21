from actions.action import Action
from entities.creatures.herbivore import Herbivore
from entities.creatures.predator import Predator
import random

class ReproductionAction(Action):
    """Action for the reproduction of creatures"""
    def __init__(self, amount_to_create=2):
        self.__amount_to_create = amount_to_create

    def execute(self, map_obj):
        entities = list(map_obj.get_entities().values())
        
        herbivores = [e for e in entities if isinstance(e, Herbivore)]
        predators = [e for e in entities if isinstance(e, Predator)]
        
        for _ in range(self.__amount_to_create):
            if len(herbivores) <= 5:  
                for herbivore in herbivores:  
                        
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    random.shuffle(directions)
                        
                    for dx, dy in directions:
                        nx, ny = herbivore.x + dx, herbivore.y + dy
                        if (0 <= nx < map_obj.width and 
                            0 <= ny < map_obj.height and 
                            not map_obj.if_exist((nx, ny))):
                            map_obj.put_entity(Herbivore(nx, ny, health_bar=100, speed=2))
                            print("Было создано новое травоядное")
                            break
            
            if len(predators) <= 4:  
                for predator in predators:
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    random.shuffle(directions)
                        
                    for dx, dy in directions:
                        nx, ny = predator.x + dx, predator.y + dy
                        if (0 <= nx < map_obj.width and 
                            0 <= ny < map_obj.height and 
                            not map_obj.if_exist((nx, ny))):
                            map_obj.put_entity(Predator(nx, ny, health_bar=100, speed=2, bite_power=25))
                            predator.health_bar -= 40  # Родитель теряет здоровье
                            print("Был создан новый хищник")
                            break
