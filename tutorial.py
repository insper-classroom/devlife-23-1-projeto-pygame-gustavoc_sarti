from config import *
import pygame

class Tutorial:
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.button = pygame.image.load('assets/images/menu/button_unselected.jpg')
        self.button = pygame.transform.scale(self.button, (240, 80))
        self.botoes = ['voltar']
        self.fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(self.fonte_padrao, 45)
        self.titulo = self.fonte.render('Tutorial', True, (255, 255, 255))

    def desenha_tutorial(self):
        self.window.fill((0,0,0))
        self.window.blit(self.titulo, ((SCREEN_WIDTH - self.titulo.get_width()) // 2, 69))
        pygame.draw.rect(self.window, (255, 255, 255), (0, 0, 50, 50))
    