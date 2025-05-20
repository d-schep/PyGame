import pygame
import time
from cfg import *

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