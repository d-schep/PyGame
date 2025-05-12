from Classes_e_sprites import * 
import pygame
from os import path
from config import * 

pygame.init()

# Tamanho da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Escape 60: O Jogo")


# Fonte
fonte_titulo = pygame.font.SysFont("Arial", 64, bold=True)
fonte_opcao = pygame.font.SysFont("Arial", 36, bold=True)

# Carrega imagem de fundo do menu (certifique-se que o arquivo existe)
fundo = pygame.image.load("inicio") 
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

def desenhar_botao(texto, y):
    botao = fonte_opcao.render(texto, True, VERDE)
    x = (LARGURA - botao.get_width()) // 2
    tela.blit(botao, (x, y))
    return pygame.Rect(x, y, botao.get_width(), botao.get_height())

def desenhar_menu():
    tela.blit(fundo, (0, 0))
    titulo = fonte_titulo.render("A Última Porta", True, BRANCO)
    tela.blit(titulo, ((LARGURA - titulo.get_width()) // 2, 100))

    rects = []
    botoes = ["Iniciar Jogo", "Créditos", "Sair"]
    for i, texto in enumerate(botoes):
        y = 250 + i * 70
        rects.append((texto, desenhar_botao(texto, y)))

    return rects

def sala():
    rodando = True
    clock = pygame.time.Clock()
    contador_luz = 0
    luz_acesa = True

    # Som de fundo (opcional - adicione um arquivo 'terror.wav' na pasta)
    # pygame.mixer.music.load("terror.wav")
    # pygame.mixer.music.play(-1)

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    # pygame.mixer.music.stop()
                    rodando = False

        # Simulação de luz piscando
        contador_luz += 1
        if contador_luz > 30:
            luz_acesa = not luz_acesa
            contador_luz = 0

        # Fundo escuro ou apagado
        tela.fill((15, 15, 15) if luz_acesa else (0, 0, 0))

        # Texto de terror
        texto = fonte_titulo.render("Você está na sala escura...", True, (180, 0, 0))
        tela.blit(texto, ((LARGURA - texto.get_width()) // 2, 100))

        # Dica
        dica = fonte_opcao.render("Aperte ESC para voltar ao menu...", True, (100, 100, 100))
        tela.blit(dica, ((LARGURA - dica.get_width()) // 2, ALTURA - 80))

        # Sombra ou elemento visual
        pygame.draw.circle(tela, (50, 50, 50), (LARGURA // 2, ALTURA // 2), 40 if luz_acesa else 20)

        pygame.display.flip()
        clock.tick(30)

def menu_principal():
    while True:
        botoes = desenhar_menu()
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                for texto, rect in botoes:
                    if rect.collidepoint(evento.pos):
                        if texto == "Iniciar Jogo":
                            sala()
                        elif texto == "Créditos":
                            print("Mostrar créditos...")
                        elif texto == "Sair":
                            pygame.quit()
                            sys.exit()

menu_principal()
