
import pygame
from cfg import *
pygame.init()
pygame.mixer.init()
pygame.font.init()
# ----- Gera tela principal
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Escape Z')
import random

from INICIO import * 
from Classe_Botoes_inicio import * 

state = INICIO
while state != QUIT:
    if state == INICIO:
        state = tela_inicial(window)
    # elif state == GAME:
    #     state = game_screen(window)
    # elif state == MORT:
    #     state = mort_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

