from Control import config
from View.Buttons.blackjack_hand_button_view import BlackjackHandButtonView
from View.Buttons.button import Button


class BlackjackHitButton(Button):
    def __init__(self):
        super(BlackjackHitButton, self).__init__(
            "HIT",
            BlackjackHandButtonView.hit_x_axis,
            BlackjackHandButtonView.decision_y_axis,
            BlackjackHandButtonView.decision_button_width,
            BlackjackHandButtonView.decision_button_height,
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