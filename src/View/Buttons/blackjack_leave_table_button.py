from Control import config
from View.Buttons.view_blackjack_game_button import BlackjackGameButtonView
from View.Buttons.view_blackjack_post_hand_button import BlackjackPostHandButtonView
from View.Buttons.button import Button


class BlackjackLeaveTableButton(Button):
    def __init__(self):
        super(BlackjackLeaveTableButton, self).__init__(
            "LEAVE TABLE",
            BlackjackGameButtonView.new_game_x_axis,
            BlackjackGameButtonView.control_y_axis,
            BlackjackGameButtonView.control_button_width,
            BlackjackGameButtonView.control_button_height,
            config.light_gold,
            config.gold,
        )
        self.intro_button()


class BlackjackPostHandLeaveTableButton(Button):
    def __init__(self):
        super(BlackjackPostHandLeaveTableButton, self).__init__(
            "LEAVE TABLE",
            BlackjackPostHandButtonView.post_new_game_x_axis,
            BlackjackPostHandButtonView.post_game_type_y_axis,
            BlackjackPostHandButtonView.post_button_width,
            BlackjackPostHandButtonView.post_button_height,
            config.light_gold,
            config.gold,
        )
        self.bool_button()
