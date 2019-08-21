from Control import config
from Model.deck import Deck
from Control.dealer import Dealer
from Control.player import Player


class BlackjackController(object):
    """"Calculates and keeps track of the game, points, deck"""

    def __init__(self):
        self.currentDeck = Deck()
        self.currentDeck.shuffle()
        self.bet_amount = 100
        self.win = False
        self.default_balance = 10000
        self.starting_blackjack = False

        """Deal player and dealer 2 cards each"""
        self.currentPlayer = Player([self.currentDeck.deal(), self.currentDeck.deal()], self.default_balance)
        self.currentDealer = Dealer([self.currentDeck.deal(), self.currentDeck.deal()], self.default_balance)
        
        if self.currentPlayer.has_blackjack():
            self.win = True
            self.currentPlayer.update_balance(self.bet_amount, self.win)
            self.starting_blackjack = True
        # Fif self.currentPlayer.has_blackjack:
        #     self.win = True
        #     self.currentPlayer.update_balance(self.bet_amount, self.win)
        #     self.player_wins()

    def get_players_balance(self):
        return self.currentPlayer.get_balance()

    def get_players_hand(self):
        """Returns player's hand"""
        return self.currentPlayer.get_hand()

    def get_blackjack(self):
        return self.starting_blackjack

    def get_new_player_hand(self):
        self.currentPlayer.new_hand([self.currentDeck.deal(), self.currentDeck.deal()])

    def get_dealers_hand(self):
        """Returns dealer's hand"""
        return self.currentDealer.get_hand()

    def get_new_dealer_hand(self):
        self.currentDealer.new_hand([self.currentDeck.deal(), self.currentDeck.deal()])

    def get_if_shoe_end(self):
        """Returns bool true if shoe card cut is drawn"""
        if self.currentDeck.get_deck_size() < self.currentDeck.get_end_of_shoe():
            return True
        else:
            return False

    def hit_player(self):
        card = self.currentDeck.deal()
        card.turn()
        self.currentPlayer.hit(card)
        # Returns tuple of the card and total points
        return card, self.currentPlayer.get_score()

    def hit_dealer(self):
        """Dealer only hits after the player stands"""
        self.currentDealer.show_first_card()
        player_score = self.currentPlayer.get_score()
        if player_score > 21:
            self.win = False
            self.currentPlayer.update_balance(self.bet_amount, self.win)
            return "You bust and lose!"
        else:
            self.currentDealer.hit(self.currentDeck)
            dealer_score = self.currentDealer.get_score()
            if player_score != dealer_score and self.currentPlayer.has_blackjack():
                # If the player has blackjack and it isn't a tie
                self.win = True
                self.currentPlayer.update_balance(self.bet_amount, self.win)
                config.blackjack = True
                return "Blackjack! You Win!"
            if dealer_score > 21:
                self.win = True
                self.currentPlayer.update_balance(self.bet_amount, self.win)
                return "Dealer busts! You win!"
            elif player_score > dealer_score:
                self.win = True
                self.currentPlayer.update_balance(self.bet_amount, self.win)
                return "You win!"
            elif player_score < dealer_score:
                self.win = False
                self.currentPlayer.update_balance(self.bet_amount, self.win)
                return "You lose!"
            elif player_score == dealer_score:
                if (
                    self.currentPlayer.has_blackjack()
                    and not self.currentDealer.has_blackjack()
                ):
                    self.win = True
                    self.currentPlayer.update_balance(self.bet_amount, self.win)
                    blackjack = True
                    return "BlackJack! You Win!"
                elif (
                    not self.currentPlayer.has_blackjack()
                    and self.currentDealer.has_blackjack()
                ):
                    self.win = False
                    self.currentPlayer.update_balance(self.bet_amount, self.win)
                    return "Dealer has BlackJack! You Lose!"
                else:
                    return "It's a Tie!"


