# displays main game board
import pygame
import time
from Control import config
from View.soundeffects import Sound
from View.button import Button


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
                        100,
                        500,
                        100,
                        50,
                        config.rose_white,
                        config.dark_red,
                        self.hit,
                    )
                    hit_button.intro_button()
                    stand_button = Button(
                        "STAND", 300, 500, 100, 50, config.rose_white, config.dark_red
                    )
                    stand_button.bool_button()
                    if stand_button.is_displayed():
                        self.stand()
                    # buttons that return a boolean for new game and quit game
                    new_game_button = Button(
                        "NEW GAME",
                        800,
                        500,
                        150,
                        50,
                        config.rose_white,
                        config.dark_red,
                    )
                    new_game_button.bool_button()
                    if new_game_button.is_displayed():
                        config.new_game = True
                        self.loop_1 = False
                    quit_button = Button(
                        "QUIT GAME",
                        1000,
                        500,
                        150,
                        50,
                        config.rose_white,
                        config.dark_red,
                    )
                    quit_button.bool_button()
                    if quit_button.is_displayed():
                        config.game_exit = True
                        self.loop_1 = False

            # buttons for hit,stand,new game, and quit game
            hit_button = Button(
                "HIT", 100, 500, 100, 50, config.light_gold, config.gold
            )
            hit_button.intro_button()
            stand_button = Button(
                "STAND", 300, 500, 100, 50, config.light_gold, config.gold
            )
            stand_button.intro_button()
            new_game_button = Button(
                "NEW GAME", 800, 500, 150, 50, config.light_gold, config.gold
            )
            new_game_button.intro_button()
            quit_button = Button(
                "QUIT GAME", 1000, 500, 150, 50, config.light_gold, config.gold
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
                        "NEXT HAND", 100, 500, 150, 50, config.light_gold, config.gold
                    )
                    next_hand_button.bool_button()
                    if next_hand_button.is_displayed():
                        self.loop_2 = False
                    new_game_button = Button(
                        "NEW GAME", 800, 500, 150, 50, config.light_gold, config.gold
                    )
                    new_game_button.bool_button()
                    if new_game_button.is_displayed():
                        config.new_game = True
                        self.loop_2 = False
                    quit_button = Button(
                        "QUIT GAME", 1000, 500, 150, 50, config.light_gold, config.gold
                    )
                    quit_button.bool_button()
                    if quit_button.is_displayed():
                        config.game_exit = True
                        self.loop_2 = False

            # config.gameDisplay.fill(config.board_color)
            hit_button = Button(
                "", 100, 500, 100, 50, config.board_color, config.board_color
            )
            hit_button.intro_button()
            stand_button = Button(
                "", 300, 500, 100, 50, config.board_color, config.board_color
            )
            stand_button.intro_button()
            next_hand_button = Button(
                "NEXT HAND", 100, 500, 150, 50, config.light_gold, config.gold
            )
            next_hand_button.bool_button()
            next_hand_button = Button(
                "NEW GAME", 800, 500, 150, 50, config.light_gold, config.gold
            )
            next_hand_button.intro_button()
            new_game_button = Button(
                "QUIT GAME", 1000, 500, 150, 50, config.light_gold, config.gold
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
        large_text = pygame.font.Font("freesansbold.ttf", 80)
        text_surf, text_rect = self.text_objects(text, large_text)
        text_rect.center = ((config.display_width / 2), (config.display_height / 2.5))
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
            right = 500
            down = 50
            card = pygame.image.load(str(dealers_hand[i].get_filename()))
            config.game_display.blit(card, (right + k, down))
            k += 100

    def show_players_hand(self):
        """TODO: Add method description"""

        k = 1
        players_hand = self.control.get_players_hand()
        for i in range(len(players_hand)):
            right = 500
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
        mid_text = pygame.font.Font("freesansbold.ttf", 30)
        text_surf, text_rect = self.text_objects("Balance: $" + balance, mid_text)
        # text_rect.top = (0, 0)
        config.game_display.blit(text_surf, text_rect)
        pygame.display.update()
        # time.sleep(1)