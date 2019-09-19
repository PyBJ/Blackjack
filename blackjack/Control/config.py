import platform
import os
import pygame

# import re
#  File Configurations including Globals

# game control/testing
new_game: bool = False
game_exit: bool = False
menu: bool = False
end_shoe: bool = False
end_shoe_warn: bool = False
crashed: bool = False
blackjack: bool = False
# colors
board_color = (28, 74, 50)
black = (0, 0, 0)
white = (255, 255, 255)
rose_white = (235, 131, 131)
red = (255, 0, 0)
dark_red = (134, 28, 28)
deep_red = (30, 3, 3)
green = (0, 255, 0)
dark_green = (0, 200, 0)
blue = (0, 0, 255)
dark_blue = (0, 0, 200)
light_gray = (159, 180, 194)
gold = (201, 173, 24)
light_gold = (237, 214, 97)

# display dimensions
display_width = 900
display_height = 600

# pygame constructors
pygame.init()
small_text = pygame.font.Font("freesansbold.ttf", 20)
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("BlackJack")
clock = pygame.time.Clock()

if platform.system() == "Windows":
    path = os.getcwd() + r"\Control\images\background_images"
    game_menu = pygame.image.load(path + "\possible_menu.png")
    table_background = pygame.image.load(path + "\possible_game_2.png")

else:
    path = os.getcwd() + "/Control/images/background_images"
    game_menu = pygame.image.load(path + "/possible_menu.png")
    table_background = pygame.image.load(path + "/possible_game_2.png")


class UtilityFunctions:

    def quit_game(self):
        """call the pygame quit() method"""
        game_exit = True
        pygame.quit()
        quit()