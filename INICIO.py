import pygame
from Classe_Jogador import *
from cfg import *
from groups import * 
from assets import * 
import random
import time 
from Classe_Botoes_inicio import * 
from Classe_Textos import *

def iniciar_jogo():
    global estado
    estado = "jogo"

def tela_inicial(screen):
    clock = pygame.time.Clock()
    assets = load_assets()
    preto = pygame.Surface((LARGURA,ALTURA), pygame.SRCALPHA)
    preto_rect = preto.get_rect()
    background = assets[TELA_INICIAL]
    titulo = assets[IMG_TITULO]
    background_rect = background.get_rect()
    botao_inicio = Botao(CENTROx-(LARG_BOT/2),(CENTROy+100-ALT_BOT),LARG_BOT,ALT_BOT,'INICIAR', ACINZENTADO, BRANCO_ALPHA,assets, iniciar_jogo)
    rodando = True 
    state = INICIO
    botao_quit = Botao(CENTROx-(LARG_BOT/2),(CENTROy+120),LARG_BOT,ALT_BOT,'QUIT', ACINZENTADO, BRANCO_ALPHA,assets, iniciar_jogo)


    while rodando:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            print(event)
            if event.type == pygame.QUIT:
                state = QUIT
                rodando = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state = QUIT
                rodando = False
            if state == INICIO:
                botao_inicio.checar_click(event)
        

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(PRETO)
        screen.blit(background, background_rect)
        pygame.draw.rect(preto,(0,0,0,160), preto_rect)
        screen.blit(preto,(0,0))
        screen.blit(titulo,((CENTROx-400,30)))
        botao_inicio.desenhar(screen)
        botao_quit.desenhar(screen)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.update()


    return state
