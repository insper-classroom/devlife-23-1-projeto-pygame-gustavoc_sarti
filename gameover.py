from config import *
import pygame

class Gameover:
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Genius Heist - Game Over')

        self.button = pygame.image.load('assets/images/menu/button_unselected.jpg')
        self.button = pygame.transform.scale(self.button, (240, 80))

        self.botoes = ['jogar novamente','sair']
        self.fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(self.fonte_padrao, 45)
        self.titulo = self.fonte.render('Game Over', True, (255,255,255))

    def desenha_gameover(self):
        self.window.fill((0,0,0))
        self.window.blit(self.titulo,(400,100))
        for botoes in range(len(self.botoes)):
            botao = self.fonte.render(f'{self.botoes[botoes]}', True, (255,255,255))
            self.window.blit(self.button,(390,300+(150*botoes)))
            self.window.blit(botao,(430,320+(150*botoes)))
        pygame.display.update()
    
    def clique_jogar_novamente(self):
        if (
            390 <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= 390 + 240 and
            300 <= self.mouse_pos[1] and
            self.mouse_pos[1] <= 300 + 80
            ):
                return True
        else:
                return False    
    def clique_sair(self):
        if (
            390 <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= 390 + 240 and
            450 <= self.mouse_pos[1] and
            self.mouse_pos[1] <= 450 + 80
            ):
                return True
        else:
                return False
        
    def atualiza_estado(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.desenha_gameover()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.clique_jogar_novamente():
                    self.game.start()
                if self.clique_sair():
                    pygame.quit()
                    exit()
        return True

    def start(self):
         while self.atualiza_estado():
              self.desenha_gameover()