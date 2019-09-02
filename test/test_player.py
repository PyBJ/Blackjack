import unittest
from Model.deck import Deck
from Control import player


class PlayerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
        self.default_balance = 10000
        self.test_suit_list = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
        self.test_player = player.BlackjackPlayer([self.deck.deal(), self.deck.deal()], self.default_balance)

    def test_player_hand_size(self):
        self.assertEqual(len(self.test_player.get_hand()), 2)

    def test_player_hand(self):
        self.assertIn('of', self.test_player.__str__())

    def test_player_hand_str(self):
        print(self.test_player.__str__())
    #
    def test_player_hand_score(self):
        self.assertTrue(self.test_player.get_score() > 0)
        self.assertTrue(self.test_player.get_score() <= 21)

    def test_player_hit(self):
        card = self.deck.deal()
        self.test_player.hit(card)
        self.assertEqual(len(self.test_player.get_hand()), 3)
