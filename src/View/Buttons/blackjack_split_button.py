from Control import config
from View.Buttons.blackjack_hand_button_view import BlackjackHandButtonView
from View.Buttons.button import Button


class BlackjackSplitButton(Button):
    def __init__(self):
        super(BlackjackSplitButton, self).__init__(
            "SPLIT",
            BlackjackHandButtonView.split_x_axis,
            BlackjackHandButtonView.decision_y_axis,
            BlackjackHandButtonView.decision_button_width,
            BlackjackHandButtonView.decision_button_height,
            config.light_gold,
            config.gold,
        )

    # def get_split_button(self, split_button):
    #     split_button = Button(
    #         "SPLIT",
    #         BlackjackHandButtonParam.split_x_axis,
    #         BlackjackHandButtonParam.decision_y_axis,
    #         BlackjackHandButtonParam.decision_button_width,
    #         BlackjackHandButtonParam.decision_button_height,
    #         config.light_gold,
    #         config.gold,
    #     )
    #     split_button.intro_button()
    #     return split_button