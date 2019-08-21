"""File: card.py"""
import os


class Card:
    """This Class Card creates a card object with suit and rank"""

    SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    BACK_OF_CARD_FILE_NAME = os.path.join(THIS_FOLDER, "DECK/b.png")

    def __init__(self, rank, suit):
        """Creates a card with given rank and suit"""

        self.rank = rank
        self.suit = suit
        """The images for cards are saved in path res/DECK/
        For example: Ace of clubs is in res/DECK/1c.gif
        A number for rank, and a lower case initial for suits"""

        self.filename = "DECK/" + str(rank) + suit[0].lower() + ".gif"
        self.my_file = os.path.join(Card.THIS_FOLDER, self.filename)

        self.faceUp = False

    def __str__(self):
        """Returns a string representation of a card"""
        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = self.rank
        return str(rank) + " of " + self.suit

    def get_filename(self):
        """Only lets you get the file name if the card is face up"""
        if self.faceUp:
            return self.my_file
        else:
            return Card.BACK_OF_CARD_FILE_NAME

    def turn(self):
        """Turns the card"""
        self.faceUp = not self.faceUp
