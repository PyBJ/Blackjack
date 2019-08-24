import unittest

from Model.deck import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.Deck = Deck()
        self.EmptyDeck = Deck()
        self.EmptyDeck.deck = []

    def test_number_of_cards(self):
        self.assertEqual(self.Deck.get_deck_size(), 312)

    @unittest.expectedFailure
    def test_not_equal_cards(self):
        self.assertEqual(self.Deck.get_deck_size(), 52)

    # tests deal function
    def test_end_of_deck(self):
        # Empty python lists eval to False
        while self.Deck.deck:
            self.Deck.deal()
        self.assertFalse(self.Deck.deck)


if __name__ == "__main__":
    unittest.main()
