from Control import config
from View.button import Button


class BlackjackGameButtons:
    control_y_axis = 153
    new_game_x_axis = 650
    quit_x_axis = 760
    control_button_width = 100
    control_button_height = 40

    @classmethod
    def get_new_game_button(cls, new_game_button):
        new_game_button = Button(
            "NEW GAME",
            cls.new_game_x_axis,
            cls.control_y_axis,
            cls.control_button_width,
            cls.control_button_height,
            config.light_gold,
            config.gold,
        )
        new_game_button.intro_button()
        return new_game_button

    @classmethod
    def get_quit_button(cls, quit_button):
        quit_button = Button(
            "QUIT GAME",
            cls.quit_x_axis,
            cls.control_y_axis,
            cls.control_button_width,
            cls.control_button_height,
            config.light_gold,
            config.gold,
        )
        quit_button.intro_button()
        return quit_button