from Model.deck import Deck


class Hand:
    """
    Attributes:
        _cards: list BlackjackCard
        name: str
    """

    def __init__(self, name="", *cards):
        """
        Args:
            name:
            *cards:
        """
        self._cards = list(cards)
        self.name = name


class BlackjackHand(Hand):
    """
    Attributes:
        _cards: list BlackjackCard
        name: str
    """

    def __init__(self, name="", *cards):
        super().__init__(name, *cards)

    def hard_total(self) -> int:
        return sum(c.hard_score for c in self._cards)

    def soft_total(self) -> int:
        return sum(c.soft_score for c in self._cards)

    def bust(self) -> bool:
        if self.hard_total() > 21 and self.soft_total() > 21:
            return True
        else:
            return False

    def blackjack(self) -> bool:
        if self.hard_total() == 21 or self.soft_total() == 21:
            return True
        else:
            return False

    def hit(self, card):
        self._cards.append(card)
        return self._cards

    def size(self) -> int:
        return len(self._cards)

    def get_cards(self):
        return self._cards[:]

    def __str__(self) -> str:
        hand_list = [str(card) for card in self._cards]
        return str(", ".join(hand_list))
