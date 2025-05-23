import pygame
import random
from cfg import *
from assets import * 
from math import * 
import os 
import time 
from sons import *


class Jogador(pygame.sprite.Sprite):
    def __init__(self,assets):
        self.assets = assets
        pygame.sprite.Sprite.__init__(self)
        self.image = self.assets[PERSONAGEM]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA/2
        self.rect.bottom = ALTURA - 100
        self.speedx = 0
        self.speedy = 0
        #self.group = group  
        self.ultimo_interact = pygame.time.get_ticks()
        self.tick_de_interação = 300
        self.som_andando_tocando = False
        self.ultimo_som_andando = 0
        self.delay_som_andando = 300  # Reduzido para 300ms para sons mais frequentes
    def update(self):
        # Atualiza a posição do jogador
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # == HARD LIMITS == 
        if self.rect.right > LARGURA-30:
            self.rect.right = LARGURA-30
        if self.rect.left < 30:
            self.rect.left = 30
        if self.rect.top < 115:
            self.rect.top = 115
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
            
        # Gerencia o som de caminhada
        tempo_atual = pygame.time.get_ticks()
        esta_andando = (self.speedx != 0 or self.speedy != 0)
        
        if esta_andando:
            if not self.som_andando_tocando:
                tocar_som(SOM_ANDANDO)
                self.som_andando_tocando = True
                self.ultimo_som_andando = tempo_atual
            elif tempo_atual - self.ultimo_som_andando > self.delay_som_andando:
                tocar_som(SOM_ANDANDO)
                self.ultimo_som_andando = tempo_atual
        elif self.som_andando_tocando:
            parar_som(SOM_ANDANDO)
            self.som_andando_tocando = False
    def interact(self):
        # == limite de interação por tick == 
        t0 = pygame.time.get_ticks()
        delta_t = t0 - self.ultimo_interact
        if delta_t > self.tick_de_interação:
            self.ultimo_interact = t0
        
        