from config import *
import level1
import pygame

class Menu:
    #Inicializa os elementos graficos do menu.
    def __init__(self,):
        #Inicialização basica
        pygame.init()
        self.level1 = level1.Level1()
        pygame.display.set_caption("Genius Heist")
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        #Start music
        pygame.mixer.music.load('assets/sounds/sounds_misc/ogg/background_music.ogg')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.08)

        #Configura os botões
        self.button = pygame.image.load('assets/images/menu/button_unselected.jpg')
        self.button = pygame.transform.scale(self.button, (240, 80))

        #Configura a imagem de fundo
        background = pygame.image.load('assets/images/menu/bank-pygame.png')
        self.background = pygame.transform.scale(background,(1420,969))
        
        #Configura texto dos botões
        self.botoes = ['jogar','tutorial','sair']
        self.fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(self.fonte_padrao, 45)
        self.fonte_titulo = pygame.font.Font(self.fonte_padrao, 100)
        self.titulo = self.fonte_titulo.render('GENIUS HEIST', True, (0,0,0))
        self.button_width, self.button_height = self.button.get_size()


    def desenha_menu(self): #usamos o Chat GPT para a centralizacao
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.titulo, (350, 100))

        button_width, button_height = self.button.get_size()
        y_start = (SCREEN_HEIGHT - (len(self.botoes) * (button_height + 20))) // 2

        for i, label in enumerate(self.botoes):
            botao = self.fonte.render(label, True, (255, 255, 255))
            text_width, text_height = botao.get_size()

            x_button = (SCREEN_WIDTH - button_width) // 2
            y_button = y_start + i * (button_height + 50)
            x_text = (SCREEN_WIDTH - text_width) // 2
            y_text = y_button + (button_height - text_height) // 2

            self.window.blit(self.button, (x_button, y_button))
            self.window.blit(botao, (x_text, y_text))
    
        pygame.display.update()

    #Cria as funções que registram clicks nos botões da tela.
    def clique_jogar(self):
        if (
            (SCREEN_WIDTH - 240) // 2 <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= (SCREEN_WIDTH - 240) // 2 + 240 and
            (SCREEN_HEIGHT - (len(self.botoes) * (self.button_height + 20))) // 2 <= self.mouse_pos[1] and
            self.mouse_pos[1] <= (SCREEN_HEIGHT - (len(self.botoes) * (self.button_height + 20))) // 2 + self.button_height
            ):
                return True
        else:
            return False
    
    def clique_tutorial(self):
        if (
            (SCREEN_WIDTH - 240) // 2 <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= (SCREEN_WIDTH - 240) // 2 + 240 and
            (SCREEN_HEIGHT - (len(self.botoes) * (80 + 50))) // 2 + (80 + 50) <= self.mouse_pos[1] and
            self.mouse_pos[1] <= (SCREEN_HEIGHT - (len(self.botoes) * (80 + 50))) // 2 + 2 * (80 + 50)
            ):
                return True
        else:
            return False

    def clique_sair(self):
        if (
            (SCREEN_WIDTH - 240) // 2 <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= (SCREEN_WIDTH - 240) // 2 + 240 and
            (SCREEN_HEIGHT - (len(self.botoes) * (80 + 50))) // 2 + 2 * (80 + 50) <= self.mouse_pos[1] and
            self.mouse_pos[1] <= (SCREEN_HEIGHT - (len(self.botoes) * (80 + 50))) // 2 + 3 * (80 + 50)
            ):
                return True
        else:
            return False


    #Atualiza as informações do menu conforme o usuario interagir com a tela.
    def atualiza_estado_menu(self):
        self.mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.clique_jogar():
                    self.level1.start()
                if self.clique_tutorial():
                    return False
                if self.clique_sair():
                    pygame.quit()
        return True

    #Função principal que inicia o jogo todo a partir do menu.
    def start(self):
        while self.atualiza_estado_menu():
            self.desenha_menu()

