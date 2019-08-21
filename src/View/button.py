import pygame
from Control import config


class Button:
    def __init__(self, msg, x, y, w, h, ac, ic, action=None):
        """

        :rtype: object
        """
        self.msg = msg
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ac = ac
        self.ic = ic
        self.action = action
        self.boolean = False

    # a static method is a method bound to the class not the object of the class
    # cannot modify the class state
    @staticmethod
    def text_objects(text, font):
        text_surface = font.render(text, True, config.black)
        return text_surface, text_surface.get_rect()

    # button functionality with message, coordinates, width/height, active/inactive color
    def intro_button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            pygame.draw.rect(
                config.gameDisplay, self.ac, (self.x, self.y, self.w, self.h)
            )
            if click[0] == 1 and self.action:
                # POSSIBLE TEST CASE HERE
                self.action()
        else:
            pygame.draw.rect(
                config.gameDisplay, self.ic, (self.x, self.y, self.w, self.h)
            )
        small_text = pygame.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = self.text_objects(self.msg, small_text)
        #                     center of x     center of y
        text_rect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        config.gameDisplay.blit(text_surf, text_rect)

    # hit,stand, quit, new game
    def game_button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            pygame.draw.ellipse(
                config.gameDisplay, self.ac, (self.x, self.y, self.w, self.h)
            )
            if click[0] == 1 and self.action:
                self.action()
        else:
            pygame.draw.ellipse(
                config.gameDisplay, self.ic, (self.x, self.y, self.w, self.h)
            )
        button_text = pygame.font.SysFont("comicsans", 20)
        text_surf, text_ellip = self.text_objects(self.msg, button_text)
        text_ellip.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        config.gameDisplay.blit(text_surf, text_ellip)

    # button functionality with message, coordinates, width/height, active/inactive color
    def bool_button(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            pygame.draw.rect(
                config.gameDisplay, self.ac, (self.x, self.y, self.w, self.h)
            )
            if click[0] == 1:
                # POSSIBLE TEST CASE HERE
                self.boolean = True
        else:
            pygame.draw.rect(
                config.gameDisplay, self.ic, (self.x, self.y, self.w, self.h)
            )
        small_text = pygame.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = self.text_objects(self.msg, small_text)
        #                     center of x     center of y
        text_rect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        config.gameDisplay.blit(text_surf, text_rect)

    def return_boolean(self):
        return self.boolean
