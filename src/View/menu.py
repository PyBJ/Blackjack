import pygame
from Control import config
from View.button import Button


class Menu:
    def __init__(self):
        self.game_loop = False
        self.quit_game = False

    @staticmethod
    def text_objects(text, font):
        text_surface = font.render(text, True, config.black)
        return text_surface, text_surface.get_rect()

    # displays ace cards
    @staticmethod
    def ace_show(x, y):
        config.gameDisplay.blit(config.custom_cards[1][0], (x, y))
        config.gameDisplay.blit(config.custom_cards[0][0], (x + 100, y))
        config.gameDisplay.blit(config.custom_cards[3][0], (x + 200, y))
        config.gameDisplay.blit(config.custom_cards[2][0], (x + 300, y))

    # game_menu now returns a boolean value 0 for main game_loop or 1 for quit game
    def game_menu(self):
        config.menu = True
        while config.menu and not self.game_loop and not self.quit_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            config.gameDisplay.fill(config.board_color)
            large_text = pygame.font.Font("freesansbold.ttf", 100)
            text_surf, text_rect = self.text_objects("BlackJack", large_text)
            text_rect.center = ((config.disp_width / 2), (config.disp_height / 2.2))
            config.gameDisplay.blit(text_surf, text_rect)

            play_button = Button(
                "PLAY", 550, 350, 100, 50, config.rose_white, config.dark_red)

            play_button.bool_button()
            self.game_loop = play_button.return_boolean()

            quit_button = Button(
                "QUIT", 550, 425, 100, 50, config.rose_white, config.dark_red
            )
            quit_button.bool_button()
            self.quit_game = quit_button.return_boolean()

            self.ace_show((config.disp_width / 2.9), 40)
            pygame.display.update()
            config.clock.tick(15)

        if self.game_loop:
            return 0
        elif self.quit_game:
            return 1
        else:
            print("ERROR IN MENU CLASS")
