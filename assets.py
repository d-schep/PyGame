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
SOFA = 'sofa'
LIVRO = 'livro'
MONITOR = 'monitor'
PAPEL = 'papel'
PAPEL2 = 'papel2'
PISTABARRIL = 'pistabarril'
MESA_ARMA = 'mesa_arma'
COMPUTADOR = 'computador'
CAMERA = 'camera'
QUADRO = 'quadro'

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
    assets[TELA_DE_FUNDO_ESCAPE_2] = pygame.image.load(os.path.join(IMG_DIR,'Sala_2.png')).convert()
    assets[TELA_DE_FUNDO_ESCAPE_2] = pygame.transform.scale(assets[TELA_DE_FUNDO_ESCAPE_2], (LARGURA,ALTURA))
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
    assets[SOFA] = pygame.image.load(os.path.join(IMG_DIR, 'SOFA1.png')).convert_alpha()
    assets[SOFA] = pygame.transform.scale(assets[SOFA], (LARGURA_SOFA, ALTURA_SOFA))
    assets[LIVRO] = pygame.image.load(os.path.join(IMG_DIR, 'LIVRO1.png')).convert_alpha()
    assets[LIVRO] = pygame.transform.scale(assets[LIVRO], (800, 600))
    assets[PAPEL] = pygame.image.load(os.path.join(IMG_DIR, 'PAPEL1.png')).convert_alpha()
    assets[PAPEL] = pygame.transform.scale(assets[PAPEL], (30, 30))  # Tamanho pequeno para o papel no chão
    assets[PAPEL2] = pygame.image.load(os.path.join(IMG_DIR, 'PAPEL2.png')).convert_alpha()
    assets[PAPEL2] = pygame.transform.scale(assets[PAPEL2], (800, 600))  # Tamanho grande para visualização
    assets[PISTABARRIL] = pygame.image.load(os.path.join(IMG_DIR, 'PistaBarril.png')).convert_alpha()
    assets[PISTABARRIL] = pygame.transform.scale(assets[PISTABARRIL], (800, 600))
    assets[MESA_ARMA] = pygame.image.load(os.path.join(IMG_DIR, 'Mesa_Arma.png')).convert_alpha()
    assets[MESA_ARMA] = pygame.transform.scale(assets[MESA_ARMA], (int(LARGURA_MESA * 1.5), int(ALTURA_MESA * 1.5)))
    assets[COMPUTADOR] = pygame.image.load(os.path.join(IMG_DIR, 'Computador.png')).convert_alpha()
    assets[COMPUTADOR] = pygame.transform.scale(assets[COMPUTADOR], (250, 250))  # Tamanho intermediário
    try:
        # First try loading normally
        assets[MONITOR] = pygame.image.load(os.path.join(IMG_DIR, 'MONITOR1.png')).convert_alpha()
    except pygame.error:
        try:
            # Try loading without convert_alpha
            assets[MONITOR] = pygame.image.load(os.path.join(IMG_DIR, 'MONITOR1.png'))
        except pygame.error:
            print("Error loading MONITOR1.png - Creating fallback surface")
            # Create a fallback surface if loading fails
            assets[MONITOR] = pygame.Surface((700, 500))
            assets[MONITOR].fill((50, 50, 50))  # Dark gray color for monitor
            # Add a screen area
            screen_area = pygame.Surface((600, 400))
            screen_area.fill((0, 0, 0))  # Black screen
            assets[MONITOR].blit(screen_area, (50, 50))  # Position the screen on the monitor
    assets[MONITOR] = pygame.transform.scale(assets[MONITOR], (700, 500))
    assets[CAMERA] = pygame.image.load(os.path.join(IMG_DIR, 'Camera.png')).convert_alpha()
    assets[CAMERA] = pygame.transform.scale(assets[CAMERA], (60, 60))
    assets[QUADRO] = pygame.image.load(os.path.join(IMG_DIR, 'Quadro.png')).convert_alpha()
    assets[QUADRO] = pygame.transform.scale(assets[QUADRO], (300, 200))

#     #SONS

#     pygame.mixer.music.load(os.path.join(SONS_DIR, 'nome do arquivo'))
#     pygame.mixer.music.set_volume()
#     assets[MUSICA_FUNDO] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'nome do arquivo'))
#     assets[SOM_VITORIA] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'nome do arquivo'))
#     assets[SOM_DERROTA] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'nome do arquivo'))
#     assets[SOM_ANDANDO] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'nome do arquivo'))
#     assets[SOM_DICA] = pygame.mixer.Sound(os.path.join(SONS_DIR, 'nome do arquivo'))
    return assets