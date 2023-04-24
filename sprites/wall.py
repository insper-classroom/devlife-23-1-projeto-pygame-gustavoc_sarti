import pygame

class Wall:
    def __init__(self):
        pygame.image.load('assets/images/hexagon.png')
        self.rect = self.image.get_rect()