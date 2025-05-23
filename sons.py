import pygame
import os
from cfg import *

# Constantes dos efeitos sonoros
SOM_ZUMBI = 'zumbi_ambiente'
SOM_MENU = 'musica_menu'
SOM_VITORIA = 'vitoria'
SOM_ANDANDO = 'andando'
SOM_SUSPENSE = 'suspense'
SOM_MORTE = 'morte'

# Objetos de som globais
sons = {}
musica_atual = None

def carregar_sons():
    """Carrega todos os sons do jogo"""
    global sons
    
    # Lista de sons para carregar
    lista_sons = {
        SOM_ZUMBI: 'zumbi_ambiente.wav',
        SOM_MENU: 'musica_menu.wav',
        SOM_VITORIA: 'vitoria.mp3',  # Alterado para .mp3
        SOM_ANDANDO: 'andando.wav',
        SOM_SUSPENSE: 'suspense.wav',
        SOM_MORTE: 'morte.wav'
    }
    
    # Tenta carregar cada som
    for nome_som, arquivo in lista_sons.items():
        try:
            caminho_arquivo = os.path.join(SONS_DIR, arquivo)
            if os.path.exists(caminho_arquivo):
                sons[nome_som] = pygame.mixer.Sound(caminho_arquivo)
                # Define volumes específicos para cada som
                if nome_som == SOM_ZUMBI:
                    sons[nome_som].set_volume(0.3)
                elif nome_som == SOM_ANDANDO:
                    sons[nome_som].set_volume(0.2)
                elif nome_som == SOM_SUSPENSE:
                    sons[nome_som].set_volume(0.4)
                elif nome_som == SOM_MORTE:
                    sons[nome_som].set_volume(0.5)
                elif nome_som == SOM_VITORIA:
                    sons[nome_som].set_volume(0.5)
                print(f"Som carregado com sucesso: {arquivo}")
            else:
                print(f"Aviso: Arquivo de som não encontrado: {arquivo}")
                # Cria um som vazio para não dar erro
                sons[nome_som] = pygame.mixer.Sound(buffer=bytes(44))
        except Exception as e:
            print(f"Erro ao carregar som {arquivo}: {str(e)}")
            # Cria um som vazio para não dar erro
            sons[nome_som] = pygame.mixer.Sound(buffer=bytes(44))

def tocar_som(nome_som, loops=0):
    """Toca um efeito sonoro"""
    if nome_som in sons:
        try:
            sons[nome_som].play(loops)
        except Exception as e:
            print(f"Erro ao tocar som {nome_som}: {str(e)}")

def parar_som(nome_som):
    """Para um efeito sonoro específico"""
    if nome_som in sons:
        try:
            sons[nome_som].stop()
        except Exception as e:
            print(f"Erro ao parar som {nome_som}: {str(e)}")

def parar_todos_sons():
    """Para todos os sons que estão tocando"""
    for som in sons.values():
        try:
            som.stop()
        except Exception as e:
            print(f"Erro ao parar som: {str(e)}")

def tocar_musica(nome_musica):
    """Toca música de fundo"""
    global musica_atual
    if musica_atual:
        pygame.mixer.music.stop()
    try:
        caminho_musica = os.path.join(SONS_DIR, f'{nome_musica}.wav')
        if os.path.exists(caminho_musica):
            pygame.mixer.music.load(caminho_musica)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
            musica_atual = nome_musica
            print(f"Música carregada com sucesso: {nome_musica}")
        else:
            print(f"Aviso: Arquivo de música não encontrado: {nome_musica}")
    except Exception as e:
        print(f"Erro ao carregar música {nome_musica}: {str(e)}")

def parar_musica():
    """Para a música de fundo"""
    pygame.mixer.music.stop()
    global musica_atual
    musica_atual = None 