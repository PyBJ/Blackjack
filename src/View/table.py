# displays main game board
import pygame
import time
from Control import config
from View.soundeffects import Sound
from View.button import Button


class DecisionButtons:
    decision_y_axis = 550
    hit_x_axis = 20
    stand_x_axis = 130
    split_x_axis = 240
    double_down_x_axis = 350
    insurance_x_axis = 460
    surrender_x_axis = 570
    decision_button_width = 90
    decision_button_height = 30


class ControlButtons:
    control_y_axis = 40
    new_game_x_axis = 635
    quit_x_axis = 755
    control_button_width = 100
    control_button_height = 40


class PostGameButtons:
    post_game_y_axis = 275
    next_hand_x_axis = 200
    post_new_game_x_axis = 500
    post_quit_x_axis = 640
    post_button_width = 100
    post_button_height = 50


class Table:
    def __init__(self, controller):
        """
        Args:
            controller:
        """
        self.control = controller
        self.loop_1 = True
        self.loop_2 = True
        self.result_msg = ""
        self.balance = str(self.control.get_players_balance())

    # Player Hand Loop sets config.new_game and config.game_exit or goes though hand
    def player_hand_loop(self):
        config.game_exit = False

        # Sound Effect of Dealing 4 cards
        sound = Sound()
        sound.get_sound_effect("Deal4")

        config.game_display.fill(config.board_color)
        self.show_dealers_hand()
        self.show_balance(str(self.control.get_players_balance()))
        # self.show_players_hand()

        while self.loop_1:
            # checks to see if deck is empty
            if config.end_shoe is True:
                self.end_of_shoe()

            # event loop / NOT logic loop
            # creates a list of events per frame per second (mouse movement/clicks etc)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    config.game_exit = True
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # buttons for hit and stand
                    hit_button = Button(
                        "HIT",
                        DecisionButtons.hit_x_axis,
                        DecisionButtons.decision_y_axis,
                        DecisionButtons.decision_button_width,
                        DecisionButtons.decision_button_height,
                        config.rose_white,
                        config.dark_red,
                        self.hit,
                    )
                    hit_button.intro_button()
                    stand_button = Button(
                        "STAND",
                        DecisionButtons.stand_x_axis,
                        DecisionButtons.decision_y_axis,
                        DecisionButtons.decision_button_width,
                        DecisionButtons.decision_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    stand_button.bool_button()
                    split_button = Button(
                        "SPLIT",
                        DecisionButtons.split_x_axis,
                        DecisionButtons.decision_y_axis,
                        DecisionButtons.decision_button_width,
                        DecisionButtons.decision_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    split_button.bool_button()
                    double_down_button = Button(
                        "DOUBLE DOWN",
                        DecisionButtons.double_down_x_axis,
                        DecisionButtons.decision_y_axis,
                        DecisionButtons.decision_button_width,
                        DecisionButtons.decision_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    double_down_button.bool_button()
                    insurance_button = Button(
                        "INSURANCE",
                        DecisionButtons.insurance_x_axis,
                        DecisionButtons.decision_y_axis,
                        DecisionButtons.decision_button_width,
                        DecisionButtons.decision_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    insurance_button.bool_button()
                    surrender_button = Button(
                        "SURRENDER",
                        DecisionButtons.surrender_x_axis,
                        DecisionButtons.decision_y_axis,
                        DecisionButtons.decision_button_width,
                        DecisionButtons.decision_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    surrender_button.bool_button()
                    if stand_button.is_displayed():
                        self.stand()
                    # buttons that return a boolean for new game and quit game
                    new_game_button = Button(
                        "NEW GAME", ControlButtons.new_game_x_axis, ControlButtons.control_y_axis,
                        ControlButtons.control_button_width, ControlButtons.control_button_height,
                        config.rose_white, config.dark_red
                    )
                    new_game_button.bool_button()
                    if new_game_button.is_displayed():
                        config.new_game = True
                        self.loop_1 = False
                    quit_button = Button(
                        "QUIT GAME",
                        ControlButtons.quit_x_axis,
                        ControlButtons.control_y_axis,
                        ControlButtons.control_button_width,
                        ControlButtons.control_button_height,
                        config.rose_white,
                        config.dark_red,
                    )
                    quit_button.bool_button()
                    if quit_button.is_displayed():
                        config.game_exit = True
                        self.loop_1 = False

            # buttons for hit,stand,new game, and quit game
            hit_button = Button(
                "HIT",
                DecisionButtons.hit_x_axis,
                DecisionButtons.decision_y_axis,
                DecisionButtons.decision_button_width,
                DecisionButtons.decision_button_height,
                config.light_gold,
                config.gold,
            )
            hit_button.intro_button()
            stand_button = Button(
                "STAND",
                DecisionButtons.stand_x_axis,
                DecisionButtons.decision_y_axis,
                DecisionButtons.decision_button_width,
                DecisionButtons.decision_button_height,
                config.light_gold,
                config.gold,
            )
            stand_button.intro_button()
            split_button = Button(
                "SPLIT",
                DecisionButtons.split_x_axis,
                DecisionButtons.decision_y_axis,
                DecisionButtons.decision_button_width,
                DecisionButtons.decision_button_height,
                config.light_gold,
                config.gold,
            )
            split_button.intro_button()
            double_down_button = Button(
                "DOUBLE DOWN",
                DecisionButtons.double_down_x_axis,
                DecisionButtons.decision_y_axis,
                DecisionButtons.decision_button_width,
                DecisionButtons.decision_button_height,
                config.light_gold,
                config.gold,
            )
            double_down_button.intro_button()
            insurance_button = Button(
                "INSURANCE",
                DecisionButtons.insurance_x_axis,
                DecisionButtons.decision_y_axis,
                DecisionButtons.decision_button_width,
                DecisionButtons.decision_button_height,
                config.light_gold,
                config.gold,
            )
            insurance_button.intro_button()
            surrender_button = Button(
                "SURRENDER",
                DecisionButtons.surrender_x_axis,
                DecisionButtons.decision_y_axis,
                DecisionButtons.decision_button_width,
                DecisionButtons.decision_button_height,
                config.light_gold,
                config.gold,
            )
            surrender_button.intro_button()
            new_game_button = Button(
                "NEW GAME", ControlButtons.new_game_x_axis, ControlButtons.control_y_axis,
                ControlButtons.control_button_width, ControlButtons.control_button_height,
                config.light_gold, config.gold
            )
            new_game_button.intro_button()
            quit_button = Button(
                "QUIT GAME", ControlButtons.quit_x_axis,
                ControlButtons.control_y_axis,
                ControlButtons.control_button_width,
                ControlButtons.control_button_height,
                config.light_gold, config.gold
            )
            quit_button.intro_button()

            self.show_players_hand()
            if self.control.starting_blackjack:
                self.result_msg = "Blackjack! You Win!"
                self.show_results(self.result_msg)
                self.control.starting_blackjack = False
                self.loop_1 = False
            pygame.display.update()
            config.clock.tick(15)
        self.loop_1 = True

    # End of Hand
    def end_of_hand(self):
        """The players hand is over"""
        config.game_display.fill(config.board_color)
        self.show_balance(str(self.control.get_players_balance()))
        self.show_dealers_hand()
        self.show_players_hand()
        self.show_results(self.result_msg)
        while self.loop_2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    config.game_exit = True
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    next_hand_button = Button(
                        "NEXT HAND", PostGameButtons.next_hand_x_axis,
                        PostGameButtons.post_game_y_axis, PostGameButtons.post_button_width,
                        PostGameButtons.post_button_height, config.light_gold, config.gold
                    )
                    next_hand_button.bool_button()
                    if next_hand_button.is_displayed():
                        self.loop_2 = False
                    new_game_button = Button(
                        "NEW GAME", PostGameButtons.post_new_game_x_axis,
                        PostGameButtons.post_game_y_axis, PostGameButtons.post_button_width,
                        PostGameButtons.post_button_height, config.light_gold, config.gold
                    )
                    new_game_button.bool_button()
                    if new_game_button.is_displayed():
                        config.new_game = True
                        self.loop_2 = False
                    quit_button = Button(
                        "QUIT GAME", PostGameButtons.post_quit_x_axis,
                        PostGameButtons.post_game_y_axis,
                        PostGameButtons.post_button_width,
                        PostGameButtons.post_button_height,
                        config.light_gold, config.gold
                    )
                    quit_button.bool_button()
                    if quit_button.is_displayed():
                        config.game_exit = True
                        self.loop_2 = False

            # config.gameDisplay.fill(config.board_color)
            hit_button = Button(
                "",
                DecisionButtons.hit_x_axis,
                DecisionButtons.decision_y_axis,
                DecisionButtons.decision_button_width,
                DecisionButtons.decision_button_height,
                config.board_color,
                config.board_color,
            )
            hit_button.intro_button()
            stand_button = Button(
                "",
                DecisionButtons.stand_x_axis,
                DecisionButtons.decision_y_axis,
                DecisionButtons.decision_button_width,
                DecisionButtons.decision_button_height,
                config.board_color,
                config.board_color,
            )
            stand_button.intro_button()
            next_hand_button = Button(
                "NEXT HAND", PostGameButtons.next_hand_x_axis,
                PostGameButtons.post_game_y_axis, PostGameButtons.post_button_width, PostGameButtons.post_button_height, config.light_gold, config.gold
            )
            next_hand_button.bool_button()
            next_hand_button = Button(
                "NEW GAME", PostGameButtons.post_new_game_x_axis, PostGameButtons.post_game_y_axis,
                PostGameButtons.post_button_width, PostGameButtons.post_button_height, config.light_gold, config.gold
            )
            next_hand_button.intro_button()
            new_game_button = Button(
                "QUIT GAME", PostGameButtons.post_quit_x_axis,
                PostGameButtons.post_game_y_axis, PostGameButtons.post_button_width, PostGameButtons.post_button_height, config.light_gold, config.gold
            )
            new_game_button.intro_button()
            pygame.display.update()
            config.clock.tick(30)
        # Reset loop
        self.loop_2 = True

    @staticmethod
    def text_objects(text, font):
        """
        Args:
            text:
            font:
        """
        text_surface = font.render(text, True, config.black)
        return text_surface, text_surface.get_rect()

    @staticmethod
    def user_display(self, text):
        """
        Args:
            self:
            text (str):
        """
        large_text = pygame.font.Font("freesansbold.ttf", 40)
        text_surf, text_rect = self.text_objects(text, large_text)
        text_rect.center = ((config.display_width / 2), (config.display_height / 3))
        config.game_display.blit(text_surf, text_rect)
        pygame.display.update()
        # starts game loop over and resets
        time.sleep(1)

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
            k += 100

    def show_players_hand(self):
        """TODO: Add method description"""

        k = 1
        players_hand = self.control.get_players_hand()
        for i in range(len(players_hand)):
            right = 350
            down = 400
            card = pygame.image.load(str(players_hand[i].get_filename()))
            config.game_display.blit(card, (right + k, down))
            k += 100

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
        self.loop_1 = False

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
        text_surf, text_rect = self.text_objects("Balance: " + balance, mid_text)
        # text_rect.top = (0, 0)

        text_rect.right = 240
        text_rect.bottom = 500

        config.game_display.blit(text_surf, text_rect)
        pygame.display.update()
        # time.sleep(1)
