import pygame
from os import path
PERSONAGEM = 'personagem'
TELA_INICIAL = 'tela_inicial'
TELA_VITORIA = 'tela_vitoria'
TELA_DERROTA = 'tela_derrota'
TELA_DE_FUNDO_ESCAPE_1 = 'tela_fundo_escape1'
TELA_DE_FUNDO_ESCAPE_2 = 'tela_fundo_escape2'
TELA_DE_FUNDO_ESCAPE_3 = 'tela_fundo_escape3'
DICA_ESCAPE1 = 'dica_escape1'
DICA_ESCAPE2 = 'dica_escape2'
DICA_ESCAPE3 = 'dica_escape3'
DICA_ESCAPE4 = 'dica_escape4'
DICA_ESCAPE5 = 'dica_escape5'
DICA_ESCAPE6 = 'dica_escape6'
DICA_ESCAPE7 = 'dica_escape7'
DICA_ESCAPE8 = 'dica_escape8'
DICA_ESCAPE9 = 'dica_escape9'
DICA_ESCAPE10 = 'dica_escape10'
BARRA_TEMPO = 'barra_tempo'
MUSICA_FUNDO = 'musica_fundo'
SOM_VITORIA = 'som_vitoria'
SOM_DERROTA = 'som_derrota'
SOM_ANDANDO = 'som_andando'
SOM_DICA = 'som_usando_dica'

#IMAGENS
def load_assets():
    assets = {}
    assets[TELA_INICIAL] = pygame.image.load('').convert()
    assets[TELA_INICIAL] = pygame.transform.scale(assets[''], (, ))
    assets[TELA_VITORIA] = pygame.image.load('').convert()
    assets[TELA_VITORIA] = pygame.transform.scale(assets[''], (, ))
    assets[TELA_DERROTA] = pygame.image.load('').convert()
    assets[TELA_DERROTA] = pygame.transform.scale(assets[''], (, ))
    assets[TELA_DE_FUNDO_ESCAPE_1] = pygame.image.load('').convert_alpha()
    assets[TELA_DE_FUNDO_ESCAPE_1] = pygame.transform.scale(assets[''], (, ))
    assets[TELA_DE_FUNDO_ESCAPE_2] = pygame.image.load('').convert_alpha()
    assets[TELA_DE_FUNDO_ESCAPE_2] = pygame.transform.scale(assets[''], (, ))
    assets[TELA_DE_FUNDO_ESCAPE_3] = pygame.image.load('').convert_alpha()
    assets[TELA_DE_FUNDO_ESCAPE_3] = pygame.transform.scale(assets[''], (, ))
    assets[DICA_ESCAPE1] = pygame.image.load('').convert_alpha()
    assets[DICA_ESCAPE1] = pygame.transform.scale(assets[''], (, ))
    assets[DICA_ESCAPE2] = pygame.image.load('').convert_alpha()
    assets[DICA_ESCAPE2] = pygame.transform.scale(assets[''], (, ))
    assets[DICA_ESCAPE3] = pygame.image.load('').convert_alpha()
    assets[DICA_ESCAPE3] = pygame.transform.scale(assets[''], (, ))
    assets[DICA_ESCAPE4] = pygame.image.load('').convert_alpha()
    assets[DICA_ESCAPE4] = pygame.transform.scale(assets[''], (, ))
    assets[DICA_ESCAPE5] = pygame.image.load('').convert_alpha()
    assets[DICA_ESCAPE5] = pygame.transform.scale(assets[''], (, ))
    assets[DICA_ESCAPE6] = pygame.image.load('').convert_alpha()
    assets[DICA_ESCAPE6] = pygame.transform.scale(assets[''], (, ))
    assets[DICA_ESCAPE7] = pygame.image.load('').convert_alpha()
    assets[DICA_ESCAPE7] = pygame.transform.scale(assets[''], (, ))
    assets[DICA_ESCAPE8] = pygame.image.load('').convert_alpha()
    assets[DICA_ESCAPE8] = pygame.transform.scale(assets[''], (, ))
    assets[DICA_ESCAPE9] = pygame.image.load('').convert_alpha()
    assets[DICA_ESCAPE9] = pygame.transform.scale(assets[''], (, ))
    assets[DICA_ESCAPE10] = pygame.image.load('').convert_alpha()
    assets[DICA_ESCAPE10] = pygame.transform.scale(assets[''], (, ))
    assets[BARRA_TEMPO] = pygame.image.load('').convert_alpha()
    assets[BARRA_TEMPO] = pygame.transform.scale(assets[''], (, ))
    assets[PERSONAGEM] = pygame.image.load('').convert_alpha()
    assets[PERSONAGEM] = pygame.transform.scale(assets[''], (, ))

    #SONS

    pygame.mixer.music.load('')
    pygame.mixer.music.set_volume()
    assets[MUSICA_FUNDO] = pygame.mixer.Sound('')
    assets[SOM_VITORIA] = pygame.mixer.Sound('')
    assets[SOM_DERROTA] = pygame.mixer.Sound('')
    assets[SOM_ANDANDO] = pygame.mixer.Sound('')
    assets[SOM_DICA] = pygame.mixer.Sound('')
    return assets