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
botao_inicio = Botao_inicio(CENTROx,CENTROy,400,100,'INICIAR', CINZA, BRANCO, iniciar_jogo)
def tela_inicial(screen):
    clock = pygame.time.Clock()
    background = pygame.image.load(path.join(IMG_DIR,'bckg.png')).convert()
    background = pygame.transform.scale(background, (LARGURA, ALTURA))
    background_rect = background.get_rect()
    rodando = True 



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
                botao_inicio.desenhar(screen)
                botao_inicio.checar_click(event)


        # A cada loop, redesenha o fundo e os sprites
        screen.fill(PRETO)
        screen.blit(background, background_rect)
        # == Botoes inicio == 

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    return state
