import pygame
import random
from cfg import *
from assets import * 
from math import * 
import os 
import time 

class Texto(pygame.sprite.Sprite):
    def __init__(self,texto,x,y,larg,alt,cor,assets):
        self.text = texto
        self.cor = cor
        self.font =assets[FONTE_BOTAO]
        self.rect = pygame.Rect(x,y,larg,alt)
    def desenhar(self,surface):

        texto_render = self.font.render(self.text, True, self.cor)
        texto_rect = texto_render.get_rect(center=self.rect.center)
        surface.blit(texto_render, texto_rect)
