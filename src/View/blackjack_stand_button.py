from Control import config
from View.blackjack_hand_button_parameters import BlackjackHandButtonParam
from View.button import Button


class BlackjackStandButton(Button):
    def __init__(self):
        super(BlackjackStandButton, self).__init__(
            "STAND",
            BlackjackHandButtonParam.stand_x_axis,
            BlackjackHandButtonParam.decision_y_axis,
            BlackjackHandButtonParam.decision_button_width,
            BlackjackHandButtonParam.decision_button_height,
            config.light_gold,
            config.gold,
        )

    # def get_stand_button(self, stand_button):
    #     stand_button = Button(
    #         "STAND",
    #         BlackjackHandButtonParam.stand_x_axis,
    #         BlackjackHandButtonParam.decision_y_axis,
    #         BlackjackHandButtonParam.decision_button_width,
    #         BlackjackHandButtonParam.decision_button_height,
    #         config.light_gold,
    #         config.gold,
    #     )
    #     stand_button.intro_button()
    #     return stand_button