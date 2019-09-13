from Control import config
from View.button import Button


class BlackjackHandButtons(Button):
    decision_y_axis = 550
    hit_x_axis = 20
    stand_x_axis = 130
    split_x_axis = 240
    double_down_x_axis = 350
    insurance_x_axis = 460
    surrender_x_axis = 570
    decision_button_width = 90
    decision_button_height = 30

    @classmethod
    def get_hit_button(cls, stand_button):
        hit_button = Button(
            "HIT",
            cls.hit_x_axis,
            cls.decision_y_axis,
            cls.decision_button_width,
            cls.decision_button_height,
            config.light_gold,
            config.gold,
        )
        hit_button.intro_button()
        return hit_button

    @classmethod
    def get_stand_button(cls, stand_button):
        stand_button = Button(
            "STAND",
            cls.stand_x_axis,
            cls.decision_y_axis,
            cls.decision_button_width,
            cls.decision_button_height,
            config.light_gold,
            config.gold,
        )
        stand_button.intro_button()
        return stand_button

    @classmethod
    def get_split_button(cls, split_button):
        split_button = Button(
            "SPLIT",
            cls.split_x_axis,
            cls.decision_y_axis,
            cls.decision_button_width,
            cls.decision_button_height,
            config.light_gold,
            config.gold,
        )
        split_button.intro_button()
        return split_button

    @classmethod
    def get_double_down_button(cls, double_down_button):
        double_down_button = Button(
            "DOUBLE DOWN",
            cls.double_down_x_axis,
            cls.decision_y_axis,
            cls.decision_button_width,
            cls.decision_button_height,
            config.light_gold,
            config.gold,
        )
        double_down_button.intro_button()
        return double_down_button

    @classmethod
    def get_insurance_button(cls, insurance_button):
        insurance_button = Button(
            "INSURANCE",
            cls.insurance_x_axis,
            cls.decision_y_axis,
            cls.decision_button_width,
            cls.decision_button_height,
            config.light_gold,
            config.gold,
        )
        insurance_button.intro_button()
        return insurance_button

    @classmethod
    def get_surrender_button(cls, surrender_button):
        surrender_button = Button(
            "SURRENDER",
            cls.surrender_x_axis,
            cls.decision_y_axis,
            cls.decision_button_width,
            cls.decision_button_height,
            config.light_gold,
            config.gold,
        )
        surrender_button.intro_button()
        return surrender_button