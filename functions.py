import pygame
#Arquivo que reune funções utilizadas em todos os niveis, para poupar código repetido

#Codigo da quebra do laser
def laser_break(self):
    #Codigo para a remoção dos LASER disparados, feito com auxilio do chatGPT para criar a base e pensar a lõgica.
    #Basicamente ao remover a arma que dispara o laser, tambem pega suas cordenadas(na tela Pygame), as divide pelo
    #tamanho de um 'tile' do mapa, assim descobrindo a posição X,Y do arma(na lista do mapa). Em seguida remove todos
    #os lasers desta fileira ou coluna, configurado manualmente dependendo se é um laser X ou Y.
    lasers_colididos = pygame.sprite.groupcollide(self.players, self.guns, False, True, pygame.sprite.collide_rect)
    for player_sprite, laser_list in lasers_colididos.items():
        for gun_sprite in laser_list:
            #Pega tanto os index X e Y de colisao
            col_index = gun_sprite.rect.x // 40  #40 por ser o tamanho de um tile na tela
            row_index = gun_sprite.rect.y // 40  #40 por ser o tamanho de um tile na tela
            #Remove todos os laser de armas destruidas
            for arma_vertical in self.lasers_y:
                if arma_vertical.rect.x // 40 == col_index:
                    self.lasers_y.remove(arma_vertical)
            for arma_horizontal in self.lasers_x:
                if arma_horizontal.rect.y // 40 == row_index:
                    self.lasers_x.remove(arma_horizontal)

#Codigo do player morrendo
def player_hit(self):
    lasered_x = pygame.sprite.groupcollide(self.players, self.lasers_x, False, False, pygame.sprite.collide_rect)
    lasered_y = pygame.sprite.groupcollide(self.players, self.lasers_y, False, False, pygame.sprite.collide_rect)
    if lasered_x or lasered_y:
        self.defeat = True
    
def won(self):
    colide_diamond = pygame.sprite.groupcollide(self.players, self.diamond, False, False, pygame.sprite.collide_rect)
    if colide_diamond:
        self.victory = True