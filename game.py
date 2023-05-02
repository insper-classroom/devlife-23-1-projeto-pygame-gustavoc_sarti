import pygame
from sprites.player import *
from config import *
from sprites.map_content import *
import functions

#Timer
class Timer:
    def __init__(self, timer):
        self.clock = pygame.time.Clock()
        self.start = timer
        self.clock.tick(100)

    def time(self):
        self.start -= 1
        if self.start <= 0:
            return False
        return True
    #GPT
    def get_time_string(self):
        remaining_time = max(0, self.start)
        minutes = remaining_time // 6000
        seconds = (remaining_time // 100) % 60
        milliseconds = remaining_time % 100
        return f"Time: {minutes:02d}:{seconds:02d}:{milliseconds:02d}"
    #----
    def get_score(self):
        remaining_time = max(0, self.start)
        if remaining_time > self.start//2:
            score = [1,1,1]
        elif remaining_time > self.start//4:
            score = [1,1]
        else:
            score = [1]
        return score


#Jogo
class Game:
    def __init__(self):
        #Init do jogo
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.lasers_x = pygame.sprite.Group()
        self.lasers_y = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.guns = pygame.sprite.Group()
        self.map = MAP1
        self.mapa()
        self.timer = Timer(TIMER1)
        
        self.defeat = False
        self.victory = False
        self.nivel = ['menu','nivel1','nivel2','nivel3', 'win_screen', 'game_over']
        self.atual = 0
        #Start music
        pygame.mixer.music.load('assets/sounds/sounds_misc/ogg/background_music.ogg')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.08)
        self.win_sound = pygame.mixer.Sound('assets/sounds/sounds_misc/ogg/victory_music.ogg')
        self.win_sound.set_volume(0.1)


        #Init do menu
        #Configura os botões
        self.button = pygame.image.load('assets/images/menu/button_unselected.jpg')
        self.button_victory = pygame.image.load('assets/images/menu/button_selected.jpg')
        self.button = pygame.transform.scale(self.button, (240, 80))
        self.button_victory = pygame.transform.scale(self.button, (240, 80))
        self.button_width, self.button_height = self.button.get_size()



        #Configura as imagens de fundo
        background = pygame.image.load('assets/images/menu/bank-pygame.png')
        self.background = pygame.transform.scale(background,(1420,969))
        background_win = pygame.image.load('assets/images/menu/win.png')
        self.background_win = pygame.transform.scale(background_win,(1420,969))
        
        #Configura texto dos botões e menus
        self.botoes = ['jogar','tutorial','sair', 'MENU!']
        self.fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(self.fonte_padrao, 45)
        self.fonte_titulo = pygame.font.Font(self.fonte_padrao, 100)
        self.titulo = self.fonte_titulo.render('GENIUS HEIST', True, (0,0,0))
        self.titulo_win = self.fonte.render('Você Escapou!', True, (0, 0, 0))

    def atualiza_estado(self):
        self.mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.nivel[self.atual] == 'menu':
                if functions.clique_jogar(self,SCREEN_WIDTH,SCREEN_HEIGHT):
                    self.atual +=1

                if functions.clique_tutorial(self,SCREEN_WIDTH,SCREEN_HEIGHT):
                    return False
                if functions.clique_sair(self,SCREEN_WIDTH,SCREEN_HEIGHT):
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and self.nivel[self.atual] == 'menu':
                if functions.clique_jogar(self,SCREEN_WIDTH,SCREEN_HEIGHT):
                    self.atual = 0

        functions.player_hit(self)
        functions.laser_break(self)

        return True
    
    #Cria o mapa do jogo
    def mapa(self):
        basex = SCREEN_WIDTH // 2 - (len(self.map[0]) * WALL_GAP) // 2
        basey = SCREEN_HEIGHT // 2 - (len(self.map) * WALL_GAP) // 2
        for line_index, line in enumerate(self.map):
            for column_index, column in enumerate(line):
                x = basex + column_index * WALL_GAP 
                y = basey + line_index  * WALL_GAP
                if column == 'X':
                    Wall((x, y), self.walls)
                if column == 'S':
                    SideWall((x, y), self.walls)
                if column == ' ' or column == '1' or column == '-' or column == '8' or column == 'I' or column == 'L' or column == '2':
                    Floor((x, y), self.sprites)
                if column == '1':
                    self.player1 = Player1((x, y), self.players)
                if column == '2':
                    self.player2 = Player2((x, y), self.players)
                if column == '-':
                    Laser_x((x, y), self.lasers_x)
                if column == '8':
                    Gun_x((x, y), self.guns)
                if column == 'I':
                    Laser_y((x, y), self.lasers_y)
                if column == 'L':
                    Gun_y((x, y), self.guns)
                if column == 'D':
                    Diamond((x, y), self.sprites)

    #Função de RESET, serve para resetar TODAS as variaveis(init) de toda a classe e funções para assim reiniciar o jogo.
    def reset(self):
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.lasers_x = pygame.sprite.Group()
        self.lasers_y = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.guns = pygame.sprite.Group()
        if self.nivel[self.atual] == 'nivel1':
            self.map = MAP2
            self.timer = Timer(TIMER2)
        if self.nivel[self.atual] == 'nivel2':
            self.map = MAP3
            self.timer = Timer(TIMER3)
        self.mapa()
        self.defeat = False
        self.victory = False


    def desenha(self):
        #Desenha os niveis do jogo
        if self.nivel[self.atual] == 'nivel1' or self.nivel[self.atual] == 'nivel2' or self.nivel[self.atual] == 'nivel3':
            self.window.fill((30,30,65))
            self.walls.draw(self.window)
            self.sprites.draw(self.window)
            self.players.draw(self.window)
            self.lasers_x.draw(self.window)
            self.lasers_y.draw(self.window)
            self.guns.draw(self.window)
            #GPT + stackoverflow
            self.timer.clock.tick(100)
            time_text = self.timer.get_time_string()
            font = pygame.font.Font(None, 36)
            text = font.render(time_text, True, (255, 255, 255))
            self.window.blit(text, (10, 10))
            #----
            score = self.timer.get_score()
            for i in range(3):
                if i < len(score):
                    self.window.blit(STAR, (SCREEN_WIDTH - 300 - i * 30, 50))
                else:
                    self.window.blit(NULL_STAR  , (SCREEN_WIDTH - 300 - i * 30, 50))
        pygame.display.update()  

        #Desenha o main menu do jogo
        if self.nivel[self.atual] == 'menu':
            self.window.blit(self.background, (0, 0))
            self.window.blit(self.titulo, (350, 100))
            y_start = (SCREEN_HEIGHT - (len(self.botoes) * (self.button_height + 20))) // 2
            for i, label in enumerate(self.botoes):
                if label != 'MENU!':
                    botao = self.fonte.render(label, True, (255, 255, 255))
                    text_width, text_height = botao.get_size()
                    x_button = (SCREEN_WIDTH - self.button_width) // 2
                    y_button = y_start + i * (self.button_height + 50)
                    x_text = (SCREEN_WIDTH - text_width) // 2
                    y_text = y_button + (self.button_height - text_height) // 2
                    self.window.blit(self.button, (x_button, y_button))
                    self.window.blit(botao, (x_text, y_text))

        #Desenha a victory screen do jogo
        if self.nivel[self.atual] == 'win_screen':
            self.window.blit(self.background_win, (0, 0))
            self.window.blit(self.titulo_win, ((SCREEN_WIDTH - self.titulo_win.get_width()) / 2, 100))
            for i, label in enumerate(self.botoes):
                if label == 'MENU!':
                    text_surface = self.fonte.render(label, True, (255, 255, 255))
                    text_width, text_height = text_surface.get_size()
                    self.x_button = (SCREEN_WIDTH - self.button_width) // 2
                    self.y_button = 300 + (self.button_height + 50)
                    y_text = self.y_button + (self.button_height - text_height) // 2
                    self.window.blit(self.button_victory, (self.x_button, self.y_button))
                    self.window.blit(text_surface, ((SCREEN_WIDTH - text_width) // 2, y_text))

        #Desenha a tela de game over do jogo


# alguns trechos da parte responsavel por resetar o game foi feita pelo GPT        
    def start(self):
        while self.atualiza_estado():
            if self.nivel[self.atual] == 'menu':
                self.desenha()
            if self.timer.time() and self.nivel[self.atual] != 'menu':
                self.player1.move(self.walls, self.guns)
                self.player2.move(self.walls, self.guns)
                self.desenha()
            if self.defeat or self.timer.time() == False and self.nivel[self.atual] != 'win_screen' and self.nivel[self.atual] != 'menu' and self.nivel[self.atual] != 'game_over':
                self.gameover.start()
                self.reset()
            if self.victory:
                self.reset()
                self.atual += 1
