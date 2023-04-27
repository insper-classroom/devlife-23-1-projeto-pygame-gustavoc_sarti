from config import *
import game
import pygame
import gameover

class Menu:
    #Inicializa os elementos graficos do menu.
    def __init__(self,):
        #Inicialização basica
        pygame.init()
        self.game = game.Game()
        self.gameover = gameover.Gameover()
        pygame.display.set_caption("Menu")
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        #Configura os botões
        self.button = pygame.image.load('assets/images/menu/button_unselected.jpg')
        self.button = pygame.transform.scale(self.button, (240, 80))

        #Configura a imagem de fundo
        self.background = pygame.image.load('assets/images/menu/bank-pygame.jpeg')
        self.background = pygame.transform.scale(self.background,(1020,726))

        #Configura texto dos botões
        self.botoes = ['jogar','tutorial','sair']
        self.fonte_padrao = pygame.font.get_default_font()
        self.fonte = pygame.font.Font(self.fonte_padrao, 45)
        self.titulo = self.fonte.render('GENIUS HEIST', True, (255,255,0))

    def desenha_menu(self):
        self.window.blit(self.background,(0,0))
        self.window.blit(self.titulo,(350,100))
        for botoes in range(len(self.botoes)):
            botao = self.fonte.render(f'{self.botoes[botoes]}', True, (255,255,255))
            self.window.blit(self.button,(390,300+(150*botoes)))
            self.window.blit(botao,(430,320+(150*botoes)))
        pygame.display.update()

    #Cria as funções que registram clicks nos botões da tela.
    def clique_jogar(self):
        if (
            390 <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= 390 + 240 and
            300 <= self.mouse_pos[1] and
            self.mouse_pos[1] <= 300 + 80
            ):
                return True
        else:
                return False
        
    def clique_tutorial(self):
        if (
            390 <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= 390 + 240 and
            450 <= self.mouse_pos[1] and
            self.mouse_pos[1] <= 450 + 80
            ):
                return True
        else:
                return False

    def clique_sair(self):
        if (
            390 <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= 390 + 240 and
            600 <= self.mouse_pos[1] and
            self.mouse_pos[1] <= 600 + 80
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
                    self.game.start()
                    self.gameover.start()
                    

                    return False
                if self.clique_tutorial():
                    return False
                if self.clique_sair():
                    return False
        return True

    #Função principal que inicia o jogo todo a partir do menu.
    def start(self):
        while self.atualiza_estado_menu():
            self.desenha_menu()

