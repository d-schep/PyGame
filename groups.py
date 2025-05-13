import pygame
import os 
from cfg import * 

TODOS_BOTOES = 'bts'
TODOS_TEXTOS = 'txts'
TODOS = 'tds'
def load_grupos():
    all_sprites = pygame.sprite.Group()
    all_botoes = pygame.sprite.Group()
    all_textos = pygame.sprite.Group()
    grupos = {}
    grupos[TODOS] = all_sprites
    grupos[TODOS_BOTOES] = all_botoes
    grupos[TODOS_TEXTOS] = all_textos
    return grupos




