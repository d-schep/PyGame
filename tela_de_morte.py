import pygame
from Classe_Jogador import *
from cfg import *

from assets import * 
import random
import time 
from Classe_Botoes_inicio import * 
from Classe_Textos import *
from sala1 import * 
import time

def tela_morte(screen):
    clock = pygame.time.Clock()
    assets = load_assets()
    state = MORTO
    keys_down = {} 
    fonte = assets[FONTE_BOTAO]
    txt = 'VoCÊ MoRREU'
    alph = 0
    indx = 0
    def sair_jogo():
        nonlocal state
        print('funcao foi chamada')
        state = QUIT
    def lerolero():
        nonlocal state
        state = JOGANDO
    rest = Botao(CENTROx-(LARG_BOT/2),(CENTROy+100-ALT_BOT),LARG_BOT,ALT_BOT,'REINICIAR', ACINZENTADO, BRANCO_ALPHA,assets, lerolero)
    qt = Botao(CENTROx-(LARG_BOT/2),(CENTROy+120),LARG_BOT,ALT_BOT,'QUIT', ACINZENTADO, BRANCO_ALPHA,assets, sair_jogo)
    qt.alpha = 0
    rest.alpha = 0 
    while state == MORTO:
        clock.tick(FPS)
        tela = pygame.Surface((LARGURA,ALTURA))
        tela.fill(PRETO)
        tela.set_alpha(alph)
        screen.blit(tela,(0,0))
        msg_no_mei = fonte.render(txt[:indx], True, VERMELHO)
        msg_rect = msg_no_mei.get_rect(center=(LARGURA/2, ALTURA/2 - 250))
        screen.blit(msg_no_mei,msg_rect)
        if alph < 255:
            time.sleep(0.05)
            alph +=5
        elif qt.alpha < 255: 
            qt.alpha += 5
            rest.alpha += 5
        if indx <len(txt):
            indx += 1 
        if qt.alpha > 0:
            qt.desenhar(screen)
            rest.desenhar(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                state = QUIT
            qt.checar_click(event)
            rest.checar_click(event)
        

        pygame.display.update()
    return state

