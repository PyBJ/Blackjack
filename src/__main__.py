import pygame
from View.menu import Menu
from View.table import Table
from Control import config
from Control.blackjack_controller import BlackjackController
import os
import sys
import logging
logger = logging.getLogger("ControlView")

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
# from pycallgraph2 import PyCallGraph
# from pycallgraph2 import Config as graph_config
# from pycallgraph2.output import GraphvizOutput
#
#
# output_config = graph_config(max_depth=7)
# graphviz = GraphvizOutput(output_file="UML_Diagram22.png")


class ControlView:
    def __init__(self, controller=None, new_table=None):
        """
        Outer Control Loop, TBD

        Args:
            controller (BlackjackController): Keeps track of game, points, deck
            new_table (Table): Displays UI with controller

        Returns:
            A Blackjack Game

        Raises:
            KeyError: EXAMPLE!!! REPLACE
        """
        self.controller = BlackjackController()
        self.new_table = Table(self.controller)

    @staticmethod
    def quit_game():
        """call the pygame quit() method"""
        pygame.quit()
        quit()

    # passes two objects that tell menu buttons where to go
    def meta_loop(self):
        """Outer game-control loop, controls exit and new_game."""
        config.game_exit = Menu().game_menu()
        while not config.game_exit:
            self.new_table.player_hand_loop()
            logger.info("Something happens")
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
    import logging.config

    LOG_FILENAME = "blackjack.log"
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    ControlView().meta_loop()
