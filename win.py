from config import *
import pygame

class Win:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.button = pygame.image.load('assets/images/menu/button_selected.jpg')
        self.button = pygame.transform.scale(self.button, (240, 80))
        self.botoes = ['sair']
        self.fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(self.fonte_padrao, 45)
        self.titulo = self.fonte.render('Você Escapou!', True, (0, 0, 0))
        #Configura a imagem de fundo
        background = pygame.image.load('assets/images/menu/win.png')
        self.background = pygame.transform.scale(background,(1420,969))

        self.win_sound = pygame.mixer.Sound('assets/sounds/sounds_misc/ogg/victory_music.ogg')
        self.win_sound.set_volume(0.1)
        self.menu = False


    def desenha_win(self):
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.titulo, ((SCREEN_WIDTH - self.titulo.get_width()) // 2, 100))
        self.button_width, self.button_height = self.button.get_size()
        for i, label in enumerate(self.botoes):
            text_surface = self.fonte.render(label, True, (255, 255, 255))
            text_width, text_height = text_surface.get_size()
            self.x_button = (SCREEN_WIDTH - self.button_width) // 2
            self.y_button = 300 + (self.button_height + 50)
            y_text = self.y_button + (self.button_height - text_height) // 2
            self.window.blit(self.button, (self.x_button, self.y_button))
            self.window.blit(text_surface, ((SCREEN_WIDTH - text_width) // 2, y_text))
        # self.resultado = self.fonte.render(f'Voce conseguiu {score} estrelas', True, (255,255,255))
        # self.window.blit(self.resultado)
        pygame.display.update()

    def clique_sair(self):
        if (
            self.x_button <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= self.x_button + self.button_width and
            self.y_button <= self.mouse_pos[1] and
            self.mouse_pos[1] <= self.y_button + self.button_height
            ):
                return True

    def atualiza_estado(self):
        self.mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.clique_sair():
                    self.menu = True
        return True

    def start(self):
        pygame.mixer.music.stop()
        self.win_sound.play()
        while self.atualiza_estado():
            self.desenha_win()
            if self.menu:
                break
