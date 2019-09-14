from Control import config
from View.blackjack_hand_button_parameters import BlackjackHandButtonParam
from View.button import Button


class BlackjackHitButton(Button):
    def __init__(self):
        super(BlackjackHitButton, self).__init__(
            "HIT",
            BlackjackHandButtonParam.hit_x_axis,
            BlackjackHandButtonParam.decision_y_axis,
            BlackjackHandButtonParam.decision_button_width,
            BlackjackHandButtonParam.decision_button_height,
            config.light_gold,
            config.gold,
        )
        self.intro_button()

    # def set_hit_button(self):
    #     self.hit_button = Button(
    #         "HIT",
    #         self.hit_x_axis,
    #         self.decision_y_axis,
    #         self.decision_button_width,
    #         self.decision_button_height,
    #         config.light_gold,
    #         config.gold,
    #     )
    #     self.hit_button.intro_button()
    #
    # def get_hit_button(self):
    #     return self.hit_button
    #
    # def is_hit_selected(self):
    #     if self.hit_button.is_displayed():
    #         return True