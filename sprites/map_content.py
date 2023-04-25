import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, position, group):

        super().__init__(group)
        self.image = pygame.image.load('assets/images/parede.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect(topleft=position)
    
