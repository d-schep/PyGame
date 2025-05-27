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
from sons import *  # Sistema de sons do jogo

# Inicializa o sistema de sons
carregar_sons()

# Começa o jogo
state = INICIO  # Começa na tela inicial
clock = pygame.time.Clock()  # Isso aqui controla a velocidade do jogo

# Variáveis para controlar os sons
som_zumbi_tocando = False
som_suspense_tocando = False

# Loop principal do jogo - roda enquanto o jogo estiver aberto
while state != QUIT:
    # Mantém o jogo rodando na velocidade certa
    clock.tick(FPS)

    # Aqui é onde controlamos o que está acontecendo no jogo
    if state == INICIO:
        # Mostra a tela inicial
        tocar_musica(SOM_MENU)  # Toca música suave na tela inicial
        state = tela_inicial(window)
        if state == JOGANDO:  # Se o jogador clicou em começar
            parar_musica()  # Para a música do menu
            state = tela_historia(window)  # Mostra a história
            if state == JOGANDO:  # Se o jogador leu a história
                iniciar_timer()  # Começa a contar o tempo
                # Inicia o som de zumbi na sala 1
                tocar_som(SOM_ZUMBI, -1)  # -1 significa loop infinito
                som_zumbi_tocando = True
    
    elif state == JOGANDO:
        # Jogador está na primeira sala
        if not som_zumbi_tocando:
            tocar_som(SOM_ZUMBI, -1)
            som_zumbi_tocando = True
        state = sala_1(window)
        if state != JOGANDO:  # Se saiu da sala 1
            parar_som(SOM_ZUMBI)
            som_zumbi_tocando = False
    
    elif state == PROXIMA_SALA:
        # Jogador está na segunda sala
        if not som_suspense_tocando:
            tocar_som(SOM_SUSPENSE, -1)
            som_suspense_tocando = True
        state = sala_2(window)
        if state != PROXIMA_SALA:  # Se saiu da sala 2
            parar_som(SOM_SUSPENSE)
            som_suspense_tocando = False
    
    elif state == MORTO:
        # Jogador morreu, mostra a tela de morte
        parar_todos_sons()  # Para todos os sons antes de tocar o som de morte
        tocar_som(SOM_MORTE)
        state = tela_morte(window)
        if state == JOGANDO:  # Se o jogador clicou em reiniciar
            parar_todos_sons()  # Para o som de morte
            iniciar_timer()  # Reinicia o timer
            tocar_som(SOM_ZUMBI, -1)  # Reinicia o som de zumbi
            som_zumbi_tocando = True
    
    elif state == VENCEDOR:
        # Jogador ganhou, mostra a tela de vitória
        parar_todos_sons()  # Para todos os sons antes de tocar o som de vitória
        tocar_som(SOM_VITORIA)
        state = sala_vencedor(window, tempo_restante)
    
    else:
        # Fecha o jogo
        parar_todos_sons()  # Para todos os sons
        parar_musica()  # Para a música
        state = QUIT

# Quando sair do jogo, limpa tudo
pygame.quit()

