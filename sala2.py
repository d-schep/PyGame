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

    # Carregando a nova imagem de fundo (sala de armas)
    background = assets[TELA_DE_FUNDO_ESCAPE_2]
    background_rect = background.get_rect()
    
    # Adicionando Mesa_Arma
    Mesa_Arma = assets[MESA_ARMA]
    Mesa_Arma_rect = Mesa_Arma.get_rect()
    # Centralizando a mesa na sala
    Mesa_Arma_rect.centerx = LARGURA // 2
    Mesa_Arma_rect.centery = ALTURA // 2

    # Adicionando Computador
    Computador = assets[COMPUTADOR]
    Computador_rect = Computador.get_rect()
    # Posicionando o computador mais para a esquerda no fundo da sala
    Computador_rect.left = 100  # Mantendo a mesma distância da esquerda
    Computador_rect.top = 40  # Ajustando para o novo tamanho
    # Área de colisão para o computador
    Computador_colisao = pygame.Rect(Computador_rect.left + 25, Computador_rect.top + 25,
                                    200, 200)  # Área de colisão proporcional ao novo tamanho

    # Criando colisões para as bordas da mesa
    borda_superior = pygame.Rect(Mesa_Arma_rect.left, Mesa_Arma_rect.top,
                               int(LARGURA_MESA * 1.5), 40)
    borda_inferior = pygame.Rect(Mesa_Arma_rect.left, Mesa_Arma_rect.bottom - 40,
                               int(LARGURA_MESA * 1.5), 40)
    borda_esquerda = pygame.Rect(Mesa_Arma_rect.left, Mesa_Arma_rect.top,
                               40, int(ALTURA_MESA * 1.5))
    borda_direita = pygame.Rect(Mesa_Arma_rect.right - 40, Mesa_Arma_rect.top,
                               40, int(ALTURA_MESA * 1.5))

    # Criando objetos interativos para cada arma
    texto_arma1 = """
    ⚔️ Pistola Tática M1911
    
    Calibre: .45 ACP
    Capacidade: 7+1 rounds
    Alcance efetivo: 50m
    
    Status: Munição esgotada
    Observação: Mecanismo travado
    """

    texto_arma2 = """
    🗡️ Revólver Magnum
    
    Calibre: .357 Magnum
    Capacidade: 6 rounds
    Alcance efetivo: 45m
    
    Status: 2 munições restantes
    Observação: Tambor danificado
    """

    texto_arma3 = """
    🔫 Shotgun Tática
    
    Calibre: 12 gauge
    Capacidade: 5+1 rounds
    Alcance efetivo: 40m
    
    Status: Sem munição
    Observação: Sistema de recarga comprometido
    """

    texto_computador = """
    💻 Terminal de Segurança
    
    Status: ONLINE
    Nível de Acesso: ADMINISTRADOR
    
    Logs recentes:
    > Falha no sistema de travas [ERRO-2891]
    > Tentativa de acesso não autorizado
    > Protocolo de emergência ativado
    > Sistema de segurança comprometido
    
    AVISO: Backup de dados em andamento...
    """

    # Criando objeto interativo para o computador
    computador_interativo = ObjetoInterativo(Computador_rect.left + 95, 
                                           Computador_rect.centery - 30,
                                           60, 60, texto_computador, 
                                           tipo='computador', assets=assets, 
                                           show_indicator=True)

    # Posicionando os objetos interativos para cada arma na mesa
    arma1 = ObjetoInterativo(Mesa_Arma_rect.left + int(LARGURA_MESA * 0.4), 
                            Mesa_Arma_rect.top + int(ALTURA_MESA * 0.4),
                            60, 60, texto_arma1, tipo='arma', assets=assets, show_indicator=True)

    arma2 = ObjetoInterativo(Mesa_Arma_rect.left + int(LARGURA_MESA * 0.75),
                            Mesa_Arma_rect.top + int(ALTURA_MESA * 0.4),
                            60, 60, texto_arma2, tipo='arma', assets=assets, show_indicator=True)

    arma3 = ObjetoInterativo(Mesa_Arma_rect.left + int(LARGURA_MESA * 1.1),
                            Mesa_Arma_rect.top + int(ALTURA_MESA * 0.4),
                            60, 60, texto_arma3, tipo='arma', assets=assets, show_indicator=True)
    
    state = JOGANDO

    # Criando o jogador
    gab_topa_eu = Jogador(assets)
    
    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    all_interactables = pygame.sprite.Group()  # Grupo para objetos interativos
    all_sprites.add(gab_topa_eu)

    # Adiciona objetos interativos ao grupo
    all_interactables.add(arma1)
    all_interactables.add(arma2)
    all_interactables.add(arma3)
    all_interactables.add(computador_interativo)

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

        # Verifica colisões com as bordas da mesa e computador
        colide_mesa = (pygame.Rect.colliderect(borda_superior, gab_topa_eu.rect) or
                      pygame.Rect.colliderect(borda_inferior, gab_topa_eu.rect) or
                      pygame.Rect.colliderect(borda_esquerda, gab_topa_eu.rect) or
                      pygame.Rect.colliderect(borda_direita, gab_topa_eu.rect))
        
        colide_computador = pygame.Rect.colliderect(Computador_colisao, gab_topa_eu.rect)
        
        if colide_mesa or colide_computador:
            gab_topa_eu.rect.x -= gab_topa_eu.speedx
            gab_topa_eu.rect.y -= gab_topa_eu.speedy
            gab_topa_eu.speedy = gab_topa_eu.speedx = 0
            keys_down.clear()

        # Desenha
        screen.fill(PRETO)
        screen.blit(background, background_rect)
        screen.blit(Computador, Computador_rect)  # Desenha o Computador
        screen.blit(Mesa_Arma, Mesa_Arma_rect)  # Desenha a Mesa_Arma

        # Desenha os quadrados amarelos de interação
        for obj in all_interactables:
            if obj.pode_interagir:
                pygame.draw.rect(screen, AMARELO, obj.rect, 2)  # Desenha borda amarela
                s = pygame.Surface((60, 60))
                s.set_alpha(128)  # Transparência
                s.fill(AMARELO)
                screen.blit(s, obj.rect)  # Desenha quadrado amarelo semi-transparente

        # Desenha os objetos interativos
        for obj in all_interactables:
            obj.desenhar(screen)

        all_sprites.draw(screen)

        # Desenha as pistas dos objetos interativos
        for obj in all_interactables:
            obj.desenhar_pista(screen)

        pygame.display.update()

    return state 