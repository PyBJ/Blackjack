import pygame
from Control import config
from View.Buttons.button import Button
import logging

logger = logging.getLogger("menu.py")


class Menu:
    def __init__(self):
        """Menu class

            TODO: Add description

            Args:

            Attributes:
                game_loop : bool
                    TODO: Add description
                quit_game : bool
                    TODO: Add description

            Returns:
                The Menu
                TODO: Figure out this class

            Raises:
                KeyError: EXAMPLE!!! REPLACE
        """
        self.game_loop = False
        self.quit_game = False

    @staticmethod
    def text_objects(text, font):
        """
        Args:
            text:
            font:
        """
        text_surface = font.render(text, True, config.black)
        return text_surface, text_surface.get_rect()

    # game_menu now returns a boolean value 0 for main game_loop or 1 for quit game
    def game_menu(self):
        logger.info("[Menu: Menu.game_menu()] start going through method\n")
        logger.debug("[Menu: Menu.game_menu()] set config.menu to TRUE")
        config.menu = True
        logger.debug("[Menu: Menu.game_menu()] WHILE config.menu is TRUE and "
                     "game_loop / quit_game are FALSE, DO:")
        while config.menu and not self.game_loop and not self.quit_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logger.warning("event.type is equal to pygame.QUIT")
                    pygame.quit()
            # config.game_display.fill(config.board_color)
            config.game_display.blit(config.game_menu, [0, 0])

            play_button = Button(
                "PLAY", 400, 250, 80, 40, config.rose_white, config.dark_red
            )

            play_button.bool_button()
            help_button = Button(
                #  TODO: Design Help_Button
                "HELP", 400, 300, 80, 40, config.rose_white, config.dark_red
            )
            help_button.bool_button()
            self.game_loop = play_button.is_displayed()

            quit_button = Button(
                "EXIT", 780, 20, 80, 40, config.rose_white, config.dark_red
            )
            quit_button.bool_button()
            self.quit_game = quit_button.is_displayed()

            # self.ace_show(((config.display_width / 2) - 200), 20)
            pygame.display.update()
            config.clock.tick(15)

        if self.game_loop:
            return 0
        elif self.quit_game:
            return 1
        else:
            print("ERROR IN MENU CLASS")


