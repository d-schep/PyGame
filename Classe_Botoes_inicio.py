import pygame
import random
from cfg import *
from assets import * 
from math import * 
import os 
import time 

class Botao(pygame.sprite.Sprite):
    def __init__(self,x,y,largura,altura,texto, cor, cor_hover,assets, funcao=None):
        pygame.sprite.Sprite.__init__(self)
        self.centerx = largura/2
        self.centery = altura/2
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor = cor
        self.cor_hover = cor_hover
        self.funcao = funcao  
        self.fonte = assets[FONTE_BOTAO]
        self.alpha = 255

    def alpha(self,val):
        self.alpha = min(255, max(0, val))

    def desenhar(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        cor_atual = self.cor_hover if self.rect.collidepoint(mouse_pos) else self.cor

        # Criando superfície do botão com transparência
        superficie = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        cor_atual = (*cor_atual[:3], self.alpha)  # Adiciona transparência ao botão
        pygame.draw.rect(superficie, cor_atual, (0, 0, self.rect.width, self.rect.height), border_radius=5)

        # Renderizando texto com transparência
        texto_render = self.fonte.render(self.texto, True, (255, 255, 255))
        texto_surface = pygame.Surface(texto_render.get_size(), pygame.SRCALPHA)
        texto_surface.set_alpha(self.alpha)
        texto_surface.blit(texto_render, (0, 0))

        texto_rect = texto_render.get_rect(center=self.rect.center)
        superficie.blit(texto_surface, (texto_rect.x - self.rect.x, texto_rect.y - self.rect.y))

        surface.blit(superficie, self.rect.topleft)  # Desenha na tela

    def checar_click(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                if self.funcao:
                    self.funcao()

