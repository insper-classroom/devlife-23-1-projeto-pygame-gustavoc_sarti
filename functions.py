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

#Funcao da vitoria     
def won(self):
    colide_diamond = pygame.sprite.groupcollide(self.players, self.diamond, False, False, pygame.sprite.collide_rect)
    if colide_diamond:
        self.victory = True

#Função responsavel por criar os botões do jogo
def cria_botoes(self, SCREEN_WIDTH, SCREEN_HEIGHT, botoes_desejados, mouse_x, mouse_y):
    y_start = (SCREEN_HEIGHT - (len(self.botoes) * (self.button_height + 20))) // 2
    botoes_criados = 0
    for i, label in enumerate(self.botoes):
        #Criação de menu dedicada para o tutorial, visto que o botão deve estar em uma posição exata
        if botoes_desejados == ['retornar']:
            botao = self.fonte.render(label, True, (255, 255, 255))
            text_width, text_height = botao.get_size()
            x_button = (SCREEN_WIDTH - self.button_width) // 2
            y_button = y_start + 690
            x_text = (SCREEN_WIDTH - text_width) // 2
            y_text = y_button + (self.button_height - text_height) // 2
            self.window.blit(self.button, (x_button, y_button))
            self.window.blit(botao, (x_text, y_text))
            self.lista_btn_criado[label] = {'cord_x': x_button, 'cord_y': y_button}
        elif label in botoes_desejados:
            #Cria a interface grafica dos botoes
            botoes_criados += 1
            botao = self.fonte.render(label, True, (255, 255, 255))
            text_width, text_height = botao.get_size()
            x_button = (SCREEN_WIDTH - self.button_width) // 2
            y_button = y_start + botoes_criados * (self.button_height + 50)
            x_text = (SCREEN_WIDTH - text_width) // 2
            y_text = y_button + (self.button_height - text_height) // 2
            self.window.blit(self.button, (x_button, y_button))
            self.window.blit(botao, (x_text, y_text))
            self.lista_btn_criado[label] = {'cord_x': x_button, 'cord_y': y_button}
        
def clique_tutorial(self):
        if (
            self.lista_btn_criado['tutorial']['cord_x'] <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= self.lista_btn_criado['tutorial']['cord_x'] + self.button_width and
            self.lista_btn_criado['tutorial']['cord_y'] <= self.mouse_pos[1] and
            self.mouse_pos[1] <= self.lista_btn_criado['tutorial']['cord_y'] + self.button_height
            ):
            self.atual = 6
        
#Função do botao da tela de vitoria
def clique_menu(self):
        if (
            self.lista_btn_criado['MENU!']['cord_x'] <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= self.lista_btn_criado['MENU!']['cord_x'] + self.button_width and
            self.lista_btn_criado['MENU!']['cord_y'] <= self.mouse_pos[1] and
            self.mouse_pos[1] <= self.lista_btn_criado['MENU!']['cord_y'] + self.button_height
            ):
            self.atual = 0

#Função de retornar dedicada para o game over
def restart(self):
        if (
            self.lista_btn_criado['restart']['cord_x'] <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= self.lista_btn_criado['restart']['cord_x'] + self.button_width and
            self.lista_btn_criado['restart']['cord_y'] <= self.mouse_pos[1] and
            self.mouse_pos[1] <= self.lista_btn_criado['restart']['cord_y'] + self.button_height
            ):
            self.reset()
            pygame.mixer.music.play(-1)
            self.atual = 1

#Função de retornar dedicada para o tutorial
def clique_retornar(self):
        if (
            self.lista_btn_criado['retornar']['cord_x'] <= self.mouse_pos[0] and 
            self.mouse_pos[0] <= self.lista_btn_criado['retornar']['cord_x'] + self.button_width and
            self.lista_btn_criado['retornar']['cord_y'] <= self.mouse_pos[1] and
            self.mouse_pos[1] <= self.lista_btn_criado['retornar']['cord_y'] + self.button_height
            ):
            self.atual = 0

#Função responsavel por todas as interações de tela e botões do menu
def botoes_menu(self):
    if (
        self.lista_btn_criado['jogar']['cord_x'] <= self.mouse_pos[0] and 
        self.mouse_pos[0] <= self.lista_btn_criado['jogar']['cord_x'] + self.button_width and
        self.lista_btn_criado['jogar']['cord_y'] <= self.mouse_pos[1] and
        self.mouse_pos[1] <= self.lista_btn_criado['jogar']['cord_y'] + self.button_height
        ):
        self.reset()
        pygame.mixer.music.play(-1)
        self.atual = 1

    elif (
        self.lista_btn_criado['tutorial']['cord_x'] <= self.mouse_pos[0] and 
        self.mouse_pos[0] <= self.lista_btn_criado['tutorial']['cord_x'] + self.button_width and
        self.lista_btn_criado['tutorial']['cord_y'] <= self.mouse_pos[1] and
        self.mouse_pos[1] <= self.lista_btn_criado['tutorial']['cord_y'] + self.button_height
        ):
        self.atual = 6
        
    elif (
        self.lista_btn_criado['sair']['cord_x'] <= self.mouse_pos[0] and 
        self.mouse_pos[0] <= self.lista_btn_criado['sair']['cord_x'] + self.button_width and
        self.lista_btn_criado['sair']['cord_y'] <= self.mouse_pos[1] and
        self.mouse_pos[1] <= self.lista_btn_criado['sair']['cord_y'] + self.button_height
        ):
        self.quit = True
    
def botoes_game_over(self):
    if (
        self.lista_btn_criado['restart']['cord_x'] <= self.mouse_pos[0] and 
        self.mouse_pos[0] <= self.lista_btn_criado['restart']['cord_x'] + self.button_width and
        self.lista_btn_criado['restart']['cord_y'] <= self.mouse_pos[1] and
        self.mouse_pos[1] <= self.lista_btn_criado['restart']['cord_y'] + self.button_height
        ):
        self.atual = 0
        self.reset()
        pygame.mixer.music.play(-1)
    elif (
        self.lista_btn_criado['sair']['cord_x'] <= self.mouse_pos[0] and 
        self.mouse_pos[0] <= self.lista_btn_criado['sair']['cord_x'] + self.button_width and
        self.lista_btn_criado['sair']['cord_y'] <= self.mouse_pos[1] and
        self.mouse_pos[1] <= self.lista_btn_criado['sair']['cord_y'] + self.button_height
        ):
        self.quit = True
