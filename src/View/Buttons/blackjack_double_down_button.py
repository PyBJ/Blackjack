from Control import config
from View.Buttons.blackjack_hand_button_view import BlackjackHandButtonView
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

    # def get_double_down_button(self, double_down_button):
    #     double_down_button = Button(
    #         "DOUBLE DOWN",
    #         BlackjackHandButtonParam.double_down_x_axis,
    #         BlackjackHandButtonParam.decision_y_axis,
    #         BlackjackHandButtonParam.decision_button_width,
    #         BlackjackHandButtonParam.decision_button_height,
    #         config.light_gold,
    #         config.gold,
    #     )
    #     double_down_button.intro_button()
    #     return double_down_button