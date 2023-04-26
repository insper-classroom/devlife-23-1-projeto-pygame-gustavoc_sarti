import pygame as pyg

class Player(pyg.sprite.Sprite):
    
    def __init__(self, position, group):

        super().__init__(group)
        player = pyg.image.load('assets/images/players/player_01-pre_dash.png')
        self.image = pyg.transform.scale(player, (30, 50)).convert_alpha()
        self.rect = self.image.get_rect(center = position) #posicao sera igual ao ponto de origem do retangulo
        self.state = {
            'moving' : False,
        }
        self.direction = [0, 0]
        self.speed = 22
        

    def move(self, walls):
        keys = pyg.key.get_pressed()
        if not self.state['moving']:
            if keys[pyg.K_UP]:
                self.direction[1] = -1
            elif keys[pyg.K_DOWN]:
                self.direction[1] = 1
            elif keys[pyg.K_LEFT]:
                self.direction[0] = -1
            elif keys[pyg.K_RIGHT]:
                self.direction[0] = 1

# chat GPT sugeriu a ideia do old_rect    
        if any(self.direction):
            self.state['moving'] = True

        old_rect = self.rect.copy()
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
    
        collide_walls = pyg.sprite.spritecollide(self, walls, False)
        for collide in collide_walls:
            self.rect = old_rect
            self.direction = [0, 0]
            self.state['moving'] = False
            break
# ate aqui

    def collision(self, walls):
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
        print('player position:', self.rect.center)
        collide_walls = pyg.sprite.spritecollide(self, walls, False)
        for collide in collide_walls:
            print('wall position:', collide.rect.center)
            self.rect.move_ip(-self.direction[0] * self.speed, -self.direction[1] * self.speed)
            self.direction = [0, 0]
            self.state['moving'] = False
            return True
        return False


    def draw(self):
        self.move()