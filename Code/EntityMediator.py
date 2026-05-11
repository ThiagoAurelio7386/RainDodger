from Code.Const import WIN_HEIGHT
from Code.Gota import Gota
from Code.Entity import Entity
from Code.Player import Player

class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        # só aplica para gotas
        if isinstance(ent, Gota) and ent.rect.top >= WIN_HEIGHT:
            ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = (
            (isinstance(ent1, Player) and isinstance(ent2, Gota)) or
            (isinstance(ent1, Gota) and isinstance(ent2, Player))
        )

        if valid_interaction and ent1.rect.colliderect(ent2.rect):
            ent1.health -= ent2.damage
            ent2.health -= ent1.damage

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        # recria a lista apenas com entidades vivas
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]
