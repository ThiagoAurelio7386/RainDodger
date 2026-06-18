import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_WIDTH, MENU_OPTION, C_WHITE, C_YELLOW, C_YELLOW2, MENU_OPTION2


class Victory:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Asset/VictoryScreen.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def show_victory(self):
        pygame.mixer_music.load('./Asset/Score (Menu).mp3') #Musica
        pygame.mixer_music.play(-1)
        menu_option = 0
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect) #texto da tela de vitória
            self.menu_text(50, "YOU WIN!!!", C_YELLOW2, ((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTION2)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION2[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(30, MENU_OPTION2[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha janela
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Faz menu descer quando a seta "\/" é pressionada
                        if menu_option < len(MENU_OPTION2) - 1:
                            menu_option += 1

                    if event.key == pygame.K_UP:  #Faz menu subir quando a tecla "^" é pressionada
                        if menu_option > 0:
                            menu_option -= 1

                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION2[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)