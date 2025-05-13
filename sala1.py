import pygame
from Classe_Jogador import *
from cfg import *
from groups import * 
from assets import * 
import random
import time 
from Classe_Botoes_inicio import * 
from Classe_Textos import *


def sala_1(screen):
    clock = pygame.time.Clock()
    assets = load_assets()
    grupos = load_grupos()
    background = assets[TELA_DE_FUNDO_ESCAPE_1]
    background_rect = background.get_rect()
    state = JOGANDO
    #gab_topa_eu = Jogador()
    while state == JOGANDO:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT

        screen.fill(PRETO)
        screen.blit(background,background_rect)


        pygame.display.update()

