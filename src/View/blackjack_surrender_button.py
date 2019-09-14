from Control import config
from View.blackjack_hand_button_parameters import BlackjackHandButtonParam
from View.button import Button


class BlackjackSurrenderButton(Button):
    def __init__(self):
        super(BlackjackSurrenderButton, self).__init__(
            "SURRENDER",
            BlackjackHandButtonParam.surrender_x_axis,
            BlackjackHandButtonParam.decision_y_axis,
            BlackjackHandButtonParam.decision_button_width,
            BlackjackHandButtonParam.decision_button_height,
            config.light_gold,
            config.gold,
        )

    # def get_surrender_button(self, surrender_button):
    #     surrender_button = Button(
    #         "SURRENDER",
    #         BlackjackHandButtonParam.surrender_x_axis,
    #         BlackjackHandButtonParam.decision_y_axis,
    #         BlackjackHandButtonParam.decision_button_width,
    #         BlackjackHandButtonParam.decision_button_height,
    #         config.light_gold,
    #         config.gold,
    #     )
    #     surrender_button.intro_button()
    #     return surrender_button