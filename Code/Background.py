import pygame

from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Entity import Entity

class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        original_image = pygame.image.load('./Asset/LevelBackground.png').convert_alpha() # Carrega a imagem original
        self.image = pygame.transform.scale(original_image, (WIN_WIDTH, WIN_HEIGHT))  # Ajusta para caber
        self.rect = self.image.get_rect(topleft=position) #Atualiza rect

    def move(self):
        pass