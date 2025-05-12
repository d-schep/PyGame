import pygame
from os import path
PERSONAGEM = 'personagem'
TELA_INICIAL = 'tela_inicial'
TELA_VITORIA = 'tela_vitoria'
TELA_DERROTA = 'tela_derrota'
TELA_DE_FUNDO_ESCAPE_1 = 'tela_fundo_escape1'
TELA_DE_FUNDO_ESCAPE_2 = 'tela_fundo_escape2'
TELA_DE_FUNDO_ESCAPE_3 = 'tela_fundo_escape3'
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
    assets['dica_escape1'] = pygame.image.load('').convert_alpha()
    assets['dica_escape1'] = pygame.transform.scale(assets[''], (, ))
    assets['dica_escape2'] = pygame.image.load('').convert_alpha()
    assets['dica_escape2'] = pygame.transform.scale(assets[''], (, ))
    assets['dica_escape3'] = pygame.image.load('').convert_alpha()
    assets['dica_escape3'] = pygame.transform.scale(assets[''], (, ))
    assets['dica_escape4'] = pygame.image.load('').convert_alpha()
    assets['dica_escape4'] = pygame.transform.scale(assets[''], (, ))
    assets['dica_escape5'] = pygame.image.load('').convert_alpha()
    assets['dica_escape5'] = pygame.transform.scale(assets[''], (, ))
    assets['dica_escape6'] = pygame.image.load('').convert_alpha()
    assets['dica_escape6'] = pygame.transform.scale(assets[''], (, ))
    assets['dica_escape7'] = pygame.image.load('').convert_alpha()
    assets['dica_escape7'] = pygame.transform.scale(assets[''], (, ))
    assets['dica_escape8'] = pygame.image.load('').convert_alpha()
    assets['dica_escape8'] = pygame.transform.scale(assets[''], (, ))
    assets['dica_escape9'] = pygame.image.load('').convert_alpha()
    assets['dica_escape9'] = pygame.transform.scale(assets[''], (, ))
    assets['dica_escape10'] = pygame.image.load('').convert_alpha()
    assets['dica_escape10'] = pygame.transform.scale(assets[''], (, ))
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