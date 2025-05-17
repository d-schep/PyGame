import pygame
from cfg import *
from assets import *

class ObjetoInterativo(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, pista, tipo='normal', assets=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 0))  # Amarelo para visualizar a área
        self.image.set_alpha(50)  # Semi-transparente
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
        self.indicador.set_alpha(100)
        self.indicador_rect = self.indicador.get_rect()
        self.tipo = tipo
        self.assets = assets

    def update(self, jogador):
        # Verifica se o jogador está perto
        dist_x = abs(self.rect.centerx - jogador.rect.centerx)
        dist_y = abs(self.rect.centery - jogador.rect.centery)
        
        # Define uma distância máxima para interação
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
        # Sempre desenha a área interativa em amarelo transparente
        screen.blit(self.image, self.rect)
        
        # Se o jogador estiver perto, desenha o indicador verde
        if self.pode_interagir:
            self.indicador_rect.center = self.rect.center
            screen.blit(self.indicador, (self.rect.x - 10, self.rect.y - 10))
            
            # Desenha texto "Pressione E" acima do objeto
            fonte = pygame.font.Font(None, 24)
            texto = fonte.render("Pressione E", True, (255, 255, 255))
            texto_rect = texto.get_rect(centerx=self.rect.centerx, bottom=self.rect.top - 5)
            screen.blit(texto, texto_rect)

    def desenhar_pista(self, screen):
        if self.mostrando_pista:
            if self.tipo == 'livro':
                self.desenhar_livro(screen)
            else:
                self.desenhar_pista_normal(screen)

    def desenhar_pista_normal(self, screen):
        if self.mostrando_pista:
            if "620" in str(self.rect.topleft):  # Identifica se é a mesa
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
            
            elif "920" in str(self.rect.topleft) and self.assets and MONITOR in self.assets:  # Se for a estante (monitor)
                fundo_img = self.assets[MONITOR]
                fundo_rect = fundo_img.get_rect(center=(LARGURA//2, ALTURA//2))
                screen.blit(fundo_img, fundo_rect)
                
                fonte = pygame.font.Font(None, 32)
                cor_texto = (0, 255, 0)  # Verde fosforescente para o monitor
                y_inicial = fundo_rect.top + 60  # Reduzido de 100 para 60
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
                        # Alinha o texto à esquerda, mas dentro da largura máxima
                        texto_rect = texto.get_rect()
                        texto_rect.left = margem_esquerda
                        texto_rect.top = y
                        screen.blit(texto, texto_rect)
                    y += espacamento
                
                fonte_instrucao = pygame.font.Font(None, 24)
                instrucao = fonte_instrucao.render("[ Pressione E para fechar ]", True, (0, 255, 0))
                instrucao_rect = instrucao.get_rect(centerx=LARGURA//2, bottom=fundo_rect.bottom + 30)
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
            margem_x = 120  # Aumentei a margem esquerda
            margem_y = 120
            largura_pagina = (livro_rect.width - 3 * margem_x) // 2
            altura_pagina = livro_rect.height - 2 * margem_y
            
            # Configuração da fonte
            tamanho_fonte = 24
            fonte = pygame.font.Font(None, tamanho_fonte)
            espacamento = tamanho_fonte + 5
            
            # Divide o texto em duas partes (esquerda e direita)
            partes = self.pista.split('\n\n\n')
            
            # Função auxiliar para quebrar texto em linhas
            def quebrar_texto(texto, largura_max):
                palavras = texto.split()
                linhas = []
                linha_atual = []
                
                for palavra in palavras:
                    linha_teste = ' '.join(linha_atual + [palavra])
                    if fonte.size(linha_teste)[0] <= largura_max:
                        linha_atual.append(palavra)
                    else:
                        if linha_atual:
                            linhas.append(' '.join(linha_atual))
                            linha_atual = [palavra]
                        else:
                            linhas.append(palavra)
                            linha_atual = []
                
                if linha_atual:
                    linhas.append(' '.join(linha_atual))
                return linhas
            
            # Renderiza o texto na página esquerda
            if len(partes) > 0:
                y = livro_rect.top + margem_y
                linhas = quebrar_texto(partes[0], largura_pagina)
                
                for linha in linhas:
                    if y + espacamento > livro_rect.bottom - margem_y//2:
                        break
                    texto = fonte.render(linha, True, (0, 0, 0))
                    pos_x = livro_rect.left + margem_x + 30  # Adicionei 30 pixels à posição x
                    screen.blit(texto, (pos_x, y))
                    y += espacamento
            
            # Renderiza o texto na página direita
            if len(partes) > 1:
                y = livro_rect.top + margem_y
                linhas = quebrar_texto(partes[1], largura_pagina)
                
                for linha in linhas:
                    if y + espacamento > livro_rect.bottom - margem_y//2:
                        break
                    texto = fonte.render(linha, True, (0, 0, 0))
                    pos_x = livro_rect.centerx + margem_x//2 + 30  # Adicionei 30 pixels à posição x
                    screen.blit(texto, (pos_x, y))
                    y += espacamento

            # Adiciona botão de fechar
            fonte_botao = pygame.font.Font(None, 36)
            texto_fechar = fonte_botao.render("Pressione E para fechar", True, BRANCO)
            texto_fechar_rect = texto_fechar.get_rect(center=(LARGURA/2, livro_rect.bottom + 20))
            screen.blit(texto_fechar, texto_fechar_rect) 