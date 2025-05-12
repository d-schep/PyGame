import pygame
import random
from cfg import *
from assets import * 
from math import * 
import os 
import time 

class Botao_inicio(pygame.sprite.Sprite):
    def __init__(self,x,y,largura,altura,texto, cor, cor_hover,assets, funcao=None):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor = cor
        self.cor_hover = cor_hover
        self.funcao = funcao
        self.fonte = assets[FONTE_BOTAO]
    
    def desenhar(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        cor_atual = self.cor_hover if self.rect.collidepoint(mouse_pos) else self.cor

        pygame.draw.rect(surface, cor_atual, self.rect, border_radius=5)

        texto_render = self.fonte.render(self.texto, True, (255, 255, 255))
        texto_rect = texto_render.get_rect(center=self.rect.center)
        surface.blit(texto_render, texto_rect)

    def checar_click(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                if self.funcao:
                    self.funcao()
