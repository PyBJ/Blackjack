class Player:
    pass


class BlackjackPlayer(Player):

    def __init__(self, cards, balance):
        """
        Args:
            cards:
            balance:
        """
        self.hand = cards
        self.balance = balance
        self.bet = 100
        """Turns each card faceUp"""
        for card in self.hand:
            card.turn()

    def __str__(self):
        """Returns string rep of cards and points."""
        result = ", ".join(map(str, self.hand))
        result += "\n  " + str(self.get_score()) + " points"
        return result

    def hit(self, card):
        """Adds a card to the hand

        Args:
            card:
        """
        self.hand.append(card)

    def get_balance(self):
        return self.balance

    def subtract_ante(self):
        self.balance = self.balance - self.bet

    def update_balance(self, bet_amount, win):
        """
        Args:
            bet_amount:
            win:
        """
        if win:
            self.balance = self.balance + bet_amount * 2
        # else:
            # self.balance = self.balance - bet_amount

    def get_score(self) -> int:
        score = 0
        for card in self.hand:
            if card.rank > 9:
                score += 10
            elif card.rank == 1:
                score += 11
            else:
                score += card.rank

        """Checks if the count is > 21 with A = 11, if so, it deducts 10 to make A = 1"""
        for card in self.hand:
            if score <= 21:
                break
            elif card.rank == 1:
                score -= 10
        return score

    def has_blackjack(self):
        """Returns True if dealt cards (2) makes the score 21: Which means the
        player has Blackjack
        """
        return len(self.hand) == 2 and self.get_score() == 21

    def get_hand(self):
        return self.hand

    def new_hand(self, cards):
        """
        Args:
            cards:
        """
        self.hand = cards
        for card in self.hand:
            card.turn()
