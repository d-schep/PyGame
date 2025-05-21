import pygame
from Classe_Jogador import *
from cfg import *
from assets import * 
import random
import time 
from Classe_Botoes_inicio import * 
from Classe_Textos import *
from Classe_Interact import *
from Classe_porta import * 
from timer import desenhar_timer, atualizar_timer, timer_ativo  # Importando timer_ativo


def sala_1(screen):
    clock = pygame.time.Clock()
    assets = load_assets()

    Mesa = assets[MESA]
    Mesa_rect = Mesa.get_rect()
    Mesa_rect.topleft = (600, 350)
    # Criar um retângulo de colisão menor que a mesa, com espaço máximo na parte inferior
    Mesa_colisao = pygame.Rect(Mesa_rect.left + 20, Mesa_rect.top + 20, 
                              LARGURA_MESA - 40, ALTURA_MESA - 140)  # Aumentei a redução na altura para 140 pixels

    Estante = assets[ESTANTE]
    Estante_rect = Estante.get_rect()
    Estante_rect.topleft = (910,10)   
    # Criar um retângulo de colisão para a estante - altura reduzida
    Estante_colisao = pygame.Rect(Estante_rect.left + 20, Estante_rect.top + 20,
                                 LARGURA_ESTANTE - 40, ALTURA_ESTANTE - 150)  # Reduzindo 150 pixels da altura

    Sofa = assets[SOFA]
    Sofa_rect = Sofa.get_rect()
    Sofa_rect.topleft = (350,20)  
    # Criar um retângulo de colisão para o sofá - altura muito reduzida
    Sofa_colisao = pygame.Rect(Sofa_rect.left + 20, Sofa_rect.top + 20,
                              LARGURA_SOFA - 40, ALTURA_SOFA - 300)  # Reduzindo 300 pixels da altura

    # Criando a porta interativa (x=750, y=ALTURA//4 - 80)
    porta = PortaInterativa(750, ALTURA//4 - 80, 108, 120, "41100", assets)
    porta.rect = pygame.Rect(750, ALTURA//4 - 80, 108, 120)
    porta.pode_interagir = False  # Inicializa como False
    
    # Criando objetos interativos com pistas
    texto_livro = """19 9 1 13 5 4 5 4 18 1 20 1 10 5 19 5 21 17 19 5 20 14 1 5 22 12 1 19 19 15 14 5 5 12 5 5 21 7 5 16 15 1 8 3 15 14 15 4 1 19 19 1 13 1 12 5 16 1 16 15 5 20 1 1 22"""
    
    # Livro no sofá (x=450, y=200)
    livro_sofa = ObjetoInterativo(550, 200, 30, 30, texto_livro, tipo='livro', assets=assets)

    # Papel amassado no chão (x=300, y=600)
    texto_papel = """📜 Lista de sobrevivência – Entrada da base, 3 dias atrás

4 galões de água

6 enlatados

10 barras de cereal

1 lanterna

5 munições

7 curativos

8 pilhas"""

    papel_chao = ObjetoInterativo(270, 620, 30, 30, texto_papel, tipo='papel', assets=assets, show_indicator=False)
    
    # Terminal na mesa (x=620, y=380)
    gaveta_mesa = ObjetoInterativo(670, 410, 60, 40, """


                    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                     VOCÊ NUNCA IRÁ
                     SAIR DA SALA,
                      DESISTA!!!
                    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀


""", assets=assets)

    # Barril com pista (x=100, y=500)
    barril = ObjetoInterativo(100, 600, 40, 40, """
    """, tipo='barril', assets=assets)

    background = assets[TELA_DE_FUNDO_ESCAPE_1]
    background_rect = background.get_rect()
    state = JOGANDO

    # == GAB ==
    grupos = {}
    zumbi = pygame.Rect((0,0),(250,170))
    parede_esquerda = pygame.Rect((0,ALTURA-115),(CENTROx-130,ALTURA-115))
    parede_direita = pygame.Rect((CENTROx+80,ALTURA-115),(LARGURA-(CENTROx+80),ALTURA-115))  # Movida 50 pixels para a esquerda
    all_death =  pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_interactables = pygame.sprite.Group()  # Grupo para objetos interativos
    grupos['TODOS'] = all_sprites
    grupos['MATAVEIS'] = all_death
    grupos['INTERATIVOS'] = all_interactables

    # Adiciona objetos interativos ao grupo
    all_interactables.add(livro_sofa)
    all_interactables.add(gaveta_mesa)
    all_interactables.add(porta)
    all_interactables.add(papel_chao)
    all_interactables.add(barril)

    gab_topa_eu = Jogador(assets)
    all_sprites.add(gab_topa_eu)
    
    keys_down = {}
    while state == JOGANDO:
        clock.tick(FPS)
        
        pista_aberta = porta.input_ativo or any(getattr(obj, 'mostrando_pista', False) for obj in all_interactables)

        # Hard lock: trava a posição do jogador enquanto pista ou senha estiver aberta
        if (pista_aberta or porta.input_ativo) and not hasattr(gab_topa_eu, 'pos_travada'):
            gab_topa_eu.pos_travada = gab_topa_eu.rect.topleft

        if (pista_aberta or porta.input_ativo) and hasattr(gab_topa_eu, 'pos_travada'):
            gab_topa_eu.rect.topleft = gab_topa_eu.pos_travada
            gab_topa_eu.speedx = 0
            gab_topa_eu.speedy = 0
            keys_down.clear()
        else:
            if hasattr(gab_topa_eu, 'pos_travada'):
                del gab_topa_eu.pos_travada

        # Salva a posição do jogador antes do update
        pos_antiga = gab_topa_eu.rect.topleft

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT

            # Se a interface da porta está ativa, só processa eventos para a porta
            if porta.input_ativo:
                if event.type == pygame.KEYDOWN:
                    porta.handle_keypress(event)
                else:
                    porta.handle_mouse(event)
                continue  # Pula o restante do processamento de eventos

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    state = QUIT
                if event.key == pygame.K_l:
                    state = MORTO
                if event.key == pygame.K_p:
                    state = PROXIMA_SALA
                # Handle porta keypress e interações gerais
                if event.key == pygame.K_e:
                    # Primeiro tenta interagir com a porta se estiver perto dela
                    if porta.pode_interagir:
                        if porta.input_ativo:  # Se a interface está ativa
                            porta.input_ativo = False  # Fecha a interface
                            porta.codigo_digitado = ""  # Limpa o código digitado
                        else:  # Se a interface está fechada
                            porta.input_ativo = True  # Abre a interface
                            porta.mensagem_erro = ""  # Limpa mensagens de erro
                    else:
                        # Se não estiver perto da porta, tenta interagir com outros objetos
                        for obj in [livro_sofa, gaveta_mesa, papel_chao, barril]:
                            obj.tentar_interagir()

            # Controles do jogador (só se nenhuma pista estiver aberta e porta não estiver ativa)
            if not pista_aberta and event.type == pygame.KEYDOWN:
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

            if not pista_aberta and event.type == pygame.KEYUP:
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

        if state == JOGANDO:
            hit_zumbi = pygame.Rect.colliderect(zumbi,gab_topa_eu)
            colide_parede = pygame.Rect.colliderect(parede_esquerda,gab_topa_eu) or pygame.Rect.colliderect(parede_direita,gab_topa_eu)
            colide_mesa = pygame.Rect.colliderect(Mesa_colisao,gab_topa_eu)
            colide_estante = pygame.Rect.colliderect(Estante_colisao,gab_topa_eu)
            colide_sofa = pygame.Rect.colliderect(Sofa_colisao,gab_topa_eu)
            
            # Verifica se o jogador pode passar pela porta
            if pygame.Rect.colliderect(porta.rect, gab_topa_eu.rect):
                if porta.is_unlocked:
                    # Transição para próxima sala
                    state = PROXIMA_SALA
            
            if hit_zumbi == True:
                state = MORTO
            if colide_parede == True or colide_mesa == True or colide_estante == True or colide_sofa == True:
                gab_topa_eu.rect.x -= gab_topa_eu.speedx
                gab_topa_eu.rect.y -= gab_topa_eu.speedy
                gab_topa_eu.speedy = gab_topa_eu.speedx = 0
                keys_down.clear()  # Limpa todas as teclas pressionadas

            # Atualiza estado dos objetos interativos
            for obj in all_interactables:
                obj.update(gab_topa_eu)

        screen.fill(PRETO)
        screen.blit(background,background_rect)
        
        # Desenha a porta
        # pygame.draw.rect(screen, (139, 69, 19), porta.rect)  # Removido o retângulo marrom da porta
        
        screen.blit(Mesa, Mesa_rect)
        screen.blit(Estante, Estante_rect)
        screen.blit(Sofa, Sofa_rect)

        # Desenha os objetos interativos
        for obj in all_interactables:
            obj.desenhar(screen)

        all_sprites.draw(screen)
        all_sprites.update()

        # Desenha as pistas dos objetos interativos
        for obj in all_interactables:
            obj.desenhar_pista(screen)

        # Desenha o timer
        tempo_restante = atualizar_timer()
        if tempo_restante <= 0:
            state = MORTO
        desenhar_timer(screen)

        pygame.display.flip()

    return state

