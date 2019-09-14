from Control import config
from View.blackjack_hand_button_parameters import BlackjackHandButtonParam
from View.button import Button


class BlackjackSplitButton(Button):
    def __init__(self):
        super(BlackjackSplitButton, self).__init__(
            "SPLIT",
            BlackjackHandButtonParam.split_x_axis,
            BlackjackHandButtonParam.decision_y_axis,
            BlackjackHandButtonParam.decision_button_width,
            BlackjackHandButtonParam.decision_button_height,
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