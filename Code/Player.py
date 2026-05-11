import pygame
import pygame.key
from Code.Const import ENTITY_SPEED, WIN_WIDTH, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from Code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple): #basico do player
        super().__init__(name, position)

    def move(self, ): #movimento do jogador
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0: #faz o player ir pra ESQUERDA quando (<) é pressionado, left>0 evita o player sair da tela
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH: #faz o player nave ir pra DIREITA quando (>) é pressionado, WinWidth evita o player sair da tela
            self.rect.centerx += ENTITY_SPEED[self.name]