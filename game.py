import pygame
from sprites.player import *
from config import *
from wall import *


class Game:
    
    def __init__(self):
        pygame.init()
        bounds = (1024, 720)
        self.window = pygame.display.set_mode(bounds)
        pygame.display.set_caption('Genius Heist')
        self.player = Player(pygame.Rect(4, 4, bounds[0], bounds[1]))


        self.assets = {
            # 'player': pygame.transform.scale(player, (50, 50))
        }
        
        self.state = {

        } 

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    def desenha(self, assets, state):
        self.window.fill((0, 0, 0))                
        self.player.draw(self.window, self.pos)
        pygame.display.update()
        
    def start(self):
        while self.atualiza_estado():
            self.desenha(self.assets, self.state)
class Mapa:
    def __init__(self):
        self.map = MAP
