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
        super().__init__(x, y, width, height, "Pressione E para inserir o código", tipo='porta')
        self.codigo = codigo
        self.codigo_digitado = ""
        self.is_unlocked = False
        self.mensagem_erro = ""
        self.tempo_erro = 0
        self.input_ativo = False
        self.texto = "Pressione E para inserir o código"

    def desenhar_pista(self, screen):
        if self.pode_interagir or self.input_ativo:
            fonte = pygame.font.Font(None, 36)
            
            # Desenha o fundo da interface de senha
            if self.input_ativo:
                # Fundo semi-transparente
                s = pygame.Surface((400, 150))
                s.set_alpha(128)
                s.fill((0, 0, 0))
                screen.blit(s, (LARGURA//2 - 200, ALTURA//2 - 75))
                
                # Título
                titulo = fonte.render("Digite a senha:", True, (255, 255, 255))
                screen.blit(titulo, (LARGURA//2 - titulo.get_width()//2, ALTURA//2 - 50))
                
                # Campo de senha
                senha = "*" * len(self.codigo_digitado)
                senha_surface = fonte.render(senha, True, (255, 255, 255))
                pygame.draw.rect(screen, (100, 100, 100), (LARGURA//2 - 50, ALTURA//2, 100, 40))
                screen.blit(senha_surface, (LARGURA//2 - senha_surface.get_width()//2, ALTURA//2 + 10))
                
                # Instruções
                instrucoes = fonte.render("Pressione E para sair", True, (200, 200, 200))
                screen.blit(instrucoes, (LARGURA//2 - instrucoes.get_width()//2, ALTURA//2 + 50))
            else:
                texto = fonte.render(self.texto, True, (255, 255, 255))
                screen.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA - 50))

            if self.mensagem_erro and time.time() - self.tempo_erro < 2:
                texto_erro = fonte.render(self.mensagem_erro, True, (255, 0, 0))
                screen.blit(texto_erro, (LARGURA//2 - texto_erro.get_width()//2, ALTURA//2 - 100))

def sala_1(screen):
    clock = pygame.time.Clock()
    assets = load_assets()

    Mesa = assets[MESA]
    Mesa_rect = Mesa.get_rect()
    Mesa_rect.topleft = (600, 350)
    # Criar um retângulo de colisão menor que a mesa, com espaço máximo na parte inferior
    Mesa_colisao = pygame.Rect(Mesa_rect.left + 20, Mesa_rect.top + 20, 
                              LARGURA_MESA - 40, ALTURA_MESA - 140)  # Aumentei a redução na altura para 140 pixels

    Estante = assets[ESTANTE]
    Estante_rect = Estante.get_rect()
    Estante_rect.topleft = (910,10)   

    Sofa = assets[SOFA]
    Sofa_rect = Sofa.get_rect()
    Sofa_rect.topleft = (350,20)  

    # Criando a porta interativa
    porta = PortaInterativa(750, ALTURA//4 - 80, 108, 120, "MORPH", assets)
    
    # Criando objetos interativos com pistas
    texto_livro = """Caderno de Lab - Projeto Metamorfose

Amostra 13-α: Mutação Primária
Taxa de replicação: 15.4%
Contaminação: 18.2%
Estabilidade: 8.9%

Nota Dr. Chen:
Número 13 é crucial nos testes.
Verificar posições no alfabeto.
Possível padrão molecular."""
    
    # Ajustando posições para corresponder melhor aos objetos
    livro_sofa = ObjetoInterativo(450, 200, 30, 30, texto_livro, tipo='livro', assets=assets)
    
    # Aumentando a área de interação da mesa e ajustando posição
    gaveta_mesa = ObjetoInterativo(620, 380, 60, 40, """RELATÓRIO - CONFIDENCIAL
Lab 15-P

Incidente:
- Setor 16 comprometido
- Contenção: 18 min
- Ref.13 reagiu com
  composto 15

Nota: Sequência alfabética
encontrada. Ver terminal.""", assets=assets)

    # Aumentando a área de interação da estante e ajustando posição
    objeto_estante = ObjetoInterativo(920, 150, 60, 60, """TERMINAL DO LABORATÓRIO
>> Iniciando sequência...
>> Carregando dados...

Sequência detectada:
13 → início
15 → catálise
18 → base
16 → mutação
8 → final

'Posição = Transformação'""", assets=assets)

    background = assets[TELA_DE_FUNDO_ESCAPE_1]
    background_rect = background.get_rect()
    state = JOGANDO

    # == GAB ==
    grupos = {}
    zumbi = pygame.Rect((0,0),(250,170))
    parede_esquerda = pygame.Rect((0,ALTURA-115),(CENTROx-130,ALTURA-115))
    parede_direita = pygame.Rect((CENTROx+80,ALTURA-115),(LARGURA-(CENTROx+80),ALTURA-115))  # Movida 50 pixels para a esquerda
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
            
            # Handle porta keypress e interações gerais
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                # Primeiro tenta interagir com a porta se estiver perto dela
                if porta.pode_interagir:
                    if porta.input_ativo:  # Se a interface está ativa
                        porta.input_ativo = False  # Fecha a interface
                        porta.codigo_digitado = ""  # Limpa o código digitado
                    else:  # Se a interface está fechada
                        porta.input_ativo = True  # Abre a interface
                        porta.mensagem_erro = ""  # Limpa mensagens de erro
                else:
                    # Se não estiver perto da porta, tenta interagir com outros objetos
                    for obj in [livro_sofa, gaveta_mesa, objeto_estante]:
                        obj.tentar_interagir()

            # Processamento de inputs quando a interface da porta está ativa
            elif event.type == pygame.KEYDOWN and porta.input_ativo:
                if event.key == pygame.K_RETURN:
                    if porta.codigo_digitado.upper() == porta.codigo:
                        porta.is_unlocked = True
                        porta.texto = "Acesso concedido. Porta desbloqueada."
                        porta.input_ativo = False
                    else:
                        porta.mensagem_erro = "Código inválido. Acesso negado."
                        porta.tempo_erro = time.time()
                        porta.codigo_digitado = ""
                elif event.key == pygame.K_BACKSPACE:
                    porta.codigo_digitado = porta.codigo_digitado[:-1]
                elif event.unicode.isalpha() and len(porta.codigo_digitado) < 5:
                    porta.codigo_digitado += event.unicode.upper()
            
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
            colide_parede = pygame.Rect.colliderect(parede_esquerda,gab_topa_eu) or pygame.Rect.colliderect(parede_direita,gab_topa_eu)  # Adicionada colisão com parede direita
            colide_mesa =  pygame.Rect.colliderect(Mesa_colisao,gab_topa_eu)
            
            # Verifica se o jogador pode passar pela porta
            if pygame.Rect.colliderect(porta.rect, gab_topa_eu.rect):
                if porta.is_unlocked:
                    # Transição para próxima sala
                    state = PROXIMA_SALA  # Mudando para o novo estado ao invés de QUIT
            
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

