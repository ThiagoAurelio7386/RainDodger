import pygame
from pygame import Surface, Rect
from pygame.font import Font
from Code.Const import C_WHITE, WIN_HEIGHT, C_YELLOW3, EVENT_ENEMY, EVENT_TIMEOUT, EVENT_FRIEND, C_YELLOW
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory
from Code.EntityMediator import EntityMediator
from Code.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LevelBackground'))  # fundo
        self.entity_list.append(EntityFactory.get_entity('Player'))           # jogador
        self.timeout = 3000  # jogo dura 30 segundos (30000)

        # timers
        pygame.time.set_timer(EVENT_TIMEOUT, 100)   # decrementa tempo
        pygame.time.set_timer(EVENT_ENEMY, 500)     # spawna gotas
        pygame.time.set_timer(EVENT_FRIEND, self.timeout - 1000, True) #spawn do amigo, 1 segundo antes do fim

    def run(self):
        pygame.mixer_music.load('./Asset/Level2 (Level Music).mp3') # Musica
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60) #fps mantem velocidade estavel
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Gota'))
                elif event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout <= 0:
                        return None  # vitória
                elif event.type == EVENT_FRIEND:
                    self.entity_list.append(EntityFactory.get_entity('Friend'))

            found_player = any(isinstance(ent, Player) for ent in self.entity_list) # verifica se o player esta vivo
            if not found_player: # se o player morrer, volta pro menu principal
                return False

            for ent in self.entity_list: #pega as imagens necessárias
                ent.move()
                if ent.name == 'Player':
                    self.level_text(30, f'HP: {ent.health}', C_YELLOW, (10, WIN_HEIGHT - 60))
                self.window.blit(ent.surf, ent.rect)

            time_left = self.timeout / 1000 #segundos
            if time_left <= 5:
                color = C_WHITE if int(pygame.time.get_ticks() / 500) % 2 == 0 else C_YELLOW3
            else:
                color = C_WHITE

            self.level_text(30, f'[TEMPO: {time_left:.1f}s]', color, (165, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', (255, 255, 255), (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', (255, 255, 255), (10, WIN_HEIGHT - 20))
            pygame.display.flip() #Nos textos acima timeout mostra a duração da fase, fps coloca o fps na tela, entidades mostra entidades

            EntityMediator.verify_collision(entity_list=self.entity_list) # verificação de colisão
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
