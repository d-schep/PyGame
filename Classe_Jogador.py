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
        self.image = self.assets[FRENTE1]
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
        
        # Variáveis de animação
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_delay = 100  # Delay entre frames da animação
        self.is_moving = False
        self.direction = 'down'  # Direção inicial
        self.last_direction = 'down'  # Última direção para manter consistência
        
    def update(self):
        # Atualiza a posição do jogador
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Verifica se está se movendo
        self.is_moving = self.speedx != 0 or self.speedy != 0
        
        # Atualiza o timer de animação
        current_time = pygame.time.get_ticks()
        if self.is_moving and current_time - self.animation_timer > self.animation_delay:
            self.animation_timer = current_time
            self.animation_frame = (self.animation_frame + 1) % 3  # Ciclo entre 0, 1 e 2
        
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
        if self.speedy < 0:  # Movendo para cima
            self.direction = 'up'
            self.last_direction = 'up'
            if self.is_moving:
                if self.animation_frame == 0:
                    self.image = self.assets[TRAS1]
                elif self.animation_frame == 1:
                    self.image = self.assets[TRAS2]
                else:
                    self.image = self.assets[TRAS3]
            else:
                self.image = self.assets[TRAS1]  # Frame parado
        elif self.speedy > 0:  # Movendo para baixo
            self.direction = 'down'
            self.last_direction = 'down'
            if self.is_moving:
                if self.animation_frame == 0:
                    self.image = self.assets[FRENTE1]
                elif self.animation_frame == 1:
                    self.image = self.assets[FRENTE2]
                else:
                    self.image = self.assets[FRENTE3]
            else:
                self.image = self.assets[FRENTE1]  # Frame parado
        elif self.speedx < 0:  # Movendo para esquerda
            self.direction = 'left'
            self.last_direction = 'left'
            if self.is_moving:
                if self.animation_frame == 0:
                    self.image = self.assets[ESQUERD1]
                elif self.animation_frame == 1:
                    self.image = self.assets[ESQUERD2]
                else:
                    self.image = self.assets[ESQUERD3]
            else:
                self.image = self.assets[ESQUERD1]  # Frame parado
        elif self.speedx > 0:  # Movendo para direita
            self.direction = 'right'
            self.last_direction = 'right'
            if self.is_moving:
                if self.animation_frame == 0:
                    self.image = self.assets[DIREITA1]
                elif self.animation_frame == 1:
                    self.image = self.assets[DIREITA2]
                else:
                    self.image = self.assets[DIREITA3]
            else:
                self.image = self.assets[DIREITA1]  # Frame parado
        else:
            # Quando parado, mantém a última direção
            if self.last_direction == 'up':
                self.image = self.assets[TRAS1]
            elif self.last_direction == 'down':
                self.image = self.assets[FRENTE1]
            elif self.last_direction == 'left':
                self.image = self.assets[ESQUERD1]
            elif self.last_direction == 'right':
                self.image = self.assets[DIREITA1]
            
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
        
        