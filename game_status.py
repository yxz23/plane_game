# -*- coding: utf-8 -*-
'''
@File   : game_status.py
@Time   : 2017/6/1 10:49
@Author : yxz23
'''

import settings


class GameStatus(object):
    def __init__(self):
        self.reset_status()
        self.game_active = False

    def reset_status(self):
        self.ships_left = settings.ship_limit
        self.score = 0

