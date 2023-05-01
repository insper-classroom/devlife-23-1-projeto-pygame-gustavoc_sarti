import pygame
from sprites.player import *
from config import *
from sprites.map_content import *
import gameover
import level2
import functions

#Timer
# class Timer:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.start = TIMER
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
        if remaining_time > TIMER//2:
            score = [1,1,1]
        elif remaining_time > TIMER//4:
            score = [1,1]
        else:
            score = [1]
        return score

#Jogo
class Level1:
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameover = gameover.Gameover()
        self.level2 = level2.Level2
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.lasers_x = pygame.sprite.Group()
        self.lasers_y = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.guns = pygame.sprite.Group()
        self.map = MAP1
        self.mapa()
        self.timer = Timer()
        self.defeat = False
        self.victory = False

    def atualiza_estado(self,):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        lasered_x = pygame.sprite.groupcollide(self.players, self.lasers_x, False, False, pygame.sprite.collide_rect)
        lasered_y = pygame.sprite.groupcollide(self.players, self.lasers_y, False, False, pygame.sprite.collide_rect)
        if lasered_x or lasered_y:
                self.defeat = True
        

        #Codigo para a remoção dos LASER disparados, feito com auxilio do chatGPT para criar a base e pensar a lõgica.
        #Basicamente ao remover a arma que dispara o laser, tambem pega suas cordenadas(na tela Pygame), as divide pelo
        #tamanho de um 'tile' do mapa, assim descobrindo a posição X,Y do arma(na lista do mapa). Em seguida remove todos
        #os lasers desta fileira ou coluna, configurado manualmente dependendo se é um laser X ou Y.
        lasers_colididos = pygame.sprite.groupcollide(self.players, self.guns, False, True, pygame.sprite.collide_rect)
        for player_sprite, laser_list in lasers_colididos.items():
            for gun_sprite in laser_list:
                #Pega tanto os index X e Y de colisao
                col_index = gun_sprite.rect.x // 40  #40 por ser o tamanho de um tile na tela
                row_index = gun_sprite.rect.y // 40  #40 por ser o tamanho de um tile na tela
                #Remove todos os laser de armas destruidas
                for arma_vertical in self.lasers_y:
                    if arma_vertical.rect.x // 40 == col_index:
                        self.lasers_y.remove(arma_vertical)
                for arma_horizontal in self.lasers_x:
                    if arma_horizontal.rect.y // 40 == row_index:
                        self.lasers_x.remove(arma_horizontal)
        return True
    
    #Cria o mapa do jogo
    def mapa(self):
        basex = SCREEN_WIDTH // 2 - (len(MAP1[0]) * WALL_GAP) // 2
        basey = SCREEN_HEIGHT // 2 - (len(MAP1) * WALL_GAP) // 2
        for line_index, line in enumerate(MAP1):
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
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameover = gameover.Gameover()
        self.level2 = level2.Level2
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.lasers_x = pygame.sprite.Group()
        self.lasers_y = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.guns = pygame.sprite.Group()
        self.map = MAP1
        self.mapa()
        self.timer = Timer()
        self.defeat = False
        self.victory = False
        pygame.mixer.music.play(-1)


    def desenha(self):
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

# alguns trechos da parte responsavel por resetar o game foi feita pelo GPT        
    def start(self):
        while self.atualiza_estado():
            if self.timer.time():
                self.player1.move(self.walls, self.guns)
                self.player2.move(self.walls, self.guns)
                self.desenha()
            if self.defeat or self.timer.time() == False:
                self.gameover.start()
                self.reset()
            if self.victory:
                self.level2.start()