from Control import config
from View.blackjack_game_button_parameters import BlackjackGameButtonParameters
from View.blackjack_post_hand_button_parameters import BlackjackPostHandButtonParameters
from View.button import Button


class BlackjackQuitButton(Button):
    def __init__(self):
        super(BlackjackQuitButton, self).__init__(
            "QUIT GAME",
            BlackjackGameButtonParameters.quit_x_axis,
            BlackjackGameButtonParameters.control_y_axis,
            BlackjackGameButtonParameters.control_button_width,
            BlackjackGameButtonParameters.control_button_height,
            config.light_gold,
            config.gold,
        )
        self.intro_button()


class BlackjackPostHandQuitButton(Button):
    def __init__(self):
        super(BlackjackPostHandQuitButton, self).__init__(
            "QUIT GAME",
            BlackjackPostHandButtonParameters.post_quit_x_axis,
            BlackjackPostHandButtonParameters.post_game_type_y_axis,
            BlackjackPostHandButtonParameters.post_button_width,
            BlackjackPostHandButtonParameters.post_button_height,
            config.light_gold,
            config.gold,
        )
        self.bool_button()
