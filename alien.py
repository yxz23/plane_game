# -*- coding: utf-8 -*-
'''
@File   : alien.py
@Time   : 2017/5/31 16:09
@Author : yxz23
'''

import pygame
from pygame.sprite import Sprite

import settings

class Alien(Sprite):
    def __init__(self, screen):
        super(Alien, self).__init__()

        self.screen = screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False

    def update(self):
        self.x += settings.alien_speed * settings.fleet_direction
        self.rect.x = self.x

