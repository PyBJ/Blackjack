import pygame
from View.menu import Menu
from View.table import Table
from Control import config
from Control.blackjack_controller import BlackjackController
import os
import sys
import logging


logger = logging.getLogger("runner")
logger.debug("\n\n\n~~~~~NEW PROGRAM EXECUTION~~~~~\n\n")

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

# from pycallgraph2 import PyCallGraph
# from pycallgraph2 import Config as graph_config
# from pycallgraph2.output import GraphvizOutput
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
        logger.debug("Main: ControlView.__init__(): Create BlackjackController: controller in ControlView")
        self.controller = BlackjackController()

        logger.debug("Main: ControlView.__init__(): Create Table: new_table in ControlView")
        self.new_table = Table(self.controller)

    def quit_game():
        """call the pygame quit() method"""
        pygame.quit()
        quit()

    # passes two objects that tell menu Buttons where to go
    def meta_loop(self):
        """Outer game-control loop, controls exit and new_game."""
        logger.info("Main: ControlView.meta_loop(): Start running through ControlView meta_loop")
        config.game_exit = Menu().game_menu()
        while not config.game_exit:
            logger.debug("While config game_exit bool is FALSE: Simulate blackjack game\n\n")
            #  A player_hand_loop() is really a game loop? The debug message occurs
            #  Each time a new hand is initiated.
            logger.debug("Main: meta_loop() calling Table player_hand_loop() method...")
            self.new_table.player_hand_loop()
            logger.debug("Main: meta_loop() checking if \"NEW GAME\" or \"EXIT GAME\" pressed...")
            if config.new_game:
                logger.debug("Main: meta_loop() ...\"NEW GAME\" HAS been pressed...")
                self.controller = BlackjackController()
                self.new_table = Table(self.controller)
                config.new_game = False
            elif config.game_exit:
                logger.debug("Main: meta_loop() ...\"EXIT GAME\" HAS been pressed...")
                break
            else:
                logger.debug("Main: meta_loop() ...\"NEW GAME\" and \"EXIT GAME\" NOT pressed\n")
                logger.debug("Main: meta_loop() ... calling Table end_of_hand() method")
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
    # logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.basicConfig(
        filename=LOG_FILENAME,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - (%(filename)s : %(lineno)d) - %(message)s ",
    )
    logging.getLogger().addHandler(logging.StreamHandler())
    ControlView().meta_loop()
