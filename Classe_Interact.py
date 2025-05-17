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
        # Cria uma superfície semi-transparente para o fundo da pista
        fundo = pygame.Surface((LARGURA, 100))
        fundo.fill(PRETO)
        fundo.set_alpha(200)
        screen.blit(fundo, (0, ALTURA - 100))
        
        # Renderiza o texto da pista
        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(self.pista, True, BRANCO)
        texto_rect = texto.get_rect(center=(LARGURA/2, ALTURA - 50))
        screen.blit(texto, texto_rect)

    def desenhar_livro(self, screen):
        if self.assets and LIVRO in self.assets:
            # Usa a imagem do LIVRO
            livro_img = self.assets[LIVRO]
            livro_rect = livro_img.get_rect(center=(LARGURA/2, ALTURA/2))
            screen.blit(livro_img, livro_rect)
            
            # Adiciona o texto nas páginas
            fonte = pygame.font.Font(None, 32)
            linhas = self.pista.split('\n\n\n')  # Separa as duas frases

            # Adiciona botão de fechar
            fonte_botao = pygame.font.Font(None, 36)
            texto_fechar = fonte_botao.render("Pressione E para fechar", True, BRANCO)
            texto_fechar_rect = texto_fechar.get_rect(center=(LARGURA/2, livro_rect.bottom + 20))
            screen.blit(texto_fechar, texto_fechar_rect) 