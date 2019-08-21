import sys
import unittest
import pygame
from Control import config, control_view


class TestGame(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.game = control_view.ControlView()
        pygame.init()

    def tearDown(self):
        pygame.quit()
        unittest.TestCase.tearDown(self)

    def test_game_running(self):
        self.assertFalse(sys.stdin.close())


if __name__ == '__main__':
    unittest.main()