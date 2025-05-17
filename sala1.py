import pygame
from Classe_Jogador import *
from cfg import *
from assets import * 
import random
import time 
from Classe_Botoes_inicio import * 
from Classe_Textos import *
from Classe_Interact import *

def sala_1(screen):
    clock = pygame.time.Clock()
    assets = load_assets()

    Mesa = assets[MESA]
    Mesa_rect = Mesa.get_rect()
    Mesa_rect.topleft = (600, 350) 

    Estante = assets[ESTANTE]
    Estante_rect = Estante.get_rect()
    Estante_rect.topleft = (910,10)   

    Sofa = assets[SOFA]
    Sofa_rect = Estante.get_rect()
    Sofa_rect.topleft = (350,20)  

    # Criando objetos interativos com pistas
    texto_livro = "Uma menina urina lento\n\n\n" + \
                  "Duas também irritam pessoas"
    
    livro_sofa = ObjetoInterativo(535, 200, 50, 50, texto_livro, tipo='livro', assets=assets)
    gaveta_mesa = ObjetoInterativo(620, 400, 60, 30, "Uma gaveta... talvez tenha algo útil dentro.")
    objeto_estante = ObjetoInterativo(930, 30, 40, 40, "Tem algo interessante na estante...")

    background = assets[TELA_DE_FUNDO_ESCAPE_1]
    background_rect = background.get_rect()
    state = JOGANDO

    # == GAB ==
    grupos = {}
    zumbi = pygame.Rect((0,0),(250,170))
    parede_esquerda = pygame.Rect((0,ALTURA-115),(CENTROx-130,ALTURA-115))
    all_death =  pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_interactables = pygame.sprite.Group()  # Grupo para objetos interativos
    grupos['TODOS'] = all_sprites
    grupos['MATAVEIS'] = all_death
    grupos['INTERATIVOS'] = all_interactables

    # Adiciona objetos interativos ao grupo
    all_interactables.add(livro_sofa)
    all_interactables.add(gaveta_mesa)
    all_interactables.add(objeto_estante)

    gab_topa_eu = Jogador(assets)
    all_sprites.add(gab_topa_eu)
    
    keys_down = {}
    while state == JOGANDO:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                state = QUIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                state = MORTO
            # Verifica interação com objetos (tecla E)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                for obj in all_interactables:
                    obj.tentar_interagir()
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
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
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
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
        if state == JOGANDO:
            hit_zumbi = pygame.Rect.colliderect(zumbi,gab_topa_eu)
            colide_parede = pygame.Rect.colliderect(parede_esquerda,gab_topa_eu)
            colide_mesa =  pygame.Rect.colliderect(Mesa_rect,gab_topa_eu)
            if hit_zumbi == True:
                state = MORTO
            if colide_parede == True or colide_mesa == True:
                gab_topa_eu.rect.x -= gab_topa_eu.speedx
                gab_topa_eu.rect.y -= gab_topa_eu.speedy
                gab_topa_eu.speedy = gab_topa_eu.speedx = 0
                keys_down = {}

            # Atualiza estado dos objetos interativos
            for obj in all_interactables:
                obj.update(gab_topa_eu)

        screen.fill(PRETO)
        screen.blit(background,background_rect)
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

        pygame.display.update()
    return state

