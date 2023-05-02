import pygame as pyg


class Player1(pyg.sprite.Sprite):

    def __init__(self, position, group):
        super().__init__(group)
        self.player = pyg.image.load('assets/images/players/player_01-pre_dash.png')
        self.image = pyg.transform.scale(self.player, (30, 50)).convert_alpha()
        self.rect = self.image.get_rect(topleft = position) #posicao sera igual ao ponto de origem do retangulo
        self.state = {
            'moving' : False,
        }
        self.direction = [0, 0]
        self.speed = 17
        self.dash_sound = pyg.mixer.Sound('assets/sounds/player_sounds/ogg/dash-high_volume.ogg')
        self.dash_sound.set_volume(0.1)
        self.timer = 0

    def move(self, walls, guns): 
        keys = pyg.key.get_pressed()
        if not self.state['moving']:
            if keys[pyg.K_UP]:
                self.direction[1] = -1
                self.dash_sound.play()
            elif keys[pyg.K_DOWN]:
                self.direction[1] = 1
                self.dash_sound.play()
            elif keys[pyg.K_LEFT]:
                self.direction[0] = -1
                self.dash_sound.play()
            elif keys[pyg.K_RIGHT]:
                self.direction[0] = 1
                self.dash_sound.play()

# chat GPT sugeriu a ideia do old_rect
        if any(self.direction):
            self.state['moving'] = True
            self.player = pyg.image.load('assets/images/players/player_01-dash.png')
            self.image = pyg.transform.scale(self.player, (30, 50)).convert_alpha()
            self.timer = pyg.time.get_ticks()
        if self.state['moving'] == False:
            self.animation()
            
        old_rect = self.rect.copy()
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
    
        collide_walls = pyg.sprite.spritecollide(self, walls, False)
        for collide in collide_walls:
            self.rect = old_rect
            self.direction = [0, 0]
            self.state['moving'] = False
            break
        
        collide_guns = pyg.sprite.spritecollide(self, guns, False)
        for collide in collide_guns:
            self.direction = [0, 0]
            self.state['moving'] = False    
# ate aqui

    #Função responsavel por realizar a troca de sprites do player ao se movimentar
    def animation(self):
        if pyg.time.get_ticks() <=  self.timer + 200:
            self.player = pyg.image.load('assets/images/players/player_01-post_dash.png')
            self.image = pyg.transform.scale(self.player, (40, 60)).convert_alpha()
        else:
            self.player = pyg.image.load('assets/images/players/player_01-pre_dash.png')
            self.image = pyg.transform.scale(self.player, (30, 50)).convert_alpha()



class Player2(pyg.sprite.Sprite):
    
    def __init__(self, position, group):
        super().__init__(group)
        self.player = pyg.image.load('assets/images/players/player_02-pre_dash.png')
        self.image = pyg.transform.scale(self.player, (30, 50)).convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.state = {
            'moving' : False,
        }
        self.direction = [0, 0]
        self.speed = 17
        self.dash_sound = pyg.mixer.Sound('assets/sounds/player_sounds/ogg/dash-high_volume.ogg')
        self.dash_sound.set_volume(0.1)
        self.timer = 0
        

    def move(self, walls, guns):
        keys = pyg.key.get_pressed()
        if not self.state['moving']:
            if keys[pyg.K_w]:
                self.direction[1] = -1
                self.dash_sound.play()
            elif keys[pyg.K_s]:
                self.direction[1] = 1
                self.dash_sound.play()
            elif keys[pyg.K_a]:
                self.direction[0] = -1
                self.dash_sound.play()
            elif keys[pyg.K_d]:
                self.direction[0] = 1
                self.dash_sound.play()

# chat GPT sugeriu a ideia do old_rect    
        if any(self.direction):
            self.state['moving'] = True
            self.player = pyg.image.load('assets/images/players/player_02-dash.png')
            self.image = pyg.transform.scale(self.player, (30, 50)).convert_alpha()
            self.timer = pyg.time.get_ticks()
        if self.state['moving'] == False:
            self.animation()
            
        old_rect = self.rect.copy()
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
    
        collide_walls = pyg.sprite.spritecollide(self, walls, False)
        for collide in collide_walls:
            self.rect = old_rect
            self.direction = [0, 0]
            self.state['moving'] = False
            break
        
        collide_guns = pyg.sprite.spritecollide(self, guns, False)
        for collide in collide_guns:
            self.direction = [0, 0]
            self.state['moving'] = False
# ate aqui

    #Função responsavel por realizar a troca de sprites do player ao se movimentar
    def animation(self):
        if pyg.time.get_ticks() <=  self.timer + 200:
            self.player = pyg.image.load('assets/images/players/player_02-post_dash.png')
            self.image = pyg.transform.scale(self.player, (40, 60)).convert_alpha()
        else:
            self.player = pyg.image.load('assets/images/players/player_02-pre_dash.png')
            self.image = pyg.transform.scale(self.player, (30, 50)).convert_alpha()
