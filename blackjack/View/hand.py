import pygame

from Control import config


def show_players_hand(control):
    """TODO: Add method description"""

    k = 1
    players_hand = control.get_players_hand()
    for i in range(len(players_hand)):
        right = 350
        down = 400
        card = pygame.image.load(str(players_hand[i].get_filename()))
        config.game_display.blit(card, (right + k, down))
        k += 27


def show_dealers_hand(control):
    """TODO: Add method description"""
    k = 1
    dealers_hand = control.get_dealers_hand()
    for i in range(len(dealers_hand)):
        right = 350
        down = 50
        card = pygame.image.load(str(dealers_hand[i].get_filename()))
        config.game_display.blit(card, (right + k, down))
        k += 27
