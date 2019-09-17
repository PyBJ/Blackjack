from Control import config
from View.Buttons.view_blackjack_hand_button import BlackjackHandButtonView
from View.Buttons.button import Button


class BlackjackStandButton(Button):
    def __init__(self):
        super(BlackjackStandButton, self).__init__(
            "STAND",
            BlackjackHandButtonView.stand_x_axis,
            BlackjackHandButtonView.decision_y_axis,
            BlackjackHandButtonView.decision_button_width,
            BlackjackHandButtonView.decision_button_height,
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