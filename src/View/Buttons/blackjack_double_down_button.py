from Control import config
from View.Buttons.view_blackjack_hand_button import BlackjackHandButtonView
from View.Buttons.button import Button


class BlackjackDoubleDownButton(Button):
    def __init__(self):
        super(BlackjackDoubleDownButton, self).__init__(
            "DOUBLE DOWN",
            BlackjackHandButtonView.double_down_x_axis,
            BlackjackHandButtonView.decision_y_axis,
            BlackjackHandButtonView.decision_button_width,
            BlackjackHandButtonView.decision_button_height,
            config.light_gold,
            config.gold,
        )
