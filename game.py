import pygame
from sprites.player import *
from config import *
from sprites.wall import Wall


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Genius Heist')
        self.player = Player(pygame.Rect(4, 4, SCREEN_WIDTH, SCREEN_HEIGHT), MAP)
        self.map = MAP

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def desenha(self):
        self.window.fill((0, 0, 0))                
        self.player.draw(self.window, self.pos)
        pygame.display.update()

    def start(self):
        while self.atualiza_estado():
            self.desenha(self.assets, self.state)

    # def map(self):
    #     for line_index, line in enumerate(MAP):
    #         for column_index, column in enumerate(line):
    #             if column == 'X':
                    