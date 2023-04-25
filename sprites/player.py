import pygame as pyg

class Player(pyg.sprite.Sprite):
    
    def __init__(self, position, group):

        super().__init__(group)
        player = pyg.image.load('assets/images/players/player_01-pre_dash.png')
        self.velx = 0
        self.vely = 0
        self.image = pyg.transform.scale(player, (169, 169)).convert_alpha()
        self.rect = self.image.get_rect(topleft = position) #posicao sera igual ao ponto de origem do retangulo
        self.state = {
            'moving' : False,
        }
        
        self.direction = [0, 0]
        self.speed = 30
        

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

        if any(self.direction): #sugestao do chat gpt
            self.state['moving'] = True

        if not self.collision(walls):
            self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
        else:
            self.direction = [0, 0]
            self.state['moving'] = False

    def collision(self, walls):
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
        collide_walls = pyg.sprite.spritecollide(self, walls, False)
        for collide in collide_walls:
            self.rect.move_ip(-self.direction[0] * self.speed, -self.direction[1] * self.speed)
            self.direction = [0, 0]
            self.state['moving'] = False
            return True
        return False


    def draw(self):
        self.move()