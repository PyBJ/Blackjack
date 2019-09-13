# displays main game board
import pygame
import time
from Control import config
from View.blackjack_game_buttons import BlackjackGameButtons
from View.blackjack_hand_buttons import BlackjackHandButtons
from View.soundeffects import Sound
from View.button import Button
import logging

logger = logging.getLogger("table.py")


class AfterBlackjackButtons:
    post_game_type_y_axis = 200
    next_hand_y_axis = 475
    next_hand_x_axis = 200
    post_new_game_x_axis = 630
    post_quit_x_axis = 740
    post_button_width = 100
    post_button_height = 50


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
        self.balance = str(self.control.get_players_balance())

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
        
        check_hit_button = Button
        check_hit_button.action = self.hit
        check_hit_button = BlackjackHandButtons.get_hit_button(Button)
        check_stand_button = Button
        check_split_button = Button
        check_double_down_button = Button
        check_insurance_button = Button
        check_surrender_button = Button

        # config.game_display.fill(config.board_color)
        config.game_display.blit(config.table_background, [0, 0])
        self.show_dealers_hand()
        self.show_balance(str(self.control.get_players_balance()))
        # self.show_players_hand()

        while self.hand_decisions_loop:
            # checks to see if deck is empty
            if config.end_shoe is True:
                self.end_of_shoe()

            # event loop / NOT logic loop
            # creates a list of events per frame per second (mouse movement/clicks etc)
            for event in pygame.event.get():
                self.check_quit_game(event)
                # Check if buttons have been pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # buttons for hit and stand
                    check_hit_button.action = self.hit
                    # hit_button = Button(
                    #     "HIT",
                    #     BlackjackHandButtons.hit_x_axis,
                    #     BlackjackHandButtons.decision_y_axis,
                    #     BlackjackHandButtons.decision_button_width,
                    #     BlackjackHandButtons.decision_button_height,
                    #     config.rose_white,
                    #     config.dark_red,
                    #     self.hit,
                    # )
                    # hit_button.intro_button()
                    stand_button = Button(
                        "STAND",
                        BlackjackHandButtons.stand_x_axis,
                        BlackjackHandButtons.decision_y_axis,
                        BlackjackHandButtons.decision_button_width,
                        BlackjackHandButtons.decision_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    stand_button.bool_button()
                    split_button = Button(
                        "SPLIT",
                        BlackjackHandButtons.split_x_axis,
                        BlackjackHandButtons.decision_y_axis,
                        BlackjackHandButtons.decision_button_width,
                        BlackjackHandButtons.decision_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    split_button.bool_button()
                    double_down_button = Button(
                        "DOUBLE DOWN",
                        BlackjackHandButtons.double_down_x_axis,
                        BlackjackHandButtons.decision_y_axis,
                        BlackjackHandButtons.decision_button_width,
                        BlackjackHandButtons.decision_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    double_down_button.bool_button()
                    insurance_button = Button(
                        "INSURANCE",
                        BlackjackHandButtons.insurance_x_axis,
                        BlackjackHandButtons.decision_y_axis,
                        BlackjackHandButtons.decision_button_width,
                        BlackjackHandButtons.decision_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    insurance_button.bool_button()
                    surrender_button = Button(
                        "SURRENDER",
                        BlackjackHandButtons.surrender_x_axis,
                        BlackjackHandButtons.decision_y_axis,
                        BlackjackHandButtons.decision_button_width,
                        BlackjackHandButtons.decision_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    surrender_button.bool_button()
                    if stand_button.is_displayed():
                        self.stand()
                    # buttons that return a boolean for new game and quit game
                    new_game_button = Button(
                        "NEW GAME",
                        BlackjackGameButtons.new_game_x_axis,
                        BlackjackGameButtons.control_y_axis,
                        BlackjackGameButtons.control_button_width,
                        BlackjackGameButtons.control_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    new_game_button.bool_button()
                    if new_game_button.is_displayed():
                        config.new_game = True
                        self.hand_decisions_loop = False
                    quit_button = Button(
                        "QUIT GAME",
                        BlackjackGameButtons.quit_x_axis,
                        BlackjackGameButtons.control_y_axis,
                        BlackjackGameButtons.control_button_width,
                        BlackjackGameButtons.control_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    quit_button.bool_button()
                    if quit_button.is_displayed():
                        config.game_exit = True
                        self.hand_decisions_loop = False

            # Display Buttons
            display_hit_button = Button
            BlackjackHandButtons.get_hit_button(display_hit_button)

            display_stand_button = Button
            BlackjackHandButtons.get_stand_button(display_stand_button)

            display_split_button = Button
            BlackjackHandButtons.get_split_button(display_split_button)

            display_double_down_button = Button
            BlackjackHandButtons.get_double_down_button(display_double_down_button)

            display_insurance_button = Button
            BlackjackHandButtons.get_insurance_button(display_insurance_button)

            display_surrender_button = Button
            BlackjackHandButtons.get_surrender_button(display_surrender_button)

            display_new_game_button = Button
            BlackjackGameButtons.get_new_game_button(display_new_game_button)

            display_quit_button = Button
            BlackjackGameButtons.get_quit_button(display_quit_button)

            self.show_players_hand()
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
        self.show_balance(str(self.control.get_players_balance()))
        self.show_dealers_hand()
        self.show_players_hand()
        self.show_results(self.result_msg)
        while self.post_hand_decisions_loop:
            for event in pygame.event.get():
                self.check_quit_game(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    next_hand_button = Button(
                        "NEXT HAND",
                        AfterBlackjackButtons.next_hand_x_axis,
                        AfterBlackjackButtons.next_hand_y_axis,
                        AfterBlackjackButtons.post_button_width,
                        AfterBlackjackButtons.post_button_height,
                        config.light_gold,
                        config.gold,
                    )
                    next_hand_button.bool_button()
                    if next_hand_button.is_displayed():
                        self.post_hand_decisions_loop = False
                    new_game_button = Button(
                        "NEW GAME",
                        AfterBlackjackButtons.post_new_game_x_axis,
                        AfterBlackjackButtons.post_game_type_y_axis,
                        AfterBlackjackButtons.post_button_width,
                        AfterBlackjackButtons.post_button_height,
                        config.light_gold,
                        config.gold,
                    )
                    new_game_button.bool_button()
                    if new_game_button.is_displayed():
                        config.new_game = True
                        self.post_hand_decisions_loop = False
                    quit_button = Button(
                        "QUIT GAME",
                        AfterBlackjackButtons.post_quit_x_axis,
                        AfterBlackjackButtons.post_game_type_y_axis,
                        AfterBlackjackButtons.post_button_width,
                        AfterBlackjackButtons.post_button_height,
                        config.light_gold,
                        config.gold,
                    )
                    quit_button.bool_button()
                    if quit_button.is_displayed():
                        config.game_exit = True
                        self.post_hand_decisions_loop = False

            next_hand_button = Button(
                "NEXT HAND",
                AfterBlackjackButtons.next_hand_x_axis,
                AfterBlackjackButtons.next_hand_y_axis,
                AfterBlackjackButtons.post_button_width,
                AfterBlackjackButtons.post_button_height,
                config.light_gold,
                config.gold,
            )
            next_hand_button.bool_button()
            next_hand_button = Button(
                "NEW GAME",
                AfterBlackjackButtons.post_new_game_x_axis,
                AfterBlackjackButtons.post_game_type_y_axis,
                AfterBlackjackButtons.post_button_width,
                AfterBlackjackButtons.post_button_height,
                config.light_gold,
                config.gold,
            )
            next_hand_button.intro_button()
            new_game_button = Button(
                "QUIT GAME",
                AfterBlackjackButtons.post_quit_x_axis,
                AfterBlackjackButtons.post_game_type_y_axis,
                AfterBlackjackButtons.post_button_width,
                AfterBlackjackButtons.post_button_height,
                config.light_gold,
                config.gold,
            )
            new_game_button.intro_button()
            pygame.display.update()
            config.clock.tick(30)
        # Reset loop
        self.post_hand_decisions_loop = True

    @staticmethod
    def text_objects(text, font):
        """
        Args:
            text:
            font:
        """
        text_surface = font.render(text, True, config.gold)
        return text_surface, text_surface.get_rect()

    @staticmethod
    def user_display(self, text):
        """
        Args:
            self:
            text (str):
        """
        large_text = pygame.font.Font("freesansbold.ttf", 25)
        text_surf, text_rect = self.text_objects(text, large_text)
        text_rect.center = ((config.display_width / 1.5), (config.display_height / 20))
        config.game_display.blit(text_surf, text_rect)
        pygame.display.update()
        # starts game loop over and resets
        time.sleep(0.1)

    def end_of_shoe(self):
        """TODO: Add method description"""

        text = "End of Shoe, New Deck after re-deal"
        medium_text = pygame.font.Font("freesansbold.ttf", 50)
        text_surf, text_rect = self.text_objects(text, medium_text)
        text_rect.center = ((config.display_width / 2), (config.display_height / 3.5))
        config.game_display.blit(text_surf, text_rect)
        pygame.display.update()
        # starts game loop over and resets

    def show_dealers_hand(self):
        """TODO: Add method description"""
        k = 1
        dealers_hand = self.control.get_dealers_hand()
        for i in range(len(dealers_hand)):
            right = 350
            down = 50
            card = pygame.image.load(str(dealers_hand[i].get_filename()))
            config.game_display.blit(card, (right + k, down))
            k += 27

    def show_players_hand(self):
        """TODO: Add method description"""

        k = 1
        players_hand = self.control.get_players_hand()
        for i in range(len(players_hand)):
            right = 350
            down = 400
            card = pygame.image.load(str(players_hand[i].get_filename()))
            config.game_display.blit(card, (right + k, down))
            k += 27

    def hit(self):
        """TODO: Add method description"""

        (card, score) = self.control.hit_player()
        if score >= 21:
            self.stand()

    def stand(self):
        """TODO: Add method description"""

        self.result_msg = self.control.hit_dealer()
        self.show_dealers_hand()
        config.hand_loop = False
        self.hand_decisions_loop = False

    def show_results(self, result_msg):
        """
        Args:
            result_msg:
        """
        self.user_display(self, result_msg)

    def show_balance(self, balance):
        """
        Args:
            balance:
        """
        mid_text = pygame.font.Font("freesansbold.ttf", 25)
        text_surf, text_rect = self.text_objects(balance, mid_text)
        # text_rect.top = (0, 0)

        text_rect.right = 770
        text_rect.bottom = 502

        config.game_display.blit(text_surf, text_rect)
        pygame.display.update()
        # time.sleep(1)
