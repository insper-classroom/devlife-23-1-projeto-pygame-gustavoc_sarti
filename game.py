import pygame
from sprites.player import *
from config import *
from sprites.map_content import *
import gameover

class Timer:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.start = 3000
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

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Genius Heist')

        self.gameover = gameover.Gameover()
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.map = MAP
        self.mapa()
        self.timer = Timer()

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        return True
    
    def mapa(self):
        basex = SCREEN_WIDTH // 2 - (len(MAP[0]) * WALL_GAP) // 2
        basey = SCREEN_HEIGHT // 2 - (len(MAP) * WALL_GAP) // 2
        for line_index, line in enumerate(MAP):
            for column_index, column in enumerate(line):
                x = basex + column_index * WALL_GAP 
                y = basey + line_index  * WALL_GAP
                if column == 'X':
                    Wall((x, y), self.walls)
                if column == 'S':
                    SideWall((x, y), self.walls)
                if column == ' ':
                    Floor((x, y), self.sprites)
                if column == '1':
                    Floor((x, y), self.sprites)
                    self.player1 = Player1((x, y), self.players)
                if column == '2':
                    Floor((x, y), self.sprites)
                    self.player2 = Player2((x, y), self.players)

    def desenha(self):
        self.window.fill((30,30,65))
        self.walls.draw(self.window)
        self.sprites.draw(self.window)
        self.players.draw(self.window)
        #GPT + stackoverflow
        self.timer.clock.tick(100)
        time_text = self.timer.get_time_string()
        font = pygame.font.Font(None, 36)
        text = font.render(time_text, True, (255, 255, 255))
        self.window.blit(text, (10, 10))
        #-------------------
        pygame.display.update()  
        
    def start(self):
        while self.atualiza_estado():
            if self.gameover.reset:
                self.timer = Timer()
                self.timer.start = 3000
                self.players.empty()
                self.walls.empty()
                self.sprites.empty()
                self.mapa()
                self.gameover.reset = False
            if self.timer.time():
                self.player1.move(self.walls)
                self.player2.move(self.walls)
                self.desenha()
            else:
                self.gameover.desenha_gameover()
                self.gameover.atualiza_estado()
    
