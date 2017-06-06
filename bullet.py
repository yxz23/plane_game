# -*- coding: utf-8 -*-
'''
@File   : bullet.py
@Time   : 2017/5/31 15:22
@Author : yxz23
'''

import pygame
from pygame.sprite import Sprite

import settings

class Bullet(Sprite):
    def __init__(self, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.ship = ship

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top

        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bomb(Bullet):
    def __init__(self, screen, ship):
        super(Bomb, self).__init__(screen, ship)
        self.rect = pygame.Rect(0, 0, 100*settings.bullet_width, settings.bullet_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top

