import pygame
class Inicializacao:
    def __init__(self):
        pygame.init()
        self.assets = {

        }   
        self.state = {

        } 

class Atualiza_estado:
    def __init__(self, estado):
        self.estado = estado

    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

class Desenha:
    def __init__(self, window, inicializacao):
        self.window = window
        self.inicializacao = inicializacao

    def frame(self):
        self.window.fill((0, 0, 0))                

        pygame.display.update()

class Game:
    def __init__(self):
        self.estado = Inicializacao()
        self.window = pygame.display.set_mode((1024, 720), vsync=True, flags=pygame.SCALED)
        self.atualiza_estado = Atualiza_estado(self.estado)
        self.desenha = Desenha(self.window, self.estado)
    def start(self):
        while self.atualiza_estado.atualiza():
            self.desenha.frame()

game = Game()
game.start()