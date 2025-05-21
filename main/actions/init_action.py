from actions.action import Action
from entities.creatures.herbivore import Herbivore
from entities.creatures.predator import Predator
from entities.resources.grass import Grass
from entities.resources.tree import Tree
from entities.resources.rock import Rock
import random

class InitAction(Action):
    """Initial spawn action of creatures and resources"""
    def __init__(self, resources_amount, 
                 herbivores_amount, 
                 predators_amount):
        self.__resources = resources_amount
        self.__herbivores = herbivores_amount
        self.__predators = predators_amount

    def execute(self, map_obj):
        self.generate_herbivores(map_obj)
        self.generate_predators(map_obj)
        self.generate_resources(map_obj)

    def generate_resources(self, map_obj):
        for _ in range(self.__resources):
            x, y = self.get_random_coords(map_obj)
            num = random.randint(0, 3)
            if num == 1:
                map_obj.put_entity(Grass(x, y))
            elif num == 2:
                map_obj.put_entity(Rock(x, y))
            elif num == 3:
                map_obj.put_entity(Tree(x, y))

    def generate_predators(self, map_obj):
        for _ in range(self.__predators):
            x, y = self.get_random_coords(map_obj)
            map_obj.put_entity(Predator(x, y, health_bar=100, speed=3, bite_power=25))

    def generate_herbivores(self, map_obj):
        for _ in range(self.__herbivores):
            x, y = self.get_random_coords(map_obj)
            map_obj.put_entity(Herbivore(x, y, health_bar=100, speed=3))

    def get_random_coords(self, map_obj):
        x = random.randint(0, map_obj.width - 1)
        y = random.randint(0, map_obj.height - 1)

        while map_obj.if_exist((x, y)):
            x = random.randint(0, map_obj.width - 1)
            y = random.randint(0, map_obj.height - 1)
        return (x, y)