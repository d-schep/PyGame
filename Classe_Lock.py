import pygame
from cfg import *
from assets import *

class Lock(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, correct_code, assets=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((100, 100, 100))  # Cor cinza para a fechadura
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.correct_code = correct_code
        self.current_code = ""
        self.is_active = False
        self.pode_interagir = False
        self.assets = assets
        self.last_key_time = 0
        self.key_delay = 200  # Atraso entre pressionamentos de tecla em milissegundos
        self.is_unlocked = False
        
    def update(self, jogador):
        # Verifica se o jogador está perto
        dist_x = abs(self.rect.centerx - jogador.rect.centerx)
        dist_y = abs(self.rect.centery - jogador.rect.centery)
        
        # Define uma distância máxima menor para interação
        self.pode_interagir = dist_x < 50 and dist_y < 50  # Reduzido de 100 para 50

    def tentar_interagir(self):
        if self.pode_interagir and not self.is_unlocked:
            self.is_active = not self.is_active
            if not self.is_active:
                self.current_code = ""
            return True
        return False

    def handle_keypress(self, event):
        if not self.is_active or self.is_unlocked:
            return

        current_time = pygame.time.get_ticks()
        if current_time - self.last_key_time < self.key_delay:
            return

        if event.type == pygame.KEYDOWN:
            if event.key >= pygame.K_0 and event.key <= pygame.K_9:
                if len(self.current_code) < 4:  # Limita o código a 4 dígitos
                    self.current_code += str(event.key - pygame.K_0)
                    self.last_key_time = current_time
            elif event.key == pygame.K_BACKSPACE:
                self.current_code = self.current_code[:-1]
                self.last_key_time = current_time
            elif event.key == pygame.K_RETURN:
                self.check_code()
                self.last_key_time = current_time

    def check_code(self):
        if self.current_code == self.correct_code:
            self.is_unlocked = True
            self.is_active = False
        else:
            self.current_code = ""

    def desenhar(self, screen):
        # Desenha o retângulo base da fechadura
        screen.blit(self.image, self.rect)
        
        # Se o jogador estiver perto e a fechadura não estiver desbloqueada
        if self.pode_interagir and not self.is_unlocked:
            # Desenha texto "Pressione E" acima do objeto
            fonte = pygame.font.Font(None, 24)
            texto = fonte.render("Pressione E para interagir", True, (255, 255, 255))
            texto_rect = texto.get_rect(centerx=self.rect.centerx, bottom=self.rect.top - 5)
            screen.blit(texto, texto_rect)

        # Se o painel estiver ativo, desenha a interface do código
        if self.is_active:
            # Desenha o fundo do painel
            panel_width = 300
            panel_height = 150
            panel_x = LARGURA // 2 - panel_width // 2
            panel_y = ALTURA // 2 - panel_height // 2
            
            panel = pygame.Surface((panel_width, panel_height))
            panel.fill((50, 50, 50))  # Cor de fundo do painel
            
            # Desenha o display do código
            fonte = pygame.font.Font(None, 48)
            code_display = "*" * len(self.current_code)
            texto_codigo = fonte.render(code_display, True, (0, 255, 0))
            texto_rect = texto_codigo.get_rect(center=(panel_width//2, panel_height//3))
            panel.blit(texto_codigo, texto_rect)
            
            # Desenha as instruções
            fonte_instrucoes = pygame.font.Font(None, 24)
            instrucoes = fonte.render("Digite o código (4 dígitos) e pressione Enter", True, (255, 255, 255))
            instrucoes_rect = instrucoes.get_rect(center=(panel_width//2, panel_height*2//3))
            panel.blit(instrucoes, instrucoes_rect)
            
            # Desenha o painel na tela
            screen.blit(panel, (panel_x, panel_y)) 