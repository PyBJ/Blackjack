import pygame
from Control import config


class Button:
    def __init__(
        self,
            button_label: str,
            x_axis: int,
            y_axis: int,
            width: int,
            height: int,
            active_color,
            inactive_color,
            action=None,
    ):
        """
        Args:
            button_label (str): Description
            x_axis (int): Description
            y_axis (int): Description
            width (int): Description
            height (int): Description
            active_color: Description
            inactive_color: Description
            action:

        Returns:
            Button
        """
        self.button_label = button_label
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.width = width
        self.height = height
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.action = action
        self.button_clicked = False

    # a static method is a method bound to the class not the object of the class
    # cannot modify the class state
    @staticmethod
    def text_objects(text, font):
        """
        Args:
            text:
            font:
        """
        text_surface = font.render(text, True, config.black)
        return text_surface, text_surface.get_rect()

    # button functionality with message, coordinates, width/height, active/inactive color
    def intro_button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (
            self.x_axis + self.width > mouse[0] > self.x_axis
            and self.y_axis + self.height > mouse[1] > self.y_axis
        ):
            pygame.draw.rect(
                config.game_display,
                self.active_color,
                (self.x_axis, self.y_axis, self.width, self.height),
            )
            if click[0] == 1 and self.action:
                # POSSIBLE TEST CASE HERE
                self.action()
        else:
            pygame.draw.rect(
                config.game_display,
                self.inactive_color,
                (self.x_axis, self.y_axis, self.width, self.height),
            )
        small_text = pygame.font.Font("freesansbold.ttf", 10)
        text_surf, text_rect = self.text_objects(self.button_label, small_text)
        #                     center of x_axis     center of y_axis
        text_rect.center = (
            (self.x_axis + (self.width / 2)),
            (self.y_axis + (self.height / 2)),
        )
        config.game_display.blit(text_surf, text_rect)

    # hit,stand, quit, new game
    def game_button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (
            self.x_axis + self.width > mouse[0] > self.x_axis
            and self.y_axis + self.height > mouse[1] > self.y_axis
        ):
            pygame.draw.ellipse(
                config.game_display,
                self.active_color,
                (self.x_axis, self.y_axis, self.width, self.height),
            )
            if click[0] == 1 and self.action:
                self.action()
        else:
            pygame.draw.ellipse(
                config.game_display,
                self.inactive_color,
                (self.x_axis, self.y_axis, self.width, self.height),
            )
        button_text = pygame.font.SysFont("comicsans", 10)
        text_surf, text_ellip = self.text_objects(self.button_label, button_text)
        text_ellip.center = (
            (self.x_axis + (self.width / 2)),
            (self.y_axis + (self.height / 2)),
        )
        config.game_display.blit(text_surf, text_ellip)

    # button functionality with message, coordinates, width/height, active/inactive color
    def bool_button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (
            self.x_axis + self.width > mouse[0] > self.x_axis
            and self.y_axis + self.height > mouse[1] > self.y_axis
        ):
            pygame.draw.rect(
                config.game_display,
                self.active_color,
                (self.x_axis, self.y_axis, self.width, self.height),
            )
            if click[0] == 1:
                # POSSIBLE TEST CASE HERE
                self.button_clicked = True
        else:
            pygame.draw.rect(
                config.game_display,
                self.inactive_color,
                (self.x_axis, self.y_axis, self.width, self.height),
            )
        small_text = pygame.font.Font("freesansbold.ttf", 10)
        text_surf, text_rect = self.text_objects(self.button_label, small_text)
        #                     center of x_axis     center of y_axis
        text_rect.center = (
            (self.x_axis + (self.width / 2)),
            (self.y_axis + (self.height / 2)),
        )
        config.game_display.blit(text_surf, text_rect)

    def is_displayed(self) -> bool:
        return self.button_clicked
