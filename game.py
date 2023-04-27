import pygame
from sprites.player import *
from config import *
from sprites.map_content import *

class Game:
    
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Genius Heist')

        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.map = MAP
        self.mapa()

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    def mapa(self):
        basex = SCREEN_WIDTH // 2 - (len(MAP[0]) * WALL_GAP) // 2
        basey = SCREEN_HEIGHT // 2 - (len(MAP) * WALL_GAP) // 2
        for line_index, line in enumerate(MAP):
            for column_index, column in enumerate(line):
                x = basex + column_index * WALL_GAP 
                y = basey + line_index  * WALL_GAP
                if column == 'X':
                    Wall((x, y), self.walls)
                if column == 'S':
                    SideWall((x, y), self.walls)
                if column == ' ':
                    Floor((x, y), self.sprites)
                if column == '1':
                    Floor((x, y), self.sprites)
                    self.player1 = Player1((x, y), self.players)
                if column == '2':
                    Floor((x, y), self.sprites)
                    self.player2 = Player2((x, y), self.players)

    def desenha(self):
        self.window.fill((30,30,65))
        self.walls.draw(self.window)
        self.sprites.draw(self.window)
        self.players.draw(self.window)         
        pygame.display.update()  
        
    def start(self):
        while self.atualiza_estado():
            self.player1.move(self.walls)
            self.player2.move(self.walls)
            self.desenha()