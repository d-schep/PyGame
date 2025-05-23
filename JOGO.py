# Primeiro vamos importar tudo que precisamos
import pygame
from cfg import *  # Aqui estão todas as configurações do jogo (cores, tamanhos, etc)
pygame.init()  # Liga o pygame
pygame.mixer.init()  # Liga o som
pygame.font.init()  # Liga as fontes

# Cria a janela do jogo
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Escape Z')  # Coloca o nome do jogo na janela

# Importa todas as partes do jogo
import random
from sala1 import *  # A primeira sala onde o jogador começa
from sala2 import *  # A segunda sala com as armas
from INICIO import *  # A tela inicial com os botões
from Classe_Botoes_inicio import *  # Os botões bonitos que fizemos
from tela_de_morte import *  # A tela que aparece quando morre
from sala_vencedor import *  # A tela de vitória com os recordes
from timer import *  # O timer que conta o tempo
from tela_historia import *  # A tela que conta a história do jogo

# Começa o jogo
state = INICIO  # Começa na tela inicial
clock = pygame.time.Clock()  # Isso aqui controla a velocidade do jogo

# Loop principal do jogo - roda enquanto o jogo estiver aberto
while state != QUIT:
    # Mantém o jogo rodando na velocidade certa
    clock.tick(FPS)

    # Aqui é onde controlamos o que está acontecendo no jogo
    if state == INICIO:
        # Mostra a tela inicial
        state = tela_inicial(window)
        if state == JOGANDO:  # Se o jogador clicou em começar
            state = tela_historia(window)  # Mostra a história
            if state == JOGANDO:  # Se o jogador leu a história
                iniciar_timer()  # Começa a contar o tempo
    
    elif state == JOGANDO:
        # Jogador está na primeira sala
        state = sala_1(window)
    
    elif state == PROXIMA_SALA:
        # Jogador está na segunda sala
        state = sala_2(window)
    
    elif state == MORTO:
        # Jogador morreu, mostra a tela de morte
        state = tela_morte(window)
    
    elif state == VENCEDOR:
        # Jogador ganhou, mostra a tela de vitória
        state = sala_vencedor(window, tempo_restante)
    
    else:
        # Fecha o jogo
        state = QUIT

# Quando sair do jogo, limpa tudo
pygame.quit()

