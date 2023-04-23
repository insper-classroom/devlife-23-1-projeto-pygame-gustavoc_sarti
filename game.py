import pygame
from sprites.player import *
#Class principal do jogo que opera as 3 funções principais do Pygame:
#Criar seu estado inicial, atualizar ele e desenhar na tela.
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1024, 720), vsync=True, flags=pygame.SCALED)
        pygame.display.set_caption('')
        #Cria dicionario de assets para serem utilizados
        player = pygame.image.load('assets/images/square.png')
        self.assets = {
            'player': pygame.transform.scale(player, (50, 50))
        }
        
        #Cria dicionario de state(infos diversas) a serem utilizados
        self.state = {

        } 

    #Função da classe responsavel por atualizar o jogo
    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    #Função da classe responsavel por mostrar o jogo atualizado
    def desenha(self, assets, state):
        self.window.fill((0, 0, 0))                
        self.window.blit(assets['player'], (100, 100)) 
        pygame.display.update()
        
    #Função da classe responsavel por rodar o jogo ate ele ser encerrado
    def start(self):
        while self.atualiza_estado():
            self.desenha(self.assets, self.state)

game = Game()
game.start()