from os import path

# == DIRETORIO DOS ARQUIVOS == 
IMG_DIR = path.join(path.dirname(__file__), 'ativos', 'imgs')
SONS_DIR = path.join(path.dirname(__file__), 'ativos', 'sons')
FONT_DIR = path.join(path.dirname(__file__), 'ativos', 'font')

# Tamanho da tela
LARGURA = 1200
ALTURA = 800
# ==FPS==
FPS = 60
CENTROx = LARGURA/2
CENTROy = ALTURA/2
# ====  TEXTOS ====
# --- Tela de inicio ---
LARG_TIT = 500
ALT_TIT = 150
# == TAMANHO BOTES == 
ALT_BOT = 100
LARG_BOT = 300
# ==== CORES ====
BRANCO = (255,255,255)
PRETO = (0,0,0)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
AMARELO = (255,255,0)
ROXO = (255,0,255)
CIANO = (0,255,255)
CINZA = (40, 40, 40)
ACINZENTADO = (40, 40, 40, 200) # canal alhpa pra mudar a transparencia
BRANCO_ALPHA = (170,170,170,200)

# ==== ESTADOS DO JOGO ====
INICIO = 0
JOGANDO = 1 
QUIT = 2
