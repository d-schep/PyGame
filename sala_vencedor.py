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
    fonte = assets[FONTE_BOTAO]
    
    # Calcula o tempo total usando o tempo decorrido
    tempo_total = int(get_tempo_decorrido())
    minutos = tempo_total // 60
    segundos = tempo_total % 60
    
    # Atualiza os high scores
    high_scores = update_high_scores(tempo_total)
    
    # Texto da vitória dividido em linhas
    historia = [
        "PARABÉNS, PROFESSOR!",
        "",
        "Você conseguiu escapar dos zumbis",
        "e prometeu nunca mais colocar",
        "classes nas provas finais.",
        "",
        f"Tempo total: {minutos:02d}:{segundos:02d}",
        "",
        "Melhores Tempos:",
        f"1º Lugar: {format_time(high_scores[0])}",
        f"2º Lugar: {format_time(high_scores[1])}",
        f"3º Lugar: {format_time(high_scores[2])}",
        "",
        "Pressione ENTER para sair"
    ]
    
    # Renderiza cada linha do texto
    textos = []
    y = ALTURA/4  # Começa mais acima na tela para acomodar os high scores
    
    for linha in historia:
        texto = fonte.render(linha, True, BRANCO)
        texto_rect = texto.get_rect(centerx=LARGURA/2, top=y)
        textos.append((texto, texto_rect))
        y += 35  # Espaçamento entre linhas
    
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
        background.set_alpha(100)  # Valor entre 0 (transparente) e 255 (opaco)
        screen.blit(background, background_rect)
        
        # Desenha todos os textos
        for texto, rect in textos:
            screen.blit(texto, rect)
        
        pygame.display.flip()
    
    return state 