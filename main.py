# -*- coding: utf-8 -*-
'''
@File   : main.py
@Time   : 2017/5/27 17:47
@Author : yxz23
'''
import sys

import pygame
from pygame.sprite import Group

import settings
from ship import Ship
from alien import Alien
from game_status import GameStatus
from button import Button
import game_functions as gf


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('外星飞船大战')
    pygame.mouse.set_visible(True)

    play_button = Button(screen, 'Play')

    my_ship = Ship(screen)

    status = GameStatus()

    aliens = Group()
    gf.create_fleet(screen, my_ship, aliens)

    while 1:
        gf.deal_events(my_ship, screen, aliens, status, play_button)
        if status.game_active:
            gf.update_bullets(screen, my_ship, aliens)
            my_ship.update()
            gf.update_aliens(screen, my_ship, aliens, status)
        gf.update_screen(screen, my_ship, aliens, status, play_button)

if __name__ == '__main__':
    run_game()