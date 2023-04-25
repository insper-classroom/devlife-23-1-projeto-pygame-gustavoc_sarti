import pygame
from sprites.player import *
from config import *
from sprites.map_content import *


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
                x = column_index * WALL_GAP 
                y = line_index  * WALL_GAP
                if column == 'X':
                    Wall((x, y), self.sprites)
                if column == 'S':
                    SideWall((x, y), self.sprites)
                if column == ' ':
                    Floor((x, y), self.sprites)
                if column == 'p':
                    Floor((x, y), self.sprites)
                    self.player = Player((x, y), self.sprites)

    def desenha(self):         
        self.sprites.draw(self.window)           
        pygame.display.update()  
        
    def start(self):
        while self.atualiza_estado():
            self.player.move()
            self.desenha()