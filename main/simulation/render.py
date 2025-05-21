from entities.creatures.herbivore import Herbivore
from entities.creatures.predator import Predator
from entities.resources.grass import Grass
from entities.resources.rock import Rock
from entities.resources.tree import Tree

class ConsoleRenderer:
    @staticmethod
    def render(map_obj):
        """Displays the current state of the map in the console"""
        grid = [['🟦'] * map_obj.width for _ in range(map_obj.height)]
        
        for coords, entity in map_obj.get_entities().items():
            x, y = coords
            if isinstance(entity, Herbivore):
                grid[y][x] = '🐑'
            elif isinstance(entity, Predator):
                grid[y][x] = '🐺'
            elif isinstance(entity, Grass):
                grid[x][y] = '🌿'
            elif isinstance(entity, Rock):
                grid[y][x] = '⛰️'
            elif isinstance(entity, Tree):
                grid[x][y] = '🌲'
        
        for row in grid:
            print(" ".join(row) + " ")