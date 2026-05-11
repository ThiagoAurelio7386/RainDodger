import random

from Code.Background import Background
from Code.Const import WIN_WIDTH, WIN_HEIGHT
#from Code.Enemy import Enemy
from Code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'LevelBackground':
                list_bg = []
                for i in range(1): #lista com assets que compõem o Background, um pouco redundante, é a única forma que conheço
                    list_bg.append(Background(f'LevelBackground', (0, 0)))
                    # list_bg.append(Background(f'LevelBackground{i}')) #GENERICA, USE APENAS SE ACIMA NÃO FUNCIONAR
                return list_bg
            #case 'Player':
                #return Player('Player', (10, WIN_HEIGHT / 2 - 30)) #define posição do player, neste projeto esta no meio do canto esquerdo
        #    case 'Player2':
         #       return Player('Player2', (10, WIN_HEIGHT / 2 + 30))  # define posição do player, neste projeto esta no meio do canto esquerdo
           # case 'Enemy':
                #return Enemy('Enemy',(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
