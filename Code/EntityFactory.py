import random
from Code.Background import Background
from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Gota import Gota
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
            #case 'VictoryScreen':
              #  list_bg = []
               # for i in range(1):
                    #list_bg.append(Background(f'VictoryScreen', (0, 0)))
                #return list_bg
            case 'Player':
                return Player('Player', (215, WIN_HEIGHT / 1.4 - 8)) #define posição do player, centrado
            case 'Gota':
                return Gota('Gota', (random.randint(20, WIN_WIDTH - 40), -10))
