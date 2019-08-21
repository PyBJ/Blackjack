import pygame
from View.menu import Menu
from View.table import Table
from Control import config
from Control.blackjack_controller import BlackjackController
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))
# from pycallgraph2 import PyCallGraph
# from pycallgraph2 import Config as graph_config
# from pycallgraph2.output import GraphvizOutput

# output_config = graph_config(max_depth=7)
# graphviz = GraphvizOutput(output_file='UML_Diagram.png')


class ControlView:
    def __init__(self):
        self.controller = BlackjackController()
        self.new_table = Table(self.controller)

    @staticmethod
    def quit_game():
        pygame.quit()
        quit()

    # passes two objects that tell menu buttons where to go
    def meta_loop(self):
        config.game_exit = Menu().game_menu()
        while not config.game_exit:
            self.new_table.player_hand_loop()
            if config.new_game:
                self.controller = BlackjackController()
                self.new_table = Table(self.controller)
                config.new_game = False
            elif config.game_exit:
                break
            else:
                self.new_table.end_of_hand()
                if config.new_game or config.end_shoe:
                    self.controller = BlackjackController()
                    self.new_table = Table(self.controller)
                    config.new_game = False
                else:
                    self.controller.get_new_player_hand()
                    self.controller.get_new_dealer_hand()
            config.end_shoe = self.controller.get_if_shoe_end()


if __name__ == "__main__":
    # with PyCallGraph(output=graphviz, config=output_config):
        ControlView().meta_loop()
