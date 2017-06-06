# -*- coding: utf-8 -*-
'''
@File   : scoreboard.py
@Time   : 2017/6/06 21:17
@Author : yxz23
'''

import pygame.font

import settings


class ScoreBoard(object):
    def __init__(self, screen, status):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.status = status

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        rounded_score = int(round(self.status.score, -1))
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)


