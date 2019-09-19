from Control.player import BlackjackPlayer


class Dealer(BlackjackPlayer):
    def __init__(self, cards, balance):
        """
        Args:
            cards:
            balance:
        """
        BlackjackPlayer.__init__(self, cards, balance)
        self.show_one_card = True
        self.hand[0].turn()

    def hit(self, deck):
        """Dealers strategy is to only hit if it has less than 17 And the rule
        requires the dealer to draw at least 16

        Args:
            deck:
        """
        while self.get_score() < 17:
            card = deck.deal()
            card.turn()
            self.hand.append(card)

    def show_first_card(self):
        self.show_one_card = False
        self.hand[0].turn()

    def __str__(self):
        """Return just one card if not hit yet."""
        if self.show_one_card:
            return str(self.hand[0])
        else:
            return BlackjackPlayer.__str__(self)

    def new_hand(self, cards):
        """
        Args:
            cards:
        """
        self.__init__(cards, self.balance)
