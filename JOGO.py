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
import time

# Variáveis globais para o timer
tempo_inicial = None
tempo_restante = 15 * 60  # 15 minutos em segundos
timer_ativo = False
ultima_atualizacao = 0  # Para controlar a atualização do timer

def atualizar_timer():
    global tempo_restante, ultima_atualizacao
    tempo_atual = time.time()
    
    if timer_ativo and tempo_inicial is not None:
        # Atualiza a cada segundo
        if tempo_atual - ultima_atualizacao >= 1.0:
            tempo_decorrido = tempo_atual - tempo_inicial
            tempo_restante = max(0, 15 * 60 - tempo_decorrido)
            ultima_atualizacao = tempo_atual
        return tempo_restante
    return tempo_restante

def desenhar_timer(screen):
    if timer_ativo:
        minutos = int(tempo_restante) // 60
        segundos = int(tempo_restante) % 60
        
        # Desenha um fundo preto semi-transparente atrás do timer
        fundo = pygame.Surface((150, 40))
        fundo.fill((0, 0, 0))
        fundo.set_alpha(200)  # Aumentado para melhor visibilidade
        screen.blit(fundo, (LARGURA - 150, 20))
        
        # Desenha o texto do timer
        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(f"Tempo: {minutos:02d}:{segundos:02d}", True, (255, 0, 0))
        screen.blit(texto, (LARGURA - 150, 20))

def iniciar_timer():
    global tempo_inicial, timer_ativo, tempo_restante, ultima_atualizacao
    tempo_inicial = time.time()
    ultima_atualizacao = tempo_inicial
    tempo_restante = 15 * 60  # Reinicia o tempo para 15 minutos
    timer_ativo = True

def parar_timer():
    global timer_ativo
    timer_ativo = False

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

