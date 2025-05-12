import pygame
from Classe_Jogador import *
from cfg import *
from groups import * 
from assets import * 
import random
import time 
from Classe_Botoes_inicio import * 


def iniciar_jogo():
    global estado
    estado = "jogo"

def tela_inicial(screen):
    clock = pygame.time.Clock()
    assets = load_assets()
    background = assets[TELA_INICIAL]
    background_rect = background.get_rect()
    botao_inicio = Botao(CENTROx,CENTROy,LARG_BOT,ALT_BOT,'INICIAR', ACINZENTADO, BRANCO_ALPHA,assets, iniciar_jogo)
    rodando = True 
    state = INICIO
    while rodando:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                rodando = False

            if event.type == pygame.KEYUP:
                state = JOGANDO
                rodando = False
            if state == INICIO:
                botao_inicio.checar_click(event)
        

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(PRETO)
        screen.blit(background, background_rect)
        botao_inicio.desenhar(screen)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.update()


    return state
