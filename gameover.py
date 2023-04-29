from config import *
import pygame


class Gameover:
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Genius Heist - Game Over')

        self.reset = False
        self.button = pygame.image.load('assets/images/menu/button_unselected.jpg')
        self.button = pygame.transform.scale(self.button, (240, 80))
        self.botoes = ['restart', 'sair']
        self.fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(self.fonte_padrao, 45)
        self.titulo = self.fonte.render('Game Over', True, (255, 255, 255))


    def desenha_gameover(self, score):
        self.window.fill((0, 0, 0))
        self.window.blit(self.titulo, ((SCREEN_WIDTH - self.titulo.get_width()) // 2, 100))
        self.button_width, self.button_height = self.button.get_size()
        for i, label in enumerate(self.botoes):
            text_surface = self.fonte.render(label, True, (255, 255, 255))
            text_width, text_height = text_surface.get_size()
            self.x_button = (SCREEN_WIDTH - self.button_width) // 2
            self.y_button = 300 + (i * (self.button_height + 50))
            y_text = self.y_button + (self.button_height - text_height) // 2
            self.window.blit(self.button, (self.x_button, self.y_button))
            self.window.blit(text_surface, ((SCREEN_WIDTH - text_width) // 2, y_text))
        self.resultado = self.fonte.render(f'Voce conseguiu {score} estrelas', True, (255,255,255))
        self.window.blit(self.resultado)
        pygame.display.update()

    def clique_jogar_novamente(self):
        self.x_button = (SCREEN_WIDTH - self.button_width) // 2
        self.y_button = (SCREEN_HEIGHT - (len(self.botoes) * (self.button_height + 50))) // 2
        if (
            self.x_button <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= self.x_button + self.button_width and
            self.y_button <= self.mouse_pos[1] and
            self.mouse_pos[1] <= self.y_button + self.button_height
            ):
                return True
        else:
                return False

    def clique_sair(self):
        self.x_button = (SCREEN_WIDTH - self.button_width) // 2
        self.y_button = (SCREEN_HEIGHT - (len(self.botoes) * (self.button_height + 50))) // 2 + self.button_height + 50
        if (
            self.x_button <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= self.x_button + self.button_width and
            self.y_button <= self.mouse_pos[1] and
            self.mouse_pos[1] <= self.y_button + self.button_height
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
                    self.reset = True
                if self.clique_sair():
                    pygame.quit()
                    exit()
        return True

    def start(self):
        while self.atualiza_estado():
            self.desenha_gameover()
