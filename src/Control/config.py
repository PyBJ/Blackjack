import platform
import os
import pygame

# import re
#  File Configurations including Globals

# game control/testing
new_game = False
game_exit = False
menu = False
end_shoe = False
end_shoe_warn = False
crashed = False
blackjack = False
# colors
# board_color = (255, 60, 90)
board_color = (23, 79, 7)
black = (0, 0, 0)
white = (255, 255, 255)
rose_white = (235, 131, 131)
red = (255, 0, 0)
dark_red = (194, 35, 35)
green = (0, 255, 0)
dark_green = (0, 200, 0)
blue = (0, 0, 255)
dark_blue = (0, 0, 200)
light_gray = (159, 180, 194)
gold = (201, 173, 24)
light_gold = (237, 214, 97)

# display dimensions
disp_width = 1200
disp_height = 600

# pygame constructors
pygame.init()
small_text = pygame.font.Font("freesansbold.ttf", 20)
gameDisplay = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption("BlackJackTrainerAlfa")
clock = pygame.time.Clock()


# loads images in test folder
# custom_images: custom cards
# card_images: open source cards
# 2d list with two variables, pygame image and image name
custom_cards = []
# card_images = []

if platform.system() == "Windows":
    # os.chdir(r"C:\Users\Trevor\PythonProjects\Blackjack-Project\src\View")
    path = os.getcwd() + r"\Control\images\custom_cards"
    for image in os.listdir(path):
        custom_cards.append(
            [pygame.image.load(path + "/" + image).convert_alpha(), image.strip(".gif")]
        )
    # path = os.getcwd() + r"\rimages\card_images"
    # for image in os.listdir(path):
    #     card_images.append(
    #         [pygame.image.load(path + "/" + image).convert_alpha(), image.strip(".gif")]
    #     )
else:
    path = os.getcwd() + "/Control/images/custom_cards"
    for image in os.listdir(path):
        custom_cards.append(
            [pygame.image.load(path + "/" + image).convert_alpha(), image.strip(".gif")]
        )
    # path = os.getcwd() + "/images/card_images"
    # for image in os.listdir(path):
    #     card_images.append(
    #         [pygame.image.load(path + "/" + image).convert_alpha(), image.strip(".gif")]
    #     )

# bubble sort to sort card_images card name number value
# for j in range(0, 51):
#     check_swap = False
#     for i in range(0, 51):
#         if int(re.sub('[^0-9]', '', card_images[i][1])) > int(re.sub('[^0-9]', '', card_images[i+1][1])):
#             swap_obj = card_images[i][0]
#             swap_name = card_images[i][1]
#             card_images[i][0] = card_images[i+1][0]
#             card_images[i][1] = card_images[i+1][1]
#             card_images[i+1][0] = swap_obj
#             card_images[i+1][1] = swap_name
#             check_swap = True
#     if check_swap == 0:
#         break
#
# # bubble sort card_images card suit
# # to keep the loop simple, suit order is CLUB, DIAMOND, HEART, SPADE
# for i in range(12):
#     i = i * 4
#     for k in range(4):
#         check_swap = False
#         for j in range(3):
#             if re.sub('[^a-z]', '', card_images[j+i][1]) > re.sub('[^a-z]', '', card_images[j+i+1][1]):
#                 swap_obj = card_images[j+i][0]
#                 swap_name = card_images[j+i][1]
#                 card_images[j+i][0] = card_images[j+i+1][0]
#                 card_images[j+i][1] = card_images[j+i+1][1]
#                 card_images[j+i+1][0] = swap_obj
#                 card_images[j+i+1][1] = swap_name
