# displays main game board
import pygame
import time
from Control import config
from View.Buttons.blackjack_next_hand_button import BlackjackNextHandButton
from View.Buttons.blackjack_leave_table_button import BlackjackPostHandLeaveTableButton
from View.Buttons.blackjack_quit_game_button import BlackjackPostHandQuitButton
from View.Buttons.blackjack_surrender_button import BlackjackSurrenderButton
from View.Buttons.blackjack_insurance_button import BlackjackInsuranceButton
from View.Buttons.blackjack_double_down_button import BlackjackDoubleDownButton
from View.Buttons.blackjack_split_button import BlackjackSplitButton
from View.Buttons.blackjack_stand_button import BlackjackStandButton
from View.Buttons.blackjack_hit_button import BlackjackHitButton
from View.Buttons.blackjack_leave_table_button import BlackjackLeaveTableButton
from View.Buttons.blackjack_quit_game_button import BlackjackQuitButton
from View.hand import show_players_hand, show_dealers_hand

from View.soundeffects import Sound
import logging

logger = logging.getLogger("table.py")


def display_hand_buttons():
    hit_button = BlackjackHitButton()
    hit_button.intro_button()

    stand_button = BlackjackStandButton()
    stand_button.intro_button()

    split_button = BlackjackSplitButton()
    split_button.intro_button()

    double_down_button = BlackjackDoubleDownButton()
    double_down_button.intro_button()

    insurance_button = BlackjackInsuranceButton()
    insurance_button.intro_button()

    surrender_button = BlackjackSurrenderButton()
    surrender_button.intro_button()

    display_leave_table_button = BlackjackLeaveTableButton()
    display_leave_table_button.intro_button()

    display_quit_button = BlackjackQuitButton()
    display_quit_button.intro_button()


def display_end_of_hand_buttons():
    next_hand_button = BlackjackNextHandButton()
    next_hand_button.intro_button()

    new_game_button = BlackjackPostHandLeaveTableButton()
    new_game_button.intro_button()

    quit_button = BlackjackPostHandQuitButton()
    quit_button.intro_button()


