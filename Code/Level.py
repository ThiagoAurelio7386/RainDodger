import pygame
from pygame import Surface, Rect
from pygame.font import Font
from Code.Const import C_WHITE, WIN_HEIGHT, C_YELLOW3, EVENT_ENEMY, EVENT_TIMEOUT, C_YELLOW
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory
from Code.EntityMediator import EntityMediator
from Code.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LevelBackground'))  # instancia todos os objetos desejados
        self.entity_list.append(EntityFactory.get_entity('Player'))  # coloca o jogador
        self.timeout = 10000  # jogo deve durar 30 segundos
        pygame.time.set_timer(EVENT_TIMEOUT, 100)   # parte do timer
        pygame.time.set_timer(EVENT_ENEMY, 500)     # spawna gotas

    def run(self):
        pygame.mixer_music.load('./Asset/Level2 (Level Music).mp3')  # Musica
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)  # fps mantem velocidade estavel
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Gota'))
                elif event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout <= 0:
                        return None # parte do victory

            found_player = False  # verifica se o player está vivo
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True

            if not found_player:  # se o player morrer, volta pro menu principal
                return False

            for ent in self.entity_list:  # pega as imagens necessárias
                ent.move()
                if ent.name == 'Player':
                    self.level_text(30, f'HP: {ent.health}', C_YELLOW, (10, WIN_HEIGHT - 60))
                self.window.blit(ent.surf, ent.rect)

            time_left = self.timeout / 1000 #segundos
            if time_left <= 5:  # alterna a cor nos ultimos 5s
                if int(pygame.time.get_ticks() / 500) % 2 == 0:
                    color = C_WHITE
                else:
                    color = C_YELLOW3
            else:
                color = C_WHITE

            self.level_text(30, f'[TEMPO: {time_left:.1f}s]', color, (165, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', (255, 255, 255), (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', (255, 255, 255), (10, WIN_HEIGHT - 20))
            pygame.display.flip() #Nos textos acima timeout mostra a duração da fase, fps coloca o fps na tela, entidades mostra entidades
            #ENTIDADES_TEXT É APENAS PARA DEV TESTS, DESATIVAR ANTES DE PUBLICAR

            EntityMediator.verify_collision(entity_list=self.entity_list)   # verificação de colisão
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
