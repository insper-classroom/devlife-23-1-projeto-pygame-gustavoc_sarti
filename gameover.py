from config import *
import pygame


class Gameover:
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Genius Heist - Game Over')

        self.reset = False
        self.button = pygame.image.load('assets/images/menu/button_unselected.jpg')
        self.button = pygame.transform.scale(self.button, (240, 80))
        self.botoes = ['jogar novamente', 'sair']
        self.fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(self.fonte_padrao, 45)
        self.titulo = self.fonte.render('Game Over', True, (255, 255, 255))

    def desenha_gameover(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.titulo, ((SCREEN_WIDTH - self.titulo.get_width()) // 2, 100))

        button_width, button_height = self.button.get_size()
        for i, label in enumerate(self.botoes):
            text = self.fonte.render(label, True, (255, 255, 255))
            text_width, text_height = text.get_size()

            x_button = (SCREEN_WIDTH - button_width) // 2
            y_button = 300 + i * (button_height + 50)

            x_text = (SCREEN_WIDTH - text_width) // 2
            y_text = y_button + (button_height - text_height) // 2

            self.window.blit(self.button, (x_button, y_button))
            self.window.blit(text, (x_text, y_text))

        pygame.display.update()

    def clique_jogar_novamente(self):
        return (
            390 <= self.mouse_pos[0] <= 390 + 240 and
            300 <= self.mouse_pos[1] <= 300 + 80
        )

    def clique_sair(self):
        return (
            390 <= self.mouse_pos[0] <= 390 + 240 and
            450 <= self.mouse_pos[1] <= 450 + 80
        )

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
