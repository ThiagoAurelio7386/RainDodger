from Code.Const import ENTITY_SPEED
from Code.Entity import Entity

class Friend(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # movimento simples para a esquerda
        self.rect.x -= ENTITY_SPEED[self.name] # ajusta a velocidade de movimento
