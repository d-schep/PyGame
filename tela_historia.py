import pygame
from cfg import *
from assets import *
from Classe_Botoes_inicio import *
from Classe_Textos import *

def tela_historia(screen):
    clock = pygame.time.Clock()
    assets = load_assets()
    state = INICIO
    
    # Carrega o background
    background = assets[TELA_INICIAL]
    background_rect = background.get_rect()
    
    # Cria os textos da história
    fonte = assets[FONTE_BOTAO]
    
    # Texto da história dividido em linhas
    historia = [
        "INSPER - P3 - 2025",
        "",
        "Um erro fatal foi cometido...",
        "",
        "Classes nas Provas Finais de DesSoft!",
        "",
        "Seus alunos, em fúria,",
        "viraram zumbis programadores.",
        "",
        "Você está preso no P3,",
        "cercado por zumbis de direito.",
        "",
        "15 minutos para desvendar",
        "os mistérios e escapar.",
        "",
        "BOA SORTE, PROFESSOR...",
        "",
        "Pressione ENTER para começar"
    ]
    
    # Renderiza cada linha do texto
    textos = []
    y = ALTURA/10  # Começa muito mais acima na tela
    
    for linha in historia:
        texto = fonte.render(linha, True, BRANCO)
        texto_rect = texto.get_rect(centerx=LARGURA/2, top=y)
        textos.append((texto, texto_rect))
        y += 35  # Mantém o espaçamento entre linhas
    
    # Efeito de digitação
    texto_atual = ""
    indice = 0
    ultima_atualizacao = 0
    delay = 50  # Milissegundos entre cada caractere
    
    while state == INICIO:
        clock.tick(FPS)
        
        # Atualiza o texto com efeito de digitação
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - ultima_atualizacao > delay and indice < len(historia):
            texto_atual = historia[indice]
            indice += 1
            ultima_atualizacao = tempo_atual
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and indice >= len(historia):
                    state = JOGANDO
        
        # Desenha tudo
        screen.fill(PRETO)
        
        # Desenha o background com transparência
        background.set_alpha(100)  # Valor entre 0 (transparente) e 255 (opaco)
        screen.blit(background, background_rect)
        
        # Desenha o texto com efeito de digitação
        for i, (texto, rect) in enumerate(textos):
            if i < indice:
                screen.blit(texto, rect)
        
        pygame.display.flip()
    
    return state 