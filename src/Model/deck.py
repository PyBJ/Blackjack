from Model.card import Card
import random


class Deck(object):
    def __init__(self):
        """Creates a 4 Deck Shoe. suits * rank = 52"""
        self.deck = []
        decks = 6
        while decks > 0:
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    c = Card(rank, suit)
                    self.deck.append(c)
            decks = decks - 1
        # value representing a random card cut for the shoe
        # the lower number representing end of deck
        self.end_of_shoe = 13+random.randint(1, 52)
        self.deck_size = len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.deck_size = self.deck_size - 1
        print(self.deck_size)
        return self.deck.pop(0)

    def get_deck_size(self):
        return self.deck_size

    def get_end_of_shoe(self):
        return self.end_of_shoe

    def __str__(self):
        """Returns the string representation of the deck"""
        self.cards_in_the_deck = ""
        for card in self.deck:
            self.cards_in_the_deck = self.cards_in_the_deck + str(card) + "\n"
        return self.cards_in_the_deck

    def __len__(self):
        """Returns the number of cards in the deck"""
        return len(self.deck)