class Table:
    def __init__(self, controller):
        """
        Args:
            controller:
        """
        self.control = controller
        self.hand_decisions_loop = True
        self.post_hand_decisions_loop = True
        self.result_msg = ""
        self.balance = self.control.get_players_balance()
        self.ante = self.control.get_players_bet()
        self.pay_ante = False

    def check_quit_game(self, event):
        if event.type == pygame.QUIT:
            config.game_exit = True
            pygame.quit()
            quit()

    # Player Hand Loop sets config.new_game and config.game_exit or goes though hand
    def player_hand_loop(self):
        config.game_exit = False
        # Sound Effect of Dealing 4 cards
        sound = Sound()
        sound.get_sound_effect("Deal4")

        config.game_display.blit(config.table_background, [0, 0])
        self.get_players_ante()

        while self.hand_decisions_loop:
            # checks to see if deck is empty
            if config.end_shoe is True:
                self.end_of_shoe()

            # event loop / NOT logic loop
            # creates a list of events per frame per second (mouse movement/clicks etc)
            for event in pygame.event.get():
                self.check_quit_game(event)
                # Check if Buttons have been pressed
                if event.type == pygame.MOUSEBUTTONDOWN:

                    hit_button = BlackjackHitButton()
                    hit_button.bool_button()
                    if hit_button.is_displayed():
                        self.hit()

                    stand_button = BlackjackStandButton()
                    stand_button.bool_button()
                    if stand_button.is_displayed():
                        self.stand()

                    split_button = BlackjackSplitButton()
                    split_button.bool_button()

                    double_down_button = BlackjackDoubleDownButton()
                    double_down_button.bool_button()

                    insurance_button = BlackjackInsuranceButton()
                    insurance_button.bool_button()

                    surrender_button = BlackjackSurrenderButton()
                    surrender_button.bool_button()

                    leave_table_button = BlackjackLeaveTableButton()
                    leave_table_button.bool_button()
                    if leave_table_button.is_displayed():
                        config.new_game = True
                        self.hand_decisions_loop = False

                    quit_button = BlackjackQuitButton()
                    quit_button.bool_button()
                    if quit_button.is_displayed():
                        config.game_exit = True
                        self.hand_decisions_loop = False

            display_hand_buttons()
            self.show_hands()

            if self.control.starting_blackjack:
                self.result_msg = "Blackjack! You Win!"
                self.show_results(self.result_msg)
                self.control.starting_blackjack = False
                self.hand_decisions_loop = False
            pygame.display.update()
            config.clock.tick(15)
        self.hand_decisions_loop = True

    # End of Hand
    def end_of_hand(self):
        """The players hand is over"""
        logger.info("[table: end_of_hand()] starting the end_of_hand() methods")
        config.game_display.blit(config.table_background, [0, 0])
        self.pay_ante = False
        self.display_balance_and_bet()

        self.show_hands()

        self.show_results(self.result_msg)
        while self.post_hand_decisions_loop:
            for event in pygame.event.get():
                self.check_quit_game(event)

                if event.type == pygame.MOUSEBUTTONDOWN:

                    next_hand_button = BlackjackNextHandButton()
                    next_hand_button.bool_button()
                    if next_hand_button.is_displayed():
                        self.post_hand_decisions_loop = False

                    new_game_button = BlackjackPostHandLeaveTableButton()
                    new_game_button.bool_button()
                    if new_game_button.is_displayed():
                        config.new_game = True
                        self.post_hand_decisions_loop = False

                    quit_button = BlackjackPostHandQuitButton()
                    quit_button.bool_button()
                    if quit_button.is_displayed():
                        config.game_exit = True
                        self.post_hand_decisions_loop = False

            display_end_of_hand_buttons()

            pygame.display.update()
            config.clock.tick(30)
        # Reset loop
        self.post_hand_decisions_loop = True

    @staticmethod
    def gold_text_objects(text, font):
        """
        Args:
            text:
            font:
        """
        text_surface = font.render(text, True, config.gold)
        return text_surface, text_surface.get_rect()

    @staticmethod
    def red_text_objects(text, font):
        """
        Args:
            text:
            font:
        """
        text_surface = font.render(text, True, config.deep_red)
        return text_surface, text_surface.get_rect()

    def end_of_shoe(self):
        """TODO: Add method description"""

        text = "End of Shoe, New Deck after re-deal"
        medium_text = pygame.font.Font("freesansbold.ttf", 50)
        text_surf, text_rect = self.gold_text_objects(text, medium_text)
        text_rect.center = ((config.display_width / 2), (config.display_height / 3.5))
        config.game_display.blit(text_surf, text_rect)
        pygame.display.update()
        # starts game loop over and resets

    def hit(self):
        """TODO: Add method description"""

        (card, score) = self.control.hit_player()
        if score >= 21:
            self.stand()

    def stand(self):
        """TODO: Add method description"""

        self.result_msg = self.control.hit_dealer()
        show_dealers_hand(self.control)
        config.hand_loop = False
        self.hand_decisions_loop = False

    def show_results(self, result_msg):
        """
        Args:
            result_msg:
        """
        user_display(self, result_msg)

    def show_balance(self, balance):
        """
        Args:
            balance:
        """
        mid_text = pygame.font.Font("freesansbold.ttf", 25)
        text_surf, text_rect = self.gold_text_objects(balance, mid_text)
        # text_rect.top = (0, 0)

        text_rect.right = 770
        text_rect.bottom = 502

        config.game_display.blit(text_surf, text_rect)
        pygame.display.update()
        # time.sleep(1)

    def show_bet(self, ante):
        """
        Args:
            ante:
        """
        mid_text = pygame.font.Font("freesansbold.ttf", 40)
        text_surf, text_rect = self.red_text_objects(ante, mid_text)
        # text_rect.top = (0, 0)

        text_rect.right = 485
        text_rect.bottom = 305

        config.game_display.blit(text_surf, text_rect)
        pygame.display.update()

    def display_balance_and_bet(self):
        self.show_balance(str(self.control.get_players_balance()))
        self.show_bet(str(self.control.get_players_bet()))

    def get_players_ante(self):
        if not self.pay_ante:
            self.control.subtract_players_ante()
            self.pay_ante = True
            self.display_balance_and_bet()
        else:
            self.display_balance_and_bet()

    def show_hands(self):
        show_dealers_hand(self.control)
        show_players_hand(self.control)


def user_display(self, text):
    """
    Args:
        self:
        text (str):
    """
    large_text = pygame.font.Font("freesansbold.ttf", 25)
    text_surf, text_rect = self.gold_text_objects(text, large_text)
    text_rect.center = ((config.display_width / 1.5), (config.display_height / 20))
    config.game_display.blit(text_surf, text_rect)
    pygame.display.update()
    # starts game loop over and resets
    time.sleep(0.1)