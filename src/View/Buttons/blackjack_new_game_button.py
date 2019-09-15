from Control import config
from View.Buttons.blackjack_game_button_view import BlackjackGameButtonView
from View.Buttons.blackjack_post_hand_button_view import BlackjackPostHandButtonView
from View.Buttons.button import Button


class BlackjackNewGameButton(Button):
    def __init__(self):
        super(BlackjackNewGameButton, self).__init__(
            "NEW GAME",
            BlackjackGameButtonView.new_game_x_axis,
            BlackjackGameButtonView.control_y_axis,
            BlackjackGameButtonView.control_button_width,
            BlackjackGameButtonView.control_button_height,
            config.light_gold,
            config.gold,
        )
        self.intro_button()


class BlackjackPostHandNewGameButton(Button):
    def __init__(self):
        super(BlackjackPostHandNewGameButton, self).__init__(
            "NEW GAME",
            BlackjackPostHandButtonView.post_new_game_x_axis,
            BlackjackPostHandButtonView.post_game_type_y_axis,
            BlackjackPostHandButtonView.post_button_width,
            BlackjackPostHandButtonView.post_button_height,
            config.light_gold,
            config.gold,
        )
        self.bool_button()
