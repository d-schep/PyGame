import pygame
from Classe_Jogador import *
from cfg import *
from assets import * 
import random
import time 
from Classe_Botoes_inicio import * 
from Classe_Textos import *
from Classe_Interact import *

class PortaInterativa(ObjetoInterativo):
    def __init__(self, x, y, width, height, codigo, assets):
        super().__init__(x, y, width, height, "Digite o código:", tipo='porta')
        self.codigo = codigo
        self.codigo_digitado = ""
        self.is_unlocked = False
        self.mensagem_erro = ""
        self.tempo_erro = 0

    def handle_keypress(self, event):
        if self.mostrando_pista and event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                           pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                self.codigo_digitado += event.unicode
                if len(self.codigo_digitado) == len(self.codigo):
                    if self.codigo_digitado == self.codigo:
                        self.is_unlocked = True
                        self.texto = "Porta desbloqueada!"
                    else:
                        self.codigo_digitado = ""
                        self.mensagem_erro = "Código incorreto!"
                        self.tempo_erro = time.time()
            elif event.key == pygame.K_BACKSPACE:
                self.codigo_digitado = self.codigo_digitado[:-1]

    def desenhar_pista(self, screen):
        if self.mostrando_pista:
            fonte = pygame.font.Font(None, 36)
            texto_base = f"Digite o código: {self.codigo_digitado}"
            texto_surface = fonte.render(texto_base, True, (255, 255, 255))
            screen.blit(texto_surface, (LARGURA//2 - texto_surface.get_width()//2, ALTURA - 50))

            if self.mensagem_erro and time.time() - self.tempo_erro < 2:
                texto_erro = fonte.render(self.mensagem_erro, True, (255, 0, 0))
                screen.blit(texto_erro, (LARGURA//2 - texto_erro.get_width()//2, ALTURA - 100))

def sala_1(screen):
    clock = pygame.time.Clock()
    assets = load_assets()

    Mesa = assets[MESA]
    Mesa_rect = Mesa.get_rect()
    Mesa_rect.topleft = (600, 350) 

    Estante = assets[ESTANTE]
    Estante_rect = Estante.get_rect()
    Estante_rect.topleft = (910,10)   

    Sofa = assets[SOFA]
    Sofa_rect = Sofa.get_rect()
    Sofa_rect.topleft = (350,20)  

    # Criando a porta interativa
    porta = PortaInterativa(750, ALTURA//4 - 80, 108, 120, "1234", assets)
    
    # Criando objetos interativos com pistas
    texto_livro = "\n\n\n"  # Texto vazio para o livro
    
    # Ajustando posições para corresponder melhor aos objetos
    livro_sofa = ObjetoInterativo(400, 200, 30, 30, texto_livro, tipo='livro', assets=assets)
    gaveta_mesa = ObjetoInterativo(620, 420, 40, 20, "Achei um papel amassado com o número 2...")
    objeto_estante = ObjetoInterativo(930, 200, 30, 30, "Tem algo riscado na estante... os números '34'")

    background = assets[TELA_DE_FUNDO_ESCAPE_1]
    background_rect = background.get_rect()
    state = JOGANDO

    # == GAB ==
    grupos = {}
    zumbi = pygame.Rect((0,0),(250,170))
    parede_esquerda = pygame.Rect((0,ALTURA-115),(CENTROx-130,ALTURA-115))
    all_death =  pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_interactables = pygame.sprite.Group()  # Grupo para objetos interativos
    grupos['TODOS'] = all_sprites
    grupos['MATAVEIS'] = all_death
    grupos['INTERATIVOS'] = all_interactables

    # Adiciona objetos interativos ao grupo
    all_interactables.add(livro_sofa)
    all_interactables.add(gaveta_mesa)
    all_interactables.add(objeto_estante)
    all_interactables.add(porta)

    gab_topa_eu = Jogador(assets)
    all_sprites.add(gab_topa_eu)
    
    keys_down = {}
    while state == JOGANDO:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                state = QUIT
            if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                state = MORTO
            # Verifica interação com objetos (tecla E)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                for obj in all_interactables:
                    obj.tentar_interagir()
            
            # Handle porta keypress
            porta.handle_keypress(event)
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
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
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
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
                    
                    # Remove a tecla do dicionário após soltá-la
                    keys_down.pop(event.key)

        if state == JOGANDO:
            hit_zumbi = pygame.Rect.colliderect(zumbi,gab_topa_eu)
            colide_parede = pygame.Rect.colliderect(parede_esquerda,gab_topa_eu)
            colide_mesa =  pygame.Rect.colliderect(Mesa_rect,gab_topa_eu)
            
            # Verifica se o jogador pode passar pela porta
            if pygame.Rect.colliderect(porta.rect, gab_topa_eu.rect):
                if porta.is_unlocked:
                    # Transição para próxima sala ou estado de vitória
                    state = QUIT  # Você pode mudar isso para um novo estado para a próxima sala
            
            if hit_zumbi == True:
                state = MORTO
            if colide_parede == True or colide_mesa == True:
                gab_topa_eu.rect.x -= gab_topa_eu.speedx
                gab_topa_eu.rect.y -= gab_topa_eu.speedy
                gab_topa_eu.speedy = gab_topa_eu.speedx = 0
                keys_down.clear()  # Limpa todas as teclas pressionadas

            # Atualiza estado dos objetos interativos
            for obj in all_interactables:
                obj.update(gab_topa_eu)

        screen.fill(PRETO)
        screen.blit(background,background_rect)
        
        # Desenha a porta
        pygame.draw.rect(screen, (139, 69, 19), porta.rect)  # Cor marrom para a porta
        
        screen.blit(Mesa, Mesa_rect)
        screen.blit(Estante, Estante_rect)
        screen.blit(Sofa, Sofa_rect)

        # Desenha os objetos interativos
        for obj in all_interactables:
            obj.desenhar(screen)

        all_sprites.draw(screen)
        all_sprites.update()

        # Desenha as pistas dos objetos interativos
        for obj in all_interactables:
            obj.desenhar_pista(screen)

        pygame.display.update()

    return state

