import pygame
from config import * 

class SideWall(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/map_textures/sidewall.png')
        self.image = pygame.transform.scale(self.image, (20, 25)).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
    
class Wall(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/map_textures/wall.png')
        self.image = pygame.transform.scale(self.image, (25, 25)).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
    
class Floor(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/map_textures/floor_dark.png')
        self.image = pygame.transform.scale(self.image, (25, 25)).convert_alpha()
        self.image.set_alpha(50)
        self.rect = self.image.get_rect(topleft=position)

class Laser_x(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/map_textures/laser-x.png')
        self.image = pygame.transform.scale(self.image, (25,9)).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class Gun_x(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/map_textures/laser-gun-x.png')
        self.image = pygame.transform.scale(self.image, (20,15)).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class Laser_y(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/map_textures/laser-y.png')
        self.image = pygame.transform.scale(self.image, (9,25)).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class Gun_y(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/map_textures/laser-gun-y.png')
        self.image = pygame.transform.scale(self.image, (15,25)).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class Diamond(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/props/diamond.png')
        self.image = pygame.transform.scale(self.image, (35,25)).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

