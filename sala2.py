import pygame
from Classe_Jogador import *
from cfg import *
from assets import *
import random
import time
from Classe_Botoes_inicio import *
from Classe_Textos import *
from Classe_Interact import *
import math
from Classe_porta import *
from timer import desenhar_timer, parar_timer, atualizar_timer, timer_ativo  # Importando timer_ativo

def sala_2(screen):
    clock = pygame.time.Clock()
    assets = load_assets()
    state = PROXIMA_SALA  # Definindo o estado inicial

    # Carregando a nova imagem de fundo (sala de armas)
    background = assets[TELA_DE_FUNDO_ESCAPE_2]
    background_rect = background.get_rect()
    
    # Criando a porta interativa
    porta = PortaInterativa(750, ALTURA//4 - 80, 108, 120, "UZI MINI\nSHOTGUN\n7.62\nGK18L3", assets)
    # Ajusta a área de interação da porta para ser mais precisa
    porta.rect = pygame.Rect(750, ALTURA//4 - 80, 108, 120)
    porta.pode_interagir = False  # Inicializa como False
    
    # Adicionando Mesa_Arma
    Mesa_Arma = assets[MESA_ARMA]
    Mesa_Arma_rect = Mesa_Arma.get_rect()
    # Centralizando a mesa na sala
    Mesa_Arma_rect.centerx = LARGURA // 2
    Mesa_Arma_rect.centery = ALTURA // 2
    # Criar um retângulo de colisão menor e centralizado
    Mesa_colisao = pygame.Rect(Mesa_Arma_rect.centerx - 100, Mesa_Arma_rect.centery - 100, 
                              200, 100)  # Colisão de 200x100 pixels centralizada na mesa, movida 50 pixels para cima

    # Adicionando Computador
    Computador = assets[COMPUTADOR]
    Computador_rect = Computador.get_rect()
    # Posicionando o computador mais para a esquerda no fundo da sala
    Computador_rect.left = 100
    Computador_rect.top = 40
    # Área de colisão para o computador - justa ao corpo
    Computador_colisao = pygame.Rect(Computador_rect.left + 40, Computador_rect.top + 40, 170, 100)

    # Adicionando Camera
    Camera_img = assets[CAMERA]
    Camera_rect = Camera_img.get_rect()
    # Posicionando a camera na parede superior direita
    Camera_rect.right = LARGURA - 60
    Camera_rect.top = 40

    # Adicionando Quadro
    Quadro_img = assets[QUADRO]
    Quadro_rect = Quadro_img.get_rect()
    Quadro_rect.topleft = (450, 40)  # Posição exemplo: canto superior esquerdo

    # Criando objetos interativos para cada arma
    texto_arma1 = """
    Glock 17
    Pistola
    9mm
    SN: --------
    """

    texto_arma2 = """
    AK-47
    Fuzil
    -----mm
    SN: RN7B43
    """

    texto_arma3 = """
    --------
    Submetralhadora
    9mm
    SN: UM1009J
    """

    texto_arma4 = """
    Mossberg 500
    ----------
    12 GA
    SN: SM416K0
    """

    # Textos para as pistas
    texto_tabela_substituicao = """
    A = 7    H = K     O = 3     V = W
    B = W    I = 9     P = M     W = 5
    C = 4    J = G     Q = 8     X = T
    D = L    K = 2     R = B     Y = N
    E = P    L = 6     S = 1     Z = H
    F = Q    M = D     T = X     1 = K
    G = J    N = Y     U = V     2 = 1
    """

    texto_codigo = """
    J 2 G Q 6 O
    """

    texto_equacao = """
    (2 × π) + 1.34
    """

    texto_morse = """
    ..- --.. .. / -- .. -. ..
    """

    texto_quebra_cabeca = """
    S___G__

    Usada de perto.

    Espalha medo.

    Preencha as lacunas.

    Em Inglês
    """

    texto_computador = """
    Terminal de Segurança
    Status: ONLINE
    Nível: ADMINISTRADOR
    """

    # Dicas/páginas do computador
    dicas_computador = [
        texto_computador,
        texto_codigo,
        texto_tabela_substituicao,
        texto_equacao,
        texto_morse,
        texto_quebra_cabeca,
    ]

    # Posicionando os objetos interativos para cada arma na mesa
    arma1 = ObjetoInterativo(Mesa_Arma_rect.left + 50, 
                            Mesa_Arma_rect.top - 20,
                            60, 60, texto_arma1, tipo='arma', assets=assets, show_indicator=True)

    arma2 = ObjetoInterativo(Mesa_Arma_rect.right - 110,
                            Mesa_Arma_rect.top - 20,
                            60, 60, texto_arma2, tipo='arma', assets=assets, show_indicator=True)

    arma3 = ObjetoInterativo(Mesa_Arma_rect.left + 50,
                            Mesa_Arma_rect.bottom - 110,
                            60, 60, texto_arma3, tipo='arma', assets=assets, show_indicator=True)

    arma4 = ObjetoInterativo(Mesa_Arma_rect.right - 110,
                            Mesa_Arma_rect.bottom - 110,
                            60, 60, texto_arma4, tipo='arma', assets=assets, show_indicator=True)

    # Criando objeto interativo para o computador (área de interação grande na frente)
    comp_x = Computador_rect.left + Computador_rect.width // 2 - 60
    comp_y = Computador_rect.bottom - 60
    computador_interativo = ObjetoInterativo(comp_x, comp_y, 120, 120, dicas_computador[0], 
                                           tipo='computador', assets=assets, 
                                           show_indicator=True)
    computador_interativo.dicas = dicas_computador
    computador_interativo.pagina_atual = 0
    computador_interativo.tela_comp = assets[TELA_COMP]  # Store the computer screen image
    # Ajusta a área de interação para ser mais precisa
    computador_interativo.rect = pygame.Rect(Computador_rect.left + 40, Computador_rect.top + 40, 170, 120)

    # Criando objeto interativo para a granada (direita da mesa, no chão)
    granada = ObjetoInterativo(Mesa_Arma_rect.right + 150,
                              Mesa_Arma_rect.bottom - 115,
                              40, 40, "", tipo='granada', assets=assets, show_indicator=False)

    # Ajustando a colisão da caixa do lado direito
    caixa_colisao = pygame.Rect(LARGURA - 300, ALTURA//2 - 20, 120, 20)

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    all_interactables = pygame.sprite.Group()  # Grupo para objetos interativos
    
    # Criando o jogador
    gab_topa_eu = Jogador(assets)
    all_sprites.add(gab_topa_eu)  # Adicionando o jogador ao grupo de sprites

    # Adiciona objetos interativos ao grupo
    all_interactables.add(arma1)
    all_interactables.add(arma2)
    all_interactables.add(arma3)
    all_interactables.add(arma4)
    all_interactables.add(computador_interativo)
    all_interactables.add(granada)
    all_interactables.add(porta)  # Adicionando a porta ao grupo de interativos

    # Posiciona o jogador na entrada da nova sala, mais para frente
    gab_topa_eu.rect.x = LARGURA // 2
    gab_topa_eu.rect.y = ALTURA - 300  # Movido para frente (era -100)

    # Adicionando paredes invisíveis para colisão
    parede_esquerda = pygame.Rect((0,ALTURA-115),(CENTROx-130,ALTURA-115))  # Ajustado para ficar igual à sala1
    parede_direita = pygame.Rect((CENTROx+80,ALTURA-115),(LARGURA-(CENTROx+80),ALTURA-115))  # Ajustado para ficar igual à sala1
    
    # Adicionando paredes laterais finas
    parede_lateral_esquerda = pygame.Rect((0,0),(50,ALTURA))
    parede_lateral_direita = pygame.Rect((LARGURA-50,0),(50,ALTURA))

    keys_down = {}
    while state == PROXIMA_SALA:
        clock.tick(FPS)

        pista_aberta = any(getattr(obj, 'mostrando_pista', False) for obj in all_interactables) or porta.input_ativo

        # Hard lock: trava a posição do jogador enquanto pista ou senha estiver aberta
        if pista_aberta and not hasattr(gab_topa_eu, 'pos_travada'):
            gab_topa_eu.pos_travada = gab_topa_eu.rect.topleft

        if pista_aberta and hasattr(gab_topa_eu, 'pos_travada'):
            gab_topa_eu.rect.topleft = gab_topa_eu.pos_travada
            gab_topa_eu.speedx = 0
            gab_topa_eu.speedy = 0
            keys_down.clear()
        else:
            if hasattr(gab_topa_eu, 'pos_travada'):
                del gab_topa_eu.pos_travada

        # Salva a posição do jogador antes do update
        pos_antiga = gab_topa_eu.rect.topleft

        # --- ANIMAÇÃO DA CÂMERA ---
        t = pygame.time.get_ticks() / 1000  # tempo em segundos
        angulo = 20 * math.sin(t * 0.5)  # Oscila de -20 a +20 graus, mais devagar
        Camera_img_anim = pygame.transform.rotate(Camera_img, angulo)
        Camera_anim_rect = Camera_img_anim.get_rect(center=Camera_rect.center)

        # Luzinha vermelha piscando
        luz_on = int((t * 2) % 2) == 0  # Pisca a cada meio segundo
        luz_cor = (255, 0, 0) if luz_on else (80, 0, 0)
        # Posição da luz: ponta da câmera (direita da imagem rotacionada)
        luz_raio = 7
        luz_offset = 45  # distância do centro até a ponta
        luz_x = Camera_anim_rect.centerx + luz_offset * math.cos(math.radians(angulo))
        luz_y = Camera_anim_rect.centery + luz_offset * math.sin(math.radians(angulo))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT

            # Sempre processa eventos da porta se a interface estiver ativa
            if porta.input_ativo:
                if event.type == pygame.KEYDOWN:
                    porta.handle_keypress(event)
                    # Se o jogador acertou o código, para o timer
                    if porta.is_unlocked:
                        parar_timer()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    porta.handle_mouse(event)
                continue  # Não processa mais nada neste evento

            # Sempre processa eventos do computador se a interface estiver ativa
            if computador_interativo.mostrando_pista:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        computador_interativo.pagina_atual = (computador_interativo.pagina_atual + 1) % len(computador_interativo.dicas)
                        computador_interativo.texto = computador_interativo.dicas[computador_interativo.pagina_atual]
                        computador_interativo.atualizar_tela()
                    elif event.key == pygame.K_e:
                        computador_interativo.mostrando_pista = False
                continue  # Não processa mais nada neste evento

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    state = QUIT
                if event.key == pygame.K_RETURN:
                    state = MORTO
                
                # Handle porta keypress e interações gerais
                if event.key == pygame.K_e:
                    # Primeiro tenta interagir com a porta se estiver perto dela
                    if porta.pode_interagir or porta.input_ativo:
                        if porta.input_ativo:  # Se a interface está ativa
                            porta.input_ativo = False  # Fecha a interface
                            porta.codigo_digitado = ""  # Limpa o código digitado
                        else:  # Se a interface está fechada
                            porta.input_ativo = True  # Abre a interface
                            porta.mensagem_erro = ""  # Limpa mensagens de erro
                    else:
                        # Se não estiver perto da porta, tenta interagir com outros objetos
                        for obj in [arma1, arma2, arma3, arma4, computador_interativo, granada]:
                            obj.tentar_interagir()
            
            # Controles do jogador (só se nenhuma pista estiver aberta e porta não estiver ativa)
            if not pista_aberta and event.type == pygame.KEYDOWN:
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

            if not pista_aberta and event.type == pygame.KEYUP:
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
                    
                    keys_down.pop(event.key)

        # Verifica colisões com a mesa, computador, granada e paredes
        colide_mesa = pygame.Rect.colliderect(Mesa_colisao, gab_topa_eu.rect)
        colide_computador = pygame.Rect.colliderect(Computador_colisao, gab_topa_eu.rect)
        colide_parede = (
            pygame.Rect.colliderect(parede_esquerda, gab_topa_eu.rect) or 
            pygame.Rect.colliderect(parede_direita, gab_topa_eu.rect) or
            pygame.Rect.colliderect(parede_lateral_esquerda, gab_topa_eu.rect) or
            pygame.Rect.colliderect(parede_lateral_direita, gab_topa_eu.rect)
        )
        colide_caixa = pygame.Rect.colliderect(caixa_colisao, gab_topa_eu.rect)
        
        # Verifica colisão antes de atualizar a posição
        if colide_mesa or colide_computador or colide_parede or colide_caixa:
            # Restaura a posição anterior
            gab_topa_eu.rect.x -= gab_topa_eu.speedx
            gab_topa_eu.rect.y -= gab_topa_eu.speedy
            # Zera todas as velocidades e limpa as teclas
            gab_topa_eu.speedy = gab_topa_eu.speedx = 0
            keys_down.clear()

        # Atualiza posição de todos os sprites, exceto o jogador
        for sprite in all_sprites:
            if sprite != gab_topa_eu:  # Não atualiza o jogador aqui
                sprite.update()

        # Só atualiza o jogador se não houver pista aberta e não houver colisão
        if not pista_aberta and not (colide_mesa or colide_computador or colide_parede or colide_caixa):
            gab_topa_eu.update()
        else:
            gab_topa_eu.speedx = 0
            gab_topa_eu.speedy = 0
            keys_down.clear()

        # Se pista estiver aberta, restaura a posição antiga do jogador
        if pista_aberta:
            gab_topa_eu.rect.topleft = pos_antiga

        # Atualiza estado dos objetos interativos
        for obj in all_interactables:
            obj.update(gab_topa_eu)

        # Atualiza a posição da câmera para seguir o jogador
        camera_x = LARGURA//2 - gab_topa_eu.rect.centerx
        camera_y = ALTURA//2 - gab_topa_eu.rect.centery

        # Limita a câmera para não mostrar fora do cenário
        max_camera_x = 0
        max_camera_y = 0
        min_camera_x = LARGURA - background.get_width()
        min_camera_y = ALTURA - background.get_height()
        camera_x = min(max_camera_x, max(min_camera_x, camera_x))
        camera_y = min(max_camera_y, max(min_camera_y, camera_y))

        # Desenha
        screen.fill(PRETO)
        # Desenha o background com offset da câmera
        screen.blit(background, (background_rect.x + camera_x, background_rect.y + camera_y))
        
        # Desenha o quadro com offset da câmera
        screen.blit(Quadro_img, (Quadro_rect.x + camera_x, Quadro_rect.y + camera_y))
        
        # Desenha o computador com offset da câmera
        screen.blit(Computador, (Computador_rect.x + camera_x, Computador_rect.y + camera_y))
        
        # Desenha a mesa com offset da câmera
        screen.blit(Mesa_Arma, (Mesa_Arma_rect.x + camera_x, Mesa_Arma_rect.y + camera_y))
        
        # Desenha a camera animada com offset da câmera
        screen.blit(Camera_img_anim, (Camera_anim_rect.x + camera_x, Camera_anim_rect.y + camera_y))

        # Desenha os objetos interativos
        for obj in all_interactables:
            obj.desenhar(screen)

        # Desenha o jogador
        screen.blit(gab_topa_eu.image, (gab_topa_eu.rect.x + camera_x, gab_topa_eu.rect.y + camera_y))

        # Desenha as pistas dos objetos interativos
        for obj in all_interactables:
            obj.desenhar_pista(screen)

        # Desenha o timer
        tempo_restante = atualizar_timer()
        if tempo_restante <= 0:
            state = MORTO
        desenhar_timer(screen)

        pygame.display.flip()

        # Verifica se o jogador pode passar pela porta
        if pygame.Rect.colliderect(porta.rect, gab_topa_eu.rect):
            if porta.is_unlocked:
                # Transição para a sala do vencedor
                state = VENCEDOR
                parar_timer()  # Para o timer quando o jogador vence

    return state 