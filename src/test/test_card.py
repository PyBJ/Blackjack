import unittest

from Model.card import Card


class DeckTest(unittest.TestCase):
    def setUp(self):
        self.SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")
        self.RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
        self.Card = Card(self.RANKS, self.SUITS)
        self.Card.turn()
        self.filename = "Test.txt"

    def test_turn(self):
        self.assertEqual(self.Card.faceUp, True)

    @unittest.expectedFailure
    def test_not_turn(self):
        self.assertEqual(self.Card.faceUp, False)


if __name__ == "__main__":
    unittest.main()