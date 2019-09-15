from Control import config
from View.Buttons.blackjack_game_button_view import BlackjackGameButtonView
from View.Buttons.blackjack_post_hand_button_view import BlackjackPostHandButtonView
from View.Buttons.button import Button


class BlackjackQuitButton(Button):
    def __init__(self):
        super(BlackjackQuitButton, self).__init__(
            "QUIT GAME",
            BlackjackGameButtonView.quit_x_axis,
            BlackjackGameButtonView.control_y_axis,
            BlackjackGameButtonView.control_button_width,
            BlackjackGameButtonView.control_button_height,
            config.light_gold,
            config.gold,
        )
        self.intro_button()


class BlackjackPostHandQuitButton(Button):
    def __init__(self):
        super(BlackjackPostHandQuitButton, self).__init__(
            "QUIT GAME",
            BlackjackPostHandButtonView.post_quit_x_axis,
            BlackjackPostHandButtonView.post_game_type_y_axis,
            BlackjackPostHandButtonView.post_button_width,
            BlackjackPostHandButtonView.post_button_height,
            config.light_gold,
            config.gold,
        )
        self.bool_button()
