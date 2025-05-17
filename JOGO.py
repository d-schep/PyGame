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


state = INICIO
while state != QUIT:
    if state == INICIO:
        state = tela_inicial(window)
    elif state == JOGANDO:
        state = sala_1(window)
    elif state == PROXIMA_SALA:  # Adicionando estado para a sala 2
        state = sala_2(window)
    elif state == MORTO:
         state = tela_morte(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

