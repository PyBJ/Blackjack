from Control import config
from Model.deck import Deck
from Control.dealer import Dealer
from Control.player import Player


class BlackjackController(object):
    """Calculates and keeps track of the game, points, dec"""

    def __init__(self):
        self.current_deck = Deck()
        self.current_deck.shuffle()
        self.bet_amount = 100
        self.win = False
        self.default_balance = 10000
        self.starting_blackjack = False

        """Deal player and dealer 2 cards each"""
        self.current_player = Player([self.current_deck.deal(), self.current_deck.deal()], self.default_balance)
        self.current_dealer = Dealer([self.current_deck.deal(), self.current_deck.deal()], self.default_balance)
        
        if self.current_player.has_blackjack():
            self.win = True
            self.current_player.update_balance(self.bet_amount, self.win)
            self.starting_blackjack = True
        # Fif self.current_player.has_blackjack:
        #     self.win = True
        #     self.current_player.update_balance(self.bet_amount, self.win)
        #     self.player_wins()

    def get_players_balance(self):
        return self.current_player.get_balance()

    def get_players_hand(self):
        """Returns player's hand"""
        return self.current_player.get_hand()

    def get_blackjack(self):
        return self.starting_blackjack

    def get_new_player_hand(self):
        self.current_player.new_hand([self.current_deck.deal(), self.current_deck.deal()])

    def get_dealers_hand(self):
        """Returns dealer's hand"""
        return self.current_dealer.get_hand()

    def get_new_dealer_hand(self):
        self.current_dealer.new_hand([self.current_deck.deal(), self.current_deck.deal()])

    def get_if_shoe_end(self):
        """Returns bool true if shoe card cut is drawn"""
        if self.current_deck.get_deck_size() < self.current_deck.get_end_of_shoe():
            return True
        else:
            return False

    def hit_player(self):
        card = self.current_deck.deal()
        card.turn()
        self.current_player.hit(card)
        # Returns tuple of the card and total points
        return card, self.current_player.get_score()

    def hit_dealer(self):
        """Dealer only hits after the player stands"""
        self.current_dealer.show_first_card()
        player_score = self.current_player.get_score()
        if player_score > 21:
            self.win = False
            self.current_player.update_balance(self.bet_amount, self.win)
            return "You bust and lose!"
        else:
            self.current_dealer.hit(self.current_deck)
            dealer_score = self.current_dealer.get_score()
            if player_score != dealer_score and self.current_player.has_blackjack():
                # If the player has blackjack and it isn't a tie
                self.win = True
                self.current_player.update_balance(self.bet_amount, self.win)
                config.blackjack = True
                return "Blackjack! You Win!"
            if dealer_score > 21:
                self.win = True
                self.current_player.update_balance(self.bet_amount, self.win)
                return "Dealer busts! You win!"
            elif player_score > dealer_score:
                self.win = True
                self.current_player.update_balance(self.bet_amount, self.win)
                return "You win!"
            elif player_score < dealer_score:
                self.win = False
                self.current_player.update_balance(self.bet_amount, self.win)
                return "You lose!"
            elif player_score == dealer_score:
                if (
                    self.current_player.has_blackjack()
                    and not self.current_dealer.has_blackjack()
                ):
                    self.win = True
                    self.current_player.update_balance(self.bet_amount, self.win)
                    blackjack = True
                    return "BlackJack! You Win!"
                elif (
                    not self.current_player.has_blackjack()
                    and self.current_dealer.has_blackjack()
                ):
                    self.win = False
                    self.current_player.update_balance(self.bet_amount, self.win)
                    return "Dealer has BlackJack! You Lose!"
                else:
                    return "It's a Tie!"


