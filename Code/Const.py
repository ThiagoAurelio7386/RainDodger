
#Este arquivo é basicamente um reservatório de valores constantes, muito util e importante.
import pygame
# C

C_WHITE = (255, 255, 255) #Cores de texto
C_YELLOW = (255, 255, 128)
C_YELLOW2 = (255, 242, 0)
C_YELLOW3 = (255, 255, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = { #Velocidade de movimento das entidades
    'Friend': 4,
    'Player': 3,
    'Gota': 5,
}

ENTITY_HEALTH = { #HP das entidades
    'LevelBackground': 999,
    'Friend': 999,
    'Player': 3,
    'Gota': 1,
}

ENTITY_DAMAGE = { #Dano
    'LevelBackground': 0,
    'Friend': 0,
    'Player': 1,
    'Gota': 1,
}

# M
MENU_OPTION = ('START GAME', #Opções
               'EXIT')

#P
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT} #Controles
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT}

# S
SPAWN_TIME = 1000

# T
TIMEOUT_STEP = 100 #100ms
TIMEOUT_LEVEL = 20000 #20s #20000

# W
WIN_WIDTH = 500
WIN_HEIGHT = 500