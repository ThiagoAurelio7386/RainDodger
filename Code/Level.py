import pygame

from Code.Entity import Entity
from Code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LevelBackground'))  # instancia todos os objetos desejados
       # self.entity_list.append(EntityFactory.get_entity('Player'))  # coloca o jogador

    def run(self, ):
        while True:
            for ent in self.entity_list: #pega as imagens necessárias
                self.window.blit(source=ent.surf, dest=ent.rect)
            pygame.display.flip()
        pass