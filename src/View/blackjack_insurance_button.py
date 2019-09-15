from Control import config
from View.blackjack_hand_button_view import BlackjackHandButtonView
from View.button import Button


class BlackjackInsuranceButton(Button):
    def __init__(self):
        super(BlackjackInsuranceButton, self).__init__(
            "INSURANCE",
            BlackjackHandButtonView.insurance_x_axis,
            BlackjackHandButtonView.decision_y_axis,
            BlackjackHandButtonView.decision_button_width,
            BlackjackHandButtonView.decision_button_height,
            config.light_gold,
            config.gold,
        )

    # def get_insurance_button(self, insurance_button):
    #     insurance_button = Button(
    #         "INSURANCE",
    #         BlackjackHandButtonParam.insurance_x_axis,
    #         BlackjackHandButtonParam.decision_y_axis,
    #         BlackjackHandButtonParam.decision_button_width,
    #         BlackjackHandButtonParam.decision_button_height,
    #         config.light_gold,
    #         config.gold,
    #     )
    #     insurance_button.intro_button()
    #     return insurance_button