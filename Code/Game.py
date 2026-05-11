import pygame

from Code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from Code.Level import Level
from Code.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # tamanho da janela, dados no arquivo const
        pygame.display.set_caption("Rain Dodger")

    def run(self):
        print('Starting...')
        while True:
            menu = Menu(self.window)  # abre mini-janela com o jogo
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
                level = Level(self.window, 'Level', menu_return)
                level_return = level.run()
               # if level_return: Level(self.window, 'Victory', menu_return)
            elif menu_return == MENU_OPTION[1]:
                pygame.quit()  # fecha janela (sai do jogo)
                print('Quitting...')
                quit()  # end pygame
                pass
