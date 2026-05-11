from Code.Const import ENTITY_SPEED
from Code.Entity import Entity
class Enemy(Entity):

    def __init__(self, name: str, position: tuple): #basico do inimigo
        super().__init__(name, position)

    def move(self, ):
        self.rect.centery -= ENTITY_SPEED[self.name] # Movimento inteiramente vertical