import pygame
from cfg import *
from assets import *
from Classe_Botoes_inicio import *
from Classe_Textos import *

def sala_vencedor(screen, tempo_restante):
    clock = pygame.time.Clock()
    assets = load_assets()
    
    # Carrega o background
    background = assets[TELA_DE_FUNDO_ESCAPE_1]  # Você pode criar um background específico para vitória depois
    background_rect = background.get_rect()
    
    # Cria os textos de vitória
    fonte_grande = pygame.font.Font(None, 74)
    fonte_media = pygame.font.Font(None, 48)
    fonte_pequena = pygame.font.Font(None, 36)
    
    # Calcula o tempo total (15 minutos - tempo restante)
    tempo_total = 15 * 60 - tempo_restante
    minutos = int(tempo_total) // 60
    segundos = int(tempo_total) % 60
    
    texto_vitoria = fonte_grande.render("MISSÃO CUMPRIDA!", True, (255, 215, 0))  # Cor dourada
    texto_subtitulo = fonte_media.render("Você salvou a humanidade!", True, (255, 255, 255))
    texto_descricao1 = fonte_pequena.render("A cura foi recuperada e os zumbis foram contidos.", True, (200, 200, 200))
    texto_descricao2 = fonte_pequena.render("O mundo está a salvo... por enquanto.", True, (200, 200, 200))
    texto_tempo = fonte_pequena.render(f"Tempo total: {minutos:02d}:{segundos:02d}", True, (255, 215, 0))  # Cor dourada
    
    # Posiciona os textos no centro da tela
    texto_vitoria_rect = texto_vitoria.get_rect(center=(LARGURA//2, ALTURA//2 - 120))
    texto_subtitulo_rect = texto_subtitulo.get_rect(center=(LARGURA//2, ALTURA//2 - 50))
    texto_descricao1_rect = texto_descricao1.get_rect(center=(LARGURA//2, ALTURA//2 + 20))
    texto_descricao2_rect = texto_descricao2.get_rect(center=(LARGURA//2, ALTURA//2 + 60))
    texto_tempo_rect = texto_tempo.get_rect(center=(LARGURA//2, ALTURA//2 + 100))
    
    # Cria o botão de sair
    def sair_jogo():
        nonlocal state
        state = QUIT
    
    botao_sair = Botao(LARGURA//2 - 100, ALTURA//2 + 140, 200, 50, "Sair", (255, 0, 0), (200, 0, 0), assets, sair_jogo)
    
    state = VENCEDOR
    
    while state == VENCEDOR:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            
            # Verifica clique no botão
            botao_sair.checar_click(event)
        
        # Atualiza o botão
        botao_sair.update(pygame.mouse.get_pos())
        
        # Desenha tudo
        screen.fill(PRETO)
        screen.blit(background, background_rect)
        
        # Desenha os textos
        screen.blit(texto_vitoria, texto_vitoria_rect)
        screen.blit(texto_subtitulo, texto_subtitulo_rect)
        screen.blit(texto_descricao1, texto_descricao1_rect)
        screen.blit(texto_descricao2, texto_descricao2_rect)
        screen.blit(texto_tempo, texto_tempo_rect)
        
        # Desenha o botão
        botao_sair.desenhar(screen)
        
        pygame.display.flip()
    
    return state 