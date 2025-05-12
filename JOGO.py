from Classe_Botoes_inicio import * 
import pygame
import random
from cfg import *
from INICIO import * 


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Escape Z')

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

