# -*- coding: utf-8 -*-
'''
@File   : game_functions.py
@Time   : 2017/5/31 11:18
@Author : yxz23
'''
import sys
from time import sleep
import pygame

import settings
from bullet import Bullet, Big_Bullet
from alien import Alien


def fire_bullet(screen, ship, bullets, big_bullets, is_commom = True):
    '''发射子弹'''
    if len(bullets) < settings.bullets_allowed and is_commom:
        new_bullet = Bullet(screen, ship)
        bullets.add(new_bullet)
    elif not is_commom:
        new_bullet = Big_Bullet(screen, ship)
        big_bullets.add(new_bullet)


def get_number_aliens_x(alien_width):
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ship_height, alien_height):
    available_space_y = settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(screen, aliens, alien_number, row_number):
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(screen, ship, aliens):
    alien = Alien(screen)
    number_aliens_x = get_number_aliens_x(alien.rect.width)
    number_rows = get_number_rows(ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(screen, aliens, alien_number, row_number)


def check_key_down_events(event, screen, ship, bullets, big_bullets):
    if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(screen, ship, bullets, big_bullets)
    elif event.key == pygame.K_b:
        fire_bullet(screen, ship, big_bullets, big_bullets, is_commom=False)


def check_key_up_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False


def deal_events(ship, screen, aliens, bullets, big_bullets, status, play_button):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, screen, ship, bullets, big_bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, ship, aliens, bullets, big_bullets, status, play_button, mouse_x, mouse_y)


def update_screen(screen, ship, aliens, bullets, big_bullets, status, play_button):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in big_bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not status.game_active:
        play_button.draw_button()
    pygame.display.flip()


def check_bullets_collisions(screen, ship, bullets, big_bullets, aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    big_collision = pygame.sprite.groupcollide(big_bullets, aliens, False, True)

    if len(aliens) == 0:
        bullets.empty()
        big_bullets.empty()
        create_fleet(screen, ship, aliens)

def update_bullets(screen, ship, bullets, big_bullets, aliens):
    bullets.update()
    big_bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for bullet in big_bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullets_collisions(screen, ship, bullets, big_bullets, aliens)


def change_fleet_direction(aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def check_fleet_edges(aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens)
            break


def check_aliens_bottom(screen, ship, aliens, bullets, big_bullets, status):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(screen, ship, aliens, bullets, big_bullets, status)
            break


def ship_hit(screen, ship, aliens, bullets, big_bullets, status):
    aliens.empty()
    bullets.empty()
    big_bullets.empty()

    create_fleet(screen, ship, aliens)
    ship.center_ship()

    if status.ships_left > 0:
        status.ships_left -= 1
        sleep(0.5)
    else:
        status.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(screen, ship, aliens, bullets, big_bullets, status):
    check_fleet_edges(aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(screen, ship, aliens, bullets, big_bullets, status)

    check_aliens_bottom(screen, ship, aliens, bullets, big_bullets, status)


def check_play_button(screen, ship, aliens, bullets, big_bullets, status, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not status.game_active:
        pygame.mouse.set_visible(False)
        status.game_active = True
        status.reset_status()

        aliens.empty()
        bullets.empty()
        big_bullets.empty()

        create_fleet(screen, ship, aliens)
        ship.center_ship()
