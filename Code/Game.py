import pygame


class Game:

    def __init__(self):
        self.window = None

    def run(self, ):
        print('Setup Start')
        pygame.init()
        window = pygame.display.set_mode(size=(600, 480))
        print('Setup End')

        print('Loop Start')
        while True:
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting...')
                    pygame.quit()
                    quit()