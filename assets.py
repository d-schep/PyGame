import pygame
import os 
from cfg import * 
pygame.font.init()
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
# ==== GAB ==== 
FRENTE1 = 'personagem'
FRENTE2 = 'frnt'
FRENTE3 = 'FRNETEE'
TRAS1 = 'gbr'
TRAS2 = 'gred'
TRAS3 = 'schepnaldo cheroso'
ESQUERD1 = 'sqerd'
ESQUERD2 = 'sssqe'
ESQUERD3 = 'sqertds'
DIREITA1 = 'drt'
DIREITA2 = 'dd'
DIREITA3 = 'ddd'
# === OBJTS === 
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
GRANADA = 'granada'
TELA_COMP = 'tela_comp'

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
    # === GAB ===
    assets[FRENTE1] = pygame.image.load(os.path.join(IMG_DIR,'Frente_1.png')).convert_alpha()
    assets[FRENTE2] = pygame.image.load(os.path.join(IMG_DIR,'Frente_2.png')).convert_alpha()
    assets[FRENTE3] = pygame.image.load(os.path.join(IMG_DIR,'Frente_3.png')).convert_alpha()
    assets[TRAS1] = pygame.image.load(os.path.join(IMG_DIR,'Trás_1.png')).convert_alpha()
    assets[TRAS2] = pygame.image.load(os.path.join(IMG_DIR,'Trás_2.png')).convert_alpha()
    assets[TRAS3] = pygame.image.load(os.path.join(IMG_DIR,'Trás_3.png')).convert_alpha()
    assets[ESQUERD1] = pygame.image.load(os.path.join(IMG_DIR,'Lado_1.png')).convert_alpha()
    assets[ESQUERD2] = pygame.image.load(os.path.join(IMG_DIR,'Lado_2.png')).convert_alpha()
    assets[ESQUERD3] = pygame.image.load(os.path.join(IMG_DIR,'Lado_3.png')).convert_alpha()
    assets[DIREITA1] = pygame.image.load(os.path.join(IMG_DIR,'Lado_1.png')).convert_alpha()
    assets[DIREITA2] = pygame.image.load(os.path.join(IMG_DIR,'Lado_2.png')).convert_alpha()
    assets[DIREITA3] = pygame.image.load(os.path.join(IMG_DIR,'Lado_3.png')).convert_alpha()

    # === GAB TRANSFORM ===
    # Frente
    assets[FRENTE1] = pygame.transform.scale(assets[FRENTE1], (ALT_GAB+20,LARG_GAB+20))
    assets[FRENTE2] = pygame.transform.scale(assets[FRENTE2], (ALT_GAB+20,LARG_GAB+20))
    assets[FRENTE3] = pygame.transform.scale(assets[FRENTE3], (ALT_GAB+20,LARG_GAB+20))
    
    # Trás
    assets[TRAS1] = pygame.transform.scale(assets[TRAS1], (ALT_GAB+20,LARG_GAB+20))
    assets[TRAS2] = pygame.transform.scale(assets[TRAS2], (ALT_GAB+20,LARG_GAB+20))
    assets[TRAS3] = pygame.transform.scale(assets[TRAS3], (ALT_GAB+20,LARG_GAB+20))
    
    # Lado (direita)
    assets[DIREITA1] = pygame.transform.scale(assets[DIREITA1], (ALT_GAB,LARG_GAB+20))
    assets[DIREITA2] = pygame.transform.scale(assets[DIREITA2], (ALT_GAB,LARG_GAB+20))
    assets[DIREITA3] = pygame.transform.scale(assets[DIREITA3], (ALT_GAB,LARG_GAB+20))
    assets[DIREITA1] = pygame.transform.flip(assets[DIREITA1], True, False)
    # Lado (esquerda) - flip das imagens da direita
    assets[ESQUERD1] = pygame.transform.scale(assets[ESQUERD1], (ALT_GAB,LARG_GAB+20))
    assets[ESQUERD2] = pygame.transform.scale(assets[ESQUERD2], (ALT_GAB,LARG_GAB+20))
    assets[ESQUERD3] = pygame.transform.scale(assets[ESQUERD3], (ALT_GAB,LARG_GAB+20))
    assets[ESQUERD2] = pygame.transform.flip(assets[ESQUERD2], True, False)
    assets[ESQUERD3] = pygame.transform.flip(assets[ESQUERD3], True, False)

    # === OBJECTS === 
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
        assets[MONITOR] = pygame.image.load(os.path.join(IMG_DIR, 'MONITOR1.png')).convert_alpha()
    except pygame.error:
        try:
            assets[MONITOR] = pygame.image.load(os.path.join(IMG_DIR, 'MONITOR1.png'))
        except pygame.error:
            print("Error loading MONITOR1.png - Creating fallback surface")
            assets[MONITOR] = pygame.Surface((700, 500))
            assets[MONITOR].fill((50, 50, 50))
            screen_area = pygame.Surface((600, 400))
            screen_area.fill((0, 0, 0))
            assets[MONITOR].blit(screen_area, (50, 50))
    assets[MONITOR] = pygame.transform.scale(assets[MONITOR], (700, 500))
    assets[CAMERA] = pygame.image.load(os.path.join(IMG_DIR, 'Camera.png')).convert_alpha()
    assets[CAMERA] = pygame.transform.scale(assets[CAMERA], (60, 60))
    assets[QUADRO] = pygame.image.load(os.path.join(IMG_DIR, 'Quadro.png')).convert_alpha()
    assets[QUADRO] = pygame.transform.scale(assets[QUADRO], (300, 200))
    assets[GRANADA] = pygame.image.load(os.path.join(IMG_DIR, 'Granadas.png')).convert_alpha()
    assets[GRANADA] = pygame.transform.scale(assets[GRANADA], (100, 100))
    assets[TELA_COMP] = pygame.image.load(os.path.join(IMG_DIR, 'Tela_Comp.png')).convert_alpha()

    return assets