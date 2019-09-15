from Control import config
from View.button import Button


class BlackjackPostHandButtonParameters:
    post_game_type_y_axis = 200
    next_hand_y_axis = 475
    next_hand_x_axis = 200
    post_new_game_x_axis = 630
    post_quit_x_axis = 740
    post_button_width = 100
    post_button_height = 50


class BlackjackNextHandButton(Button):
    def __init__(self):
        super(BlackjackNextHandButton, self).__init__(
            "NEXT HAND",
            BlackjackPostHandButtonParameters.next_hand_x_axis,
            BlackjackPostHandButtonParameters.next_hand_y_axis,
            BlackjackPostHandButtonParameters.post_button_width,
            BlackjackPostHandButtonParameters.post_button_height,
            config.light_gold,
            config.gold,
        )
        self.bool_button()
