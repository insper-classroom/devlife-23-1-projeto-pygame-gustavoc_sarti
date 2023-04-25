import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, position, group):

        super().__init__(group)
        self.image = pygame.image.load('assets/images/hexagon.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(topleft=position)
    