import pygame
from cfg import *
pygame.init()
pygame.mixer.init()
pygame.font.init()
# ----- Gera tela principal
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Escape Z')
import random
from sala1 import * 
from sala2 import *  # Importando a nova sala
from INICIO import * 
from Classe_Botoes_inicio import * 
from tela_de_morte import *
from sala_vencedor import *  # Importando a sala do vencedor
from timer import *  # Importando todas as funções do timer

state = INICIO
clock = pygame.time.Clock()  # Adiciona um clock para controlar o FPS

while state != QUIT:
    # Controla o FPS
    clock.tick(FPS)

    if state == INICIO:
        state = tela_inicial(window)
        if state == JOGANDO:  # Se saiu da tela inicial para jogar
            iniciar_timer()  # Inicia o timer quando começa o jogo
    elif state == JOGANDO:
        state = sala_1(window)
    elif state == PROXIMA_SALA:
        state = sala_2(window)
    elif state == MORTO:
        state = tela_morte(window)
    elif state == VENCEDOR:  # Novo estado para a sala do vencedor
        state = sala_vencedor(window, tempo_restante)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

