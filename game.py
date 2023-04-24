import pygame
from sprites.player import *
#Class principal do jogo que opera as 3 funções principais do Pygame:
#Criar seu estado inicial, atualizar ele e desenhar na tela.
class Game:
    def __init__(self):
        pygame.init()
        bounds = (1024, 720)
        self.window = pygame.display.set_mode(bounds)
        pygame.display.set_caption('Genius Heist')
        self.player = Player(pygame.Rect(4, 4, bounds[0], bounds[1]))


        self.assets = {
            # 'player': pygame.transform.scale(player, (50, 50))
        }
        
        #Cria dicionario de state(infos diversas) a serem utilizados
        self.state = {

        } 

    #Método responsavel por atualizar o jogo
    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    #Método responsavel por mostrar o jogo atualizado
    def desenha(self, assets, state):
        self.window.fill((0, 0, 0))                
        self.player.draw(self.window, self.pos)
        pygame.display.update()
        
    #Método responsavel por rodar o jogo ate ele ser encerrado
    def start(self):
        while self.atualiza_estado():
            self.desenha(self.assets, self.state)
