import pygame

class SideWall(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/sidewall.png')
        self.image = pygame.transform.scale(self.image, (20, 25))
        self.rect = self.image.get_rect(topleft=position)
    
class Wall(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/wall.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect(topleft=position)
    
class Floor(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/images/floor_dark.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.image.set_alpha(50)
        self.rect = self.image.get_rect(topleft=position)