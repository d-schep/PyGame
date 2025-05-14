import pygame
import random
from cfg import *
from assets import * 
from math import * 
import os 
import time 


class Jogador(pygame.sprite.Sprite):
    def __init__(self,assets):
        self.assets = assets
        pygame.sprite.Sprite.__init__(self)
        self.image = self.assets[PERSONAGEM]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA/2
        self.rect.centery = ALTURA/2
        self.speedx = 0
        self.speedy = 0
        #self.group = group  
        self.ultimo_interact = pygame.time.get_ticks()
        self.tick_de_interação = 300
    def update(self):

        # == POSIÇÃO == 
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # == HARD LIMITS == 
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTURA:
            self.rect.bottom = ALTURA
        # == TROCA IMAGEM == 
        if self.speedy < 0:
            print('cima', self.image)
            self.image = self.assets[GAB_TRAS]  
           # self.image = pygame.Surface((96, 164))
            #self.image.fill(VERDE)
        elif self.speedy > 0:
            print('baixo', self.image)
            self.image = self.assets[PERSONAGEM]
          #  self.image = pygame.Surface((96, 164))
          #  self.image.fill(VERMELHO)
        elif self.speedx < 0:
            print('esquerda')
            self.image = self.assets[ESQUERDA]
        elif self.speedx > 0:
            print('esquerda')
            self.image = self.assets[DIREITA]
            
    def interact(self):
        # == limite de interação por tick == 
        t0 = pygame.time.get_ticks()
        delta_t = t0 - self.ultimo_interact
        if delta_t > self.tick_de_interação:
            self.ultimo_interact = t0
        
        