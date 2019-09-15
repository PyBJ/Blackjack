from Control import config
from View.Buttons.blackjack_post_hand_button_view import BlackjackPostHandButtonView
from View.Buttons.button import Button


class BlackjackNextHandButton(Button):
    def __init__(self):
        super(BlackjackNextHandButton, self).__init__(
            "NEXT HAND",
            BlackjackPostHandButtonView.next_hand_x_axis,
            BlackjackPostHandButtonView.next_hand_y_axis,
            BlackjackPostHandButtonView.post_button_width,
            BlackjackPostHandButtonView.post_button_height,
            config.light_gold,
            config.gold,
        )
        self.bool_button()