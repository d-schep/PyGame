import pygame
from cfg import *
from assets import *

class ObjetoInterativo(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, pista, tipo='normal', assets=None, show_indicator=True):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 0))  # Amarelo para visualizar a área
        self.image.set_alpha(0)  # Totalmente transparente
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pista = pista
        self.pode_interagir = False
        self.mostrando_pista = False
        self.ultimo_interact = 0
        self.delay_interacao = 500
        self.indicador = pygame.Surface((width + 20, height + 20))
        self.indicador.fill((0, 255, 0))  # Verde para o indicador
        self.indicador.set_alpha(0)  # Indicador também totalmente transparente
        self.indicador_rect = self.indicador.get_rect()
        self.tipo = tipo
        self.assets = assets
        self.show_indicator = show_indicator

    def update(self, jogador):
        # Verifica se o jogador está perto
        dist_x = abs(self.rect.centerx - jogador.rect.centerx)
        dist_y = abs(self.rect.centery - jogador.rect.centery)
        
        # Define uma distância máxima para interação
        if self.tipo == 'barril':
            # Distância menor para o barril
            self.pode_interagir = dist_x < 50 and dist_y < 50
        else:
            # Mantém a distância normal para outros objetos
            self.pode_interagir = dist_x < 100 and dist_y < 100

    def tentar_interagir(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultimo_interact >= self.delay_interacao:
            self.ultimo_interact = agora
            if self.pode_interagir:
                self.mostrando_pista = not self.mostrando_pista
                return True
        return False

    def desenhar(self, screen):
        # Sempre desenha a área interativa (agora invisível)
        screen.blit(self.image, self.rect)

        # Se for granada, desenha a imagem da granada centralizada e aumentada 1,5x
        if self.tipo == 'granada' and self.assets and 'granada' in self.assets:
            img = self.assets['granada']
            w, h = img.get_width(), img.get_height()
            img_big = pygame.transform.scale(img, (int(w * 1.5), int(h * 1.5)))
            img_rect = img_big.get_rect(center=self.rect.center)
            screen.blit(img_big, img_rect)

        # Se o jogador estiver perto e show_indicator for True, desenha o indicador verde
        if self.pode_interagir and self.show_indicator:
            self.indicador_rect.center = self.rect.center
            screen.blit(self.indicador, (self.rect.x - 10, self.rect.y - 10))
            
            # Desenha texto "Pressione E" acima do objeto
            fonte = pygame.font.Font(None, 24)
            texto = fonte.render("Pressione E", True, (255, 255, 255))
            
            # Ajusta a posição do texto baseado no tipo e posição do objeto
            if self.tipo == 'arma' and self.rect.y < ALTURA//2:  # Se for uma arma na parte superior
                texto_rect = texto.get_rect(centerx=self.rect.centerx, bottom=self.rect.top + 35)  # 35 pixels abaixo
            else:
                texto_rect = texto.get_rect(centerx=self.rect.centerx, bottom=self.rect.top + 15)  # 15 pixels abaixo para os outros
                
            screen.blit(texto, texto_rect)

    def desenhar_pista(self, screen):
        if self.mostrando_pista:
            if self.tipo == 'livro':
                self.desenhar_livro(screen)
            elif self.tipo == 'papel':
                if self.assets and PAPEL2 in self.assets:
                    # Cria uma superfície para o fundo preto transparente
                    fundo_escuro = pygame.Surface((LARGURA, ALTURA))
                    fundo_escuro.fill((0, 0, 0))
                    fundo_escuro.set_alpha(128)
                    screen.blit(fundo_escuro, (0, 0))
                    
                    # Usa a imagem do PAPEL2
                    papel_img = self.assets[PAPEL2]
                    papel_rect = papel_img.get_rect()
                    
                    # Define a posição do papel (mais para a direita)
                    papel_x = LARGURA - papel_rect.width - 50  # 50 pixels da borda direita
                    papel_y = 50  # 50 pixels do topo
                    screen.blit(papel_img, (papel_x, papel_y))
                    
                    # Configuração da fonte menor
                    fonte = pygame.font.Font(None, 24)
                    espacamento = 30
                    
                    # Renderiza o texto linha por linha
                    linhas = self.pista.split('\n')
                    y = papel_y + 80
                    
                    for linha in linhas:
                        if linha.strip():
                            texto = fonte.render(linha.strip(), True, (0, 0, 0))
                            texto_rect = texto.get_rect()
                            texto_rect.centerx = papel_x + papel_rect.width // 2
                            texto_rect.top = y
                            screen.blit(texto, texto_rect)
                        y += espacamento
                    
                    # Adiciona botão de fechar
                    fonte_botao = pygame.font.Font(None, 28)
                    texto_fechar = fonte_botao.render("Pressione E para fechar", True, BRANCO)
                    texto_fechar_rect = texto_fechar.get_rect()
                    texto_fechar_rect.centerx = papel_x + papel_rect.width // 2
                    texto_fechar_rect.top = papel_y + papel_rect.height + 10
                    screen.blit(texto_fechar, texto_fechar_rect)
            else:
                self.desenhar_pista_normal(screen)

    def desenhar_pista_normal(self, screen):
        if self.mostrando_pista:
            if "620" in str(self.rect.topleft):  # Se for a mesa (agora mostra o monitor)
                if self.assets and MONITOR in self.assets:
                    fundo_img = self.assets[MONITOR]
                    fundo_rect = fundo_img.get_rect(center=(LARGURA//2, ALTURA//2))
                    screen.blit(fundo_img, fundo_rect)
                    
                    fonte = pygame.font.Font(None, 32)
                    cor_texto = (0, 255, 0)  # Verde fosforescente para o monitor
                    y_inicial = fundo_rect.top + 80  # Aumentado de 60 para 80
                    espacamento = 30
                    
                    # Adiciona efeito de terminal
                    tempo = pygame.time.get_ticks() / 1000
                    cursor = "_" if int(tempo * 2) % 2 == 0 else " "
                    
                    # Calcula a largura máxima do texto
                    largura_maxima = 400  # Reduzido para centralizar melhor
                    
                    linhas = self.pista.split('\n')
                    y = y_inicial
                    
                    # Centraliza o texto horizontalmente
                    margem_esquerda = LARGURA//2 - largura_maxima//2
                    
                    for linha in linhas:
                        if linha.strip() != '':
                            texto = fonte.render(linha + (cursor if linha == linhas[-1] else ""), True, cor_texto)
                            texto_rect = texto.get_rect()
                            texto_rect.left = margem_esquerda
                            texto_rect.top = y
                            screen.blit(texto, texto_rect)
                        y += espacamento
                    
                    fonte_instrucao = pygame.font.Font(None, 24)
                    instrucao = fonte_instrucao.render("[ Pressione E para fechar ]", True, (0, 255, 0))
                    instrucao_rect = instrucao.get_rect(centerx=LARGURA//2, bottom=fundo_rect.bottom - 20)
                    screen.blit(instrucao, instrucao_rect)
            elif self.tipo == 'barril' and self.assets and PISTABARRIL in self.assets:
                # Usa a imagem do PISTABARRIL
                pista_img = self.assets[PISTABARRIL]
                pista_rect = pista_img.get_rect(center=(LARGURA/2, ALTURA/2))
                screen.blit(pista_img, pista_rect)
                
                # Configuração da fonte
                fonte = pygame.font.Font(None, 32)
                espacamento = 35
                
                # Renderiza o texto linha por linha
                linhas = self.pista.split('\n')
                y = pista_rect.top + 100  # Começa um pouco mais acima
                
                for linha in linhas:
                    if linha.strip():  # Se a linha não estiver vazia
                        texto = fonte.render(linha.strip(), True, (0, 0, 0))
                        texto_rect = texto.get_rect(centerx=LARGURA/2, top=y)
                        screen.blit(texto, texto_rect)
                    y += espacamento
                
                # Adiciona botão de fechar
                fonte_botao = pygame.font.Font(None, 28)
                texto_fechar = fonte_botao.render("Pressione E para fechar", True, BRANCO)
                texto_fechar_rect = texto_fechar.get_rect(center=(LARGURA/2, pista_rect.bottom + 20))
                screen.blit(texto_fechar, texto_fechar_rect)
            elif "920" in str(self.rect.topleft):  # Se for a estante (agora mostra a prancheta)
                # Criar uma superfície para a prancheta
                prancheta = pygame.Surface((500, 600))
                prancheta.fill((240, 234, 214))  # Cor bege claro para papel
                
                # Adicionar efeito de borda da prancheta
                pygame.draw.rect(prancheta, (139, 69, 19), (0, 0, 500, 600), 20)  # Borda marrom
                
                # Adicionar clip de metal no topo
                pygame.draw.rect(prancheta, (192, 192, 192), (200, 0, 100, 30))  # Clip metálico
                
                # Linhas do papel
                for i in range(40, 600, 25):
                    pygame.draw.line(prancheta, (200, 200, 200), (40, i), (460, i), 1)
                
                # Posicionar a prancheta no centro
                prancheta_rect = prancheta.get_rect(center=(LARGURA//2, ALTURA//2))
                screen.blit(prancheta, prancheta_rect)
                
                # Renderizar o texto
                fonte = pygame.font.Font(None, 32)
                linhas = self.pista.split('\n')
                y = prancheta_rect.top + 60
                
                # Adicionar título sublinhado
                titulo = fonte.render("RELATÓRIO - CONFIDENCIAL", True, (139, 0, 0))  # Vermelho escuro
                titulo_rect = titulo.get_rect(centerx=LARGURA//2, top=y)
                screen.blit(titulo, titulo_rect)
                pygame.draw.line(screen, (139, 0, 0), 
                               (titulo_rect.left, titulo_rect.bottom + 2),
                               (titulo_rect.right, titulo_rect.bottom + 2), 2)
                
                y += 50  # Espaço após o título
                
                # Resto do texto
                for linha in linhas[1:]:  # Pula a primeira linha (título)
                    if linha.strip() != '':
                        texto = fonte.render(linha, True, (0, 0, 120))  # Azul escuro para texto
                        texto_rect = texto.get_rect(centerx=LARGURA//2, top=y)
                        screen.blit(texto, texto_rect)
                    y += 30
                
                # Adicionar carimbo "CONFIDENCIAL" rotacionado
                fonte_carimbo = pygame.font.Font(None, 48)
                carimbo = fonte_carimbo.render("CONFIDENCIAL", True, (255, 0, 0, 128))
                carimbo = pygame.transform.rotate(carimbo, -45)
                screen.blit(carimbo, (prancheta_rect.right - 200, prancheta_rect.top + 150))
                
                # Instrução para fechar
                fonte_instrucao = pygame.font.Font(None, 24)
                instrucao = fonte_instrucao.render("Pressione E para fechar", True, (100, 100, 100))
                instrucao_rect = instrucao.get_rect(centerx=LARGURA//2, bottom=prancheta_rect.bottom + 30)
                screen.blit(instrucao, instrucao_rect)
            else:  # Fallback para qualquer outro caso
                fundo = pygame.Surface((LARGURA - 100, ALTURA//2))
                fundo.fill(PRETO)
                fundo.set_alpha(230)
                fundo_rect = fundo.get_rect(center=(LARGURA//2, ALTURA//2))
                screen.blit(fundo, fundo_rect)
                
                fonte = pygame.font.Font(None, 32)
                linhas = self.pista.split('\n')
                y = fundo_rect.top + 20
                
                for linha in linhas:
                    if linha.strip() != '':
                        texto = fonte.render(linha, True, BRANCO)
                        texto_rect = texto.get_rect(centerx=LARGURA//2, top=y)
                        screen.blit(texto, texto_rect)
                    y += 30
                
                fonte_instrucao = pygame.font.Font(None, 24)
                instrucao = fonte_instrucao.render("Pressione E para fechar", True, (200, 200, 200))
                instrucao_rect = instrucao.get_rect(centerx=LARGURA//2, bottom=fundo_rect.bottom - 10)
                screen.blit(instrucao, instrucao_rect)

    def desenhar_livro(self, screen):
        if self.assets and LIVRO in self.assets:
            # Usa a imagem do LIVRO
            livro_img = self.assets[LIVRO]
            livro_rect = livro_img.get_rect(center=(LARGURA/2, ALTURA/2))
            screen.blit(livro_img, livro_rect)
            
            # Define a área útil para texto em cada página
            margem_x = 120
            margem_y = 100  # Reduzida a margem superior
            largura_pagina = (livro_rect.width - 3 * margem_x) // 2
            altura_pagina = livro_rect.height - 2 * margem_y
            
            # Configuração da fonte menor
            tamanho_fonte = 28  # Reduzido de 36 para 28
            fonte = pygame.font.Font(None, tamanho_fonte)
            espacamento = tamanho_fonte + 8  # Reduzido o espaçamento
            
            # Divide o texto em linhas como fornecido
            linhas = [
                "19 9 1 13 5 4",
                "5 4 18 1 20",
                "1 10 5 19",
                "5 21 17",
                "19 5 20 14 1",
                "5 22 12 1 19",
                "19 15 14",
                "5",
                "5 12 5",
                "5 21 7 5 16",
                "15 1 8 3",
                "15 14",
                "15 4 1 19 19 1 13 1",
                "12 5 16 1 16",
                "15",
                "5 20 1",
                "1 22"
            ]
            
            # Divide as linhas entre as duas páginas
            meio = len(linhas) // 2
            linhas_esquerda = linhas[:meio]
            linhas_direita = linhas[meio:]
            
            # Renderiza as linhas na página esquerda
            y = livro_rect.top + margem_y
            for linha in linhas_esquerda:
                if y + espacamento > livro_rect.bottom - margem_y:
                    break
                texto = fonte.render(linha, True, (0, 0, 0))
                pos_x = livro_rect.left + margem_x
                screen.blit(texto, (pos_x, y))
                y += espacamento
            
            # Renderiza as linhas na página direita
            y = livro_rect.top + margem_y
            for linha in linhas_direita:
                if y + espacamento > livro_rect.bottom - margem_y:
                    break
                texto = fonte.render(linha, True, (0, 0, 0))
                pos_x = livro_rect.centerx + margem_x
                screen.blit(texto, (pos_x, y))
                y += espacamento

            # Adiciona botão de fechar
            fonte_botao = pygame.font.Font(None, 36)
            texto_fechar = fonte_botao.render("Pressione E para fechar", True, BRANCO)
            texto_fechar_rect = texto_fechar.get_rect(center=(LARGURA/2, livro_rect.bottom + 20))
            screen.blit(texto_fechar, texto_fechar_rect) 