import pygame
import os 
from cfg import * 
pygame.font.init()
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
FONTE_BOTAO = 'fnt_btao'
TELA_PRETA = 'tela_preta'
IMG_TITULO = 'img_titulo'
GAB_TRAS = 'gbr'
ESQUERDA = 'sqerd'
DIREITA = 'drt'
MESA = 'mesa'
ESTANTE = 'estante'
#IMAGENS
def load_assets():
    assets = {}
    assets[IMG_TITULO] = pygame.image.load(os.path.join(IMG_DIR, 'titulo.png'))
    assets[IMG_TITULO] = pygame.transform.scale(assets[IMG_TITULO], (800,400))
    assets[FONTE_BOTAO] = pygame.font.Font(os.path.join(FONT_DIR,'PressStart2P.ttf'),28)
    assets[TELA_INICIAL] = pygame.image.load(os.path.join(IMG_DIR,'bckg.png')).convert()
    assets[TELA_INICIAL] = pygame.transform.scale(assets[TELA_INICIAL], (LARGURA,ALTURA))
    assets[TELA_DE_FUNDO_ESCAPE_1] = pygame.image.load(os.path.join(IMG_DIR,'Sala_1.png')).convert()
    assets[TELA_DE_FUNDO_ESCAPE_1] = pygame.transform.scale(assets[TELA_DE_FUNDO_ESCAPE_1], (LARGURA,ALTURA))
    assets[PERSONAGEM] = pygame.image.load(os.path.join(IMG_DIR,'gab_de_frente.png')).convert_alpha()
    assets[PERSONAGEM] = pygame.transform.scale(assets[PERSONAGEM], (ALT_GAB,LARG_GAB))
    assets[GAB_TRAS] = pygame.image.load(os.path.join(IMG_DIR,'COSTAS.png')).convert_alpha()
    assets[GAB_TRAS] = pygame.transform.scale(assets[GAB_TRAS], (ALT_GAB,LARG_GAB))
    assets[DIREITA] = pygame.image.load(os.path.join(IMG_DIR, 'direita.png')).convert_alpha()
    assets[ESQUERDA] = pygame.image.load(os.path.join(IMG_DIR, 'esquerda.png')).convert_alpha()
    assets[DIREITA] = pygame.transform.scale(assets[DIREITA], (ALT_GAB-20,LARG_GAB))
    assets[ESQUERDA] = pygame.transform.scale(assets[ESQUERDA], (ALT_GAB-20,LARG_GAB))
    assets[MESA] = pygame.image.load(os.path.join(IMG_DIR,'MESA1.png')).convert_alpha()
    assets[MESA] = pygame.transform.scale(assets[MESA], (LARGURA_MESA, ALTURA_MESA))
    assets[ESTANTE] = pygame.image.load(os.path.join(IMG_DIR, 'ESTANTE1.png')).convert_alpha()
    assets[ESTANTE] = pygame.transform.scale(assets[ESTANTE], (LARGURA_ESTANTE, ALTURA_ESTANTE))

#     #SONS

#     pygame.mixer.music.load(os.path.join(SONS_DIR, 'nome do arquivo'))
#     pygame.mixer.music.set_volume()
#     assets[MUSICA_FUNDO] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'nome do arquivo'))
#     assets[SOM_VITORIA] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'nome do arquivo'))
#     assets[SOM_DERROTA] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'nome do arquivo'))
#     assets[SOM_ANDANDO] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'nome do arquivo'))
#     assets[SOM_DICA] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'nome do arquivo'))
    return assets