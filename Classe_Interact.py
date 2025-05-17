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
            # Cria uma superfície semi-transparente para o fundo da pista
            fundo = pygame.Surface((LARGURA - 100, ALTURA//2))
            fundo.fill(PRETO)
            fundo.set_alpha(230)
            
            # Posiciona o fundo no centro da tela
            fundo_rect = fundo.get_rect(center=(LARGURA//2, ALTURA//2))
            screen.blit(fundo, fundo_rect)
            
            # Renderiza o texto da pista
            fonte = pygame.font.Font(None, 32)
            linhas = self.pista.split('\n')
            y = fundo_rect.top + 20  # Começa 20 pixels abaixo do topo do fundo
            
            for linha in linhas:
                if linha.strip() != '':  # Ignora linhas vazias
                    texto = fonte.render(linha, True, BRANCO)
                    texto_rect = texto.get_rect(centerx=LARGURA//2, top=y)
                    screen.blit(texto, texto_rect)
                y += 30  # Espaçamento entre linhas
            
            # Adiciona instrução para fechar
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
            margem_x = 100  # Margem horizontal para cada página
            margem_y = 120   # Aumentei a margem superior de 50 para 120
            largura_pagina = (livro_rect.width - 3 * margem_x) // 2  # Largura disponível para texto em cada página
            altura_pagina = livro_rect.height - 2 * margem_y         # Altura disponível para texto
            
            # Configuração da fonte
            tamanho_fonte = 24
            fonte = pygame.font.Font(None, tamanho_fonte)
            espacamento = tamanho_fonte + 5  # Espaçamento entre linhas
            
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
                    if y + espacamento > livro_rect.bottom - margem_y//2:  # Ajustei a margem inferior
                        break
                    texto = fonte.render(linha, True, (0, 0, 0))
                    pos_x = livro_rect.left + margem_x
                    screen.blit(texto, (pos_x, y))
                    y += espacamento
            
            # Renderiza o texto na página direita
            if len(partes) > 1:
                y = livro_rect.top + margem_y
                linhas = quebrar_texto(partes[1], largura_pagina)
                
                for linha in linhas:
                    if y + espacamento > livro_rect.bottom - margem_y//2:  # Ajustei a margem inferior
                        break
                    texto = fonte.render(linha, True, (0, 0, 0))
                    pos_x = livro_rect.centerx + margem_x//2
                    screen.blit(texto, (pos_x, y))
                    y += espacamento

            # Adiciona botão de fechar
            fonte_botao = pygame.font.Font(None, 36)
            texto_fechar = fonte_botao.render("Pressione E para fechar", True, BRANCO)
            texto_fechar_rect = texto_fechar.get_rect(center=(LARGURA/2, livro_rect.bottom + 20))
            screen.blit(texto_fechar, texto_fechar_rect) 