import pygame
class Game:
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode((1024, 720), vsync=True, flags=pygame.SCALED)
    def start():
        while atualiza_estado(state):
            desenha(window, tabuleiro, state)

game = Game()
game.start()