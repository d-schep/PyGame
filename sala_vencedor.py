import pygame
from cfg import *
from assets import *
from Classe_Botoes_inicio import *
from Classe_Textos import *
from timer import get_tempo_decorrido
from high_scores import update_high_scores, format_time

def sala_vencedor(screen, tempo_restante):
    clock = pygame.time.Clock()
    assets = load_assets()
    state = INICIO
    
    # Carrega o background
    background = assets[TELA_INICIAL]
    background_rect = background.get_rect()
    
    # Cria os textos da vitória
    fonte_titulo = assets[FONTE_BOTAO]
    fonte_texto = pygame.font.Font(None, 36)  # Fonte menor para os textos
    
    # Calcula o tempo total usando o tempo decorrido
    tempo_total = int(get_tempo_decorrido())
    minutos = tempo_total // 60
    segundos = tempo_total % 60
    
    # Atualiza os high scores
    high_scores = update_high_scores(tempo_total)
    
    # Texto da vitória dividido em seções
    titulo = fonte_titulo.render("PARABÉNS, PROFESSOR!", True, BRANCO)
    titulo_rect = titulo.get_rect(centerx=LARGURA/2, top=ALTURA/6)
    
    historia = [
        "Você conseguiu escapar dos zumbis",
        "e prometeu nunca mais colocar",
        "classes nas provas finais."
    ]
    
    tempo_atual = fonte_titulo.render(f"Tempo total: {minutos:02d}:{segundos:02d}", True, BRANCO)
    tempo_rect = tempo_atual.get_rect(centerx=LARGURA/2, top=ALTURA/2)
    
    # Renderiza a história
    textos_historia = []
    y = ALTURA/3
    for linha in historia:
        texto = fonte_texto.render(linha, True, BRANCO)
        texto_rect = texto.get_rect(centerx=LARGURA/2, top=y)
        textos_historia.append((texto, texto_rect))
        y += 35
    
    # Renderiza os recordes
    recordes_titulo = fonte_titulo.render("Melhores Tempos:", True, BRANCO)
    recordes_rect = recordes_titulo.get_rect(centerx=LARGURA/2, top=ALTURA/2 + 80)
    
    recordes = []
    y = ALTURA/2 + 130
    for i, score in enumerate(high_scores, 1):
        texto = fonte_texto.render(f"{i}º Lugar: {format_time(score)}", True, BRANCO)
        texto_rect = texto.get_rect(centerx=LARGURA/2, top=y)
        recordes.append((texto, texto_rect))
        y += 35
    
    # Instrução para sair - Agora mais acima na tela
    sair = fonte_texto.render("Pressione ENTER para sair", True, BRANCO)
    sair_rect = sair.get_rect(centerx=LARGURA/2, bottom=ALTURA - 100)  # Subido de 50 para 100 pixels do fundo
    
    while state == INICIO:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = QUIT
        
        # Desenha tudo
        screen.fill(PRETO)
        
        # Desenha o background com transparência
        background.set_alpha(100)
        screen.blit(background, background_rect)
        
        # Desenha o título
        screen.blit(titulo, titulo_rect)
        
        # Desenha a história
        for texto, rect in textos_historia:
            screen.blit(texto, rect)
        
        # Desenha o tempo atual
        screen.blit(tempo_atual, tempo_rect)
        
        # Desenha os recordes
        screen.blit(recordes_titulo, recordes_rect)
        for texto, rect in recordes:
            screen.blit(texto, rect)
        
        # Desenha a instrução para sair
        screen.blit(sair, sair_rect)
        
        pygame.display.flip()
    
    return state 