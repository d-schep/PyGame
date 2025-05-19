import pygame
from Classe_Jogador import *
from cfg import *
from assets import *
import random
import time
from Classe_Botoes_inicio import *
from Classe_Textos import *
from Classe_Interact import *

def sala_2(screen):
    clock = pygame.time.Clock()
    assets = load_assets()
    state = JOGANDO  # Definindo o estado inicial

    # Carregando a nova imagem de fundo (sala de armas)
    background = assets[TELA_DE_FUNDO_ESCAPE_2]
    background_rect = background.get_rect()
    
    # Adicionando Mesa_Arma
    Mesa_Arma = assets[MESA_ARMA]
    Mesa_Arma_rect = Mesa_Arma.get_rect()
    # Centralizando a mesa na sala
    Mesa_Arma_rect.centerx = LARGURA // 2
    Mesa_Arma_rect.centery = ALTURA // 2
    # Criar um retângulo de colisão menor que a mesa
    Mesa_colisao = pygame.Rect(Mesa_Arma_rect.left + 20, Mesa_Arma_rect.top + 20, 
                              int(LARGURA_MESA * 1.5) - 40, int(ALTURA_MESA * 1.5) - 140)

    # Adicionando Computador
    Computador = assets[COMPUTADOR]
    Computador_rect = Computador.get_rect()
    # Posicionando o computador mais para a esquerda no fundo da sala
    Computador_rect.left = 100
    Computador_rect.top = 40
    # Área de colisão para o computador
    Computador_colisao = pygame.Rect(Computador_rect.left + 25, Computador_rect.top + 25,
                                    200, 200)

    # Criando objetos interativos para cada arma
    texto_arma1 = """
    Glock 17
    Pistola
    9mm
    SN: --------
    """

    texto_arma2 = """
    AK-47
    Fuzil
    -----mm
    SN: RN7B43
    """

    texto_arma3 = """
    --------
    Submetralhadora
    9mm
    SN: UM1009J
    """

    texto_arma4 = """
    Mossberg 500
    ----------
    12 GA
    SN: SM416K0
    """

    # Textos para as pistas
    texto_tabela_substituicao = """
    TABELA DE SUBSTITUIÇÃO

    A = ⭐  H = △    O = ⚫    V = ●
    B = ▲  I = □    P = ⚪    W = ◆
    C = ■  J = ○    Q = ⚡    X = ○
    D = ●  K = ⚫    R = ⚠    Y = ☆
    E = ◆  L = ⚪    S = ⭐    Z = △
    F = ○  M = ⚡    T = ▲    1 = □
    G = ☆  N = ⚠    U = ■    2 = ○
    """

    texto_equacao = """
    (2 × π) + 1.34
    """

    texto_morse = """
    ..- --.. .. / -- .. -. ..
    """

    texto_quebra_cabeca = """
    Imagem QR Code
    """

    texto_computador = """
    Terminal de Segurança
    Status: ONLINE
    Nível: ADMINISTRADOR
    """

    # Posicionando os objetos interativos para cada arma na mesa
    arma1 = ObjetoInterativo(Mesa_Arma_rect.left + 50, 
                            Mesa_Arma_rect.top - 20,
                            60, 60, texto_arma1, tipo='arma', assets=assets, show_indicator=True)

    arma2 = ObjetoInterativo(Mesa_Arma_rect.right - 110,
                            Mesa_Arma_rect.top - 20,
                            60, 60, texto_arma2, tipo='arma', assets=assets, show_indicator=True)

    arma3 = ObjetoInterativo(Mesa_Arma_rect.left + 50,
                            Mesa_Arma_rect.bottom - 110,
                            60, 60, texto_arma3, tipo='arma', assets=assets, show_indicator=True)

    arma4 = ObjetoInterativo(Mesa_Arma_rect.right - 110,
                            Mesa_Arma_rect.bottom - 110,
                            60, 60, texto_arma4, tipo='arma', assets=assets, show_indicator=True)

    # Criando objetos interativos para as pistas
    # Tabela de substituição (na lateral esquerda)
    tabela_substituicao = ObjetoInterativo(100, ALTURA//2, 40, 40, texto_tabela_substituicao, 
                                         tipo='documento', assets=assets, show_indicator=True)

    # Equação matemática (no canto superior direito)
    equacao = ObjetoInterativo(LARGURA - 200, 350, 40, 40, texto_equacao, 
                              tipo='documento', assets=assets, show_indicator=True)

    # Código morse (no canto inferior esquerdo)
    morse = ObjetoInterativo(100, ALTURA - 200, 40, 40, texto_morse, 
                            tipo='documento', assets=assets, show_indicator=True)

    # Quebra-cabeça (no canto inferior direito)
    quebra_cabeca = ObjetoInterativo(LARGURA - 200, ALTURA - 200, 40, 40, texto_quebra_cabeca, 
                                    tipo='documento', assets=assets, show_indicator=True)

    # Criando objeto interativo para o computador
    computador_interativo = ObjetoInterativo(Computador_rect.left + 95, 
                                           Computador_rect.centery - 30,
                                           20, 20, texto_computador, 
                                           tipo='computador', assets=assets, 
                                           show_indicator=True)

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    all_interactables = pygame.sprite.Group()  # Grupo para objetos interativos
    
    # Criando o jogador
    gab_topa_eu = Jogador(assets)
    all_sprites.add(gab_topa_eu)

    # Adiciona objetos interativos ao grupo
    all_interactables.add(arma1)
    all_interactables.add(arma2)
    all_interactables.add(arma3)
    all_interactables.add(arma4)
    all_interactables.add(computador_interativo)
    all_interactables.add(tabela_substituicao)
    all_interactables.add(equacao)
    all_interactables.add(morse)
    all_interactables.add(quebra_cabeca)

    # Posiciona o jogador na entrada da nova sala
    gab_topa_eu.rect.x = LARGURA // 2
    gab_topa_eu.rect.y = ALTURA - 100

    keys_down = {}
    while state == JOGANDO:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                state = QUIT
            
            # Handle interações com as armas
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                for obj in all_interactables:
                    obj.tentar_interagir()

            # Controles do jogador
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_a:
                    gab_topa_eu.speedx -= 2
                if event.key == pygame.K_d:
                    gab_topa_eu.speedx += 2
                if event.key == pygame.K_w:
                    gab_topa_eu.speedy -= 2
                if event.key == pygame.K_s:
                    gab_topa_eu.speedy += 2

                if event.key == pygame.K_LEFT:
                    gab_topa_eu.speedx -= 2
                if event.key == pygame.K_RIGHT:
                    gab_topa_eu.speedx += 2
                if event.key == pygame.K_UP:
                    gab_topa_eu.speedy -= 2
                if event.key == pygame.K_DOWN:
                    gab_topa_eu.speedy += 2

            if event.type == pygame.KEYUP:
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_a:
                        gab_topa_eu.speedx += 2
                    if event.key == pygame.K_d:
                        gab_topa_eu.speedx -= 2
                    if event.key == pygame.K_w:
                        gab_topa_eu.speedy += 2
                    if event.key == pygame.K_s:
                        gab_topa_eu.speedy -= 2

                    if event.key == pygame.K_LEFT:
                        gab_topa_eu.speedx += 2
                    if event.key == pygame.K_RIGHT:
                        gab_topa_eu.speedx -= 2
                    if event.key == pygame.K_UP:
                        gab_topa_eu.speedy += 2
                    if event.key == pygame.K_DOWN:
                        gab_topa_eu.speedy -= 2
                    
                    keys_down.pop(event.key)

        # Atualiza posição de todos os sprites
        all_sprites.update()

        # Atualiza estado dos objetos interativos
        for obj in all_interactables:
            obj.update(gab_topa_eu)

        # Verifica colisões com a mesa e computador
        colide_mesa = pygame.Rect.colliderect(Mesa_colisao, gab_topa_eu.rect)
        colide_computador = pygame.Rect.colliderect(Computador_colisao, gab_topa_eu.rect)
        
        if colide_mesa or colide_computador:
            gab_topa_eu.rect.x -= gab_topa_eu.speedx
            gab_topa_eu.rect.y -= gab_topa_eu.speedy
            gab_topa_eu.speedy = gab_topa_eu.speedx = 0
            keys_down.clear()

        # Desenha
        screen.fill(PRETO)
        screen.blit(background, background_rect)
        screen.blit(Computador, Computador_rect)
        screen.blit(Mesa_Arma, Mesa_Arma_rect)

        # Desenha os objetos interativos
        for obj in all_interactables:
            obj.desenhar(screen)

        all_sprites.draw(screen)

        # Desenha as pistas dos objetos interativos
        for obj in all_interactables:
            obj.desenhar_pista(screen)

        pygame.display.update()

    return state 