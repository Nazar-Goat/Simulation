from actions.action import Action
from entities.base_classes.creature import Creature

class MoveAction(Action):
    def execute(self, map_obj):
        """Moves all creatures on the map"""
        entities = list(map_obj.get_entities().values())
        
        for entity in entities:
            if isinstance(entity, Creature):
                entity.update_current_speed()
                while entity.current_speed != 0:

                    entity.make_move(map_obj)
                    entity.current_speed -= 1
                
                    if entity.health_bar <= 0:
                        print("Существо умерло от голода")
                        map_obj.del_entity(entity.coords)
                        break