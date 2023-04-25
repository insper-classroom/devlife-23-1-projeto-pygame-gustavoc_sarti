import pygame as pyg

class Player(pyg.sprite.Sprite):
    
    def __init__(self, position, group):

        super().__init__(group)
        player = pyg.image.load('assets/images/players/player_01-pre_dash.png')
        self.image = pyg.transform.scale(player, (169, 169))
        self.rect = self.image.get_rect(topleft = position) #posicao sera igual ao ponto de origem do retangulo
        
        self.direction = pyg.math.Vector2(0, 0)
        self.speed = 30
        

    def move(self):
        keys = pyg.key.get_pressed()
        if keys[pyg.K_UP]:
            self.direction.y = -1
        elif keys[pyg.K_DOWN]:
            self.direction.y = 1

        if keys[pyg.K_LEFT]:
            self.direction.x = -1
        elif keys[pyg.K_RIGHT]:
            self.direction = 1
        
        self.rect.move_ip(self.rect.x + self.direction.x * self.speed,
                          self.rect.y + self.direction.y * self.speed)
        
    def collision(self):
        for obj in self.objects:
            if self.rect.colliderect(self.rect):
                self.rect.move_ip(self.rect.x - self.direction.x * self.speed,
                                  self.rect.y - self.direction.y * self.speed)

    def draw(self):
        self.move(self.speed)