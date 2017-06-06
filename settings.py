# -*- coding: utf-8 -*-
'''
@File   : settings.py
@Time   : 2017/5/31 10:54
@Author : yxz23

存储游戏相关设置项

'''

'''游戏窗口大小'''
screen_width = 800
screen_height = 600

'''游戏背景色'''
bg_color = (230, 230, 230)

'''飞船参数'''
speed = 1.0
ship_limit = 3

'''子弹参数'''
bullet_speed = 2.0
bullet_width = 3
bullet_height = 15
bullet_color = (60, 60, 60)
bullets_allowed = 10
bomb_allowed = 3  # 炸弹数
bullet_frequence = 35

'''外星飞船参数'''
alien_speed = 0.5
fleet_drop_speed = 10
fleet_direction = 1

speedup_scale = 1.1


def init_dynamic_settings():
    global speed, bullet_speed, alien_speed, fleet_direction
    speed = 1.0
    bullet_speed = 2.0
    alien_speed = 1

    fleet_direction = 1


def increase_speed():
    global speed, bullet_speed, alien_speed
    speed *= speedup_scale
    bullet_speed *= speedup_scale
    alien_speed *= speedup_scale

