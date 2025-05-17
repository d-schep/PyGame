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
    background = assets[TELA_DE_FUNDO_ESCAPE_2]  # Você precisará adicionar esta imagem aos assets
    background_rect = background.get_rect()
    
    state = JOGANDO

    # Criando o jogador
    gab_topa_eu = Jogador(assets)
    
    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    all_sprites.add(gab_topa_eu)

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

        # Desenha
        screen.fill(PRETO)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)

        pygame.display.update()

    return state 