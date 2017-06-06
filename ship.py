# -*- coding: utf-8 -*-
'''
@File   : ship.py
@Time   : 2017/5/31 11:00
@Author : yxz23
'''

import pygame

import settings

class Ship(object):
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.speed = settings.speed # 飞船速度

        '''飞船移动方向flag'''
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_left:
            if self.rect.centerx > self.rect.size[0] / 2.0:
                self.rect.centerx -= self.speed
        elif self.move_right:
            if self.rect.centerx < settings.screen_width - self.rect.size[0] / 2.0:
                self.rect.centerx += self.speed
        elif self.move_up:
            if self.rect.centery > self.rect.size[1] / 2.0:
                self.rect.centery -= self.speed
        elif self.move_down:
            if self.rect.centery < settings.screen_height - self.rect.size[1] / 2.0:
                self.rect.centery += self.speed

