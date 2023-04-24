import pygame
from sprites.player import *
from config import *
from sprites.wall import Wall


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Genius Heist')
      
        self.sprites = pygame.sprite.Group()
        self.map = MAP
        self.mapa()

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    def mapa(self):
        for line_index, line in enumerate(MAP):
            for column_index, column in enumerate(line):
                if column == 'X':
                    Wall((column_index, line_index), self.sprites)
                if column == 'p':
                    self.player = Player((column_index, line_index), self.sprites)

    def desenha(self):
        # self.window.fill((0, 0, 0))
         
        self.sprites.draw(self.window)           
        pygame.display.update()  
        # self.player.draw()
        

    def start(self):
        while self.atualiza_estado():
            self.desenha()
