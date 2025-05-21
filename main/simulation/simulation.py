from maps.my_map import Map
from actions.init_action import InitAction
from actions.move_action import MoveAction
from simulation.render import ConsoleRenderer
from entities.creatures.herbivore import Herbivore
from entities.creatures.predator import Predator
from entities.resources.grass import Grass
from actions.reproductive_action import ReproductionAction
from actions.reqrowth_action import RegrowAction


class Simulation:
    def __init__(self, width=20, height=20):
        print(f"Создание карты {width}x{height}...")
        self.map = Map(height, width)
        self.turn = 0
        
        print("Инициализация действий...")
        self.init_actions = [
            InitAction(resources_amount=30, herbivores_amount=15, predators_amount=5)
        ]
        
        self.turn_actions = [
            MoveAction(),
            RegrowAction(grass_growth_rate=5),
            ReproductionAction(amount_to_create= 5)
        ]
        
        print("Генерация начального мира...")
        for action in self.init_actions:
            action.execute(self.map)
        
        print(f"Создано: {len(self.map.get_entities())} объектов")

    def next_turn(self):
        self.turn += 1
        print(f"\nХод {self.turn}:")
        
        for action in self.turn_actions:
            action_name = action.__class__.__name__
            print(f" > Выполнение {action_name}...")
            action.execute(self.map)
        
        print("\nТекущее состояние:")
        ConsoleRenderer.render(self.map)
        
        self.print_stats()
    
    def print_stats(self):
        stats = {
            "Herbivores": 0,
            "Predators": 0,
            "Grass": 0,
            "Rocks/Trees": 0
        }
        
        for entity in self.map.get_entities().values():
            if isinstance(entity, Herbivore):
                stats["Herbivores"] += 1
            elif isinstance(entity, Predator):
                stats["Predators"] += 1
            elif isinstance(entity, Grass):
                stats["Grass"] += 1
            else:
                stats["Rocks/Trees"] += 1
                
        print("Stats:", stats)
