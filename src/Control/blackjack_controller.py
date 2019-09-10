from Control import config
from Model.deck import Deck
from Control.dealer import Dealer
from Control.player import BlackjackPlayer
import logging

logger = logging.getLogger("blackjack_controller.py")


class BlackjackController(object):
    def __init__(self):
        """Calculates and keeps track of the game, points, dec

        Args:
            TODO:

        Returns:
            TODO:

        Raises:
            TODO:
        """
        logger.debug("[Deck: current_deck] initialized in BlackjackController")
        self.current_deck = Deck()

        logger.debug("[Deck: current_deck] shuffled in BlackjackController")
        self.current_deck.shuffle()

        logger.debug("[Int: bet_amount] initialized in BlackjackController")
        self.bet_amount = 100

        logger.debug("[Bool: win] initialized to False in BlackjackController")
        self.win = False

        logger.debug(
            "[Int: default_balance] initialized to 10000 in BlackjackController"
        )
        self.default_balance = 10000

        logger.debug("[Bool: starting_blackjack] initialized in BlackjackController")
        self.starting_blackjack = False

        logger.debug(
            "[Player: current_player] initialized in BlackjackController, cards dealt & balance"
        )
        self.current_player = BlackjackPlayer(
            [self.current_deck.deal(), self.current_deck.deal()], self.default_balance
        )

        logger.debug(
            "[Dealer: current_dealer] initialized in BlackjackController, cards dealt & balance"
        )
        self.current_dealer = Dealer(
            [self.current_deck.deal(), self.current_deck.deal()], self.default_balance
        )

        logger.debug(
            "In BlackjackController.__init__, check if current_player has_blackjack()"
        )
        if self.current_player.has_blackjack():
            logger.info("Player has Blackjack")
            self.win = True
            self.current_player.update_balance(self.bet_amount, self.win)
            self.starting_blackjack = True
        logger.info("Player Doesn't have Blackjack")

    def get_players_balance(self):
        return self.current_player.get_balance()

    def get_players_hand(self):
        """Returns player's hand"""
        return self.current_player.get_hand()

    def get_blackjack(self):
        return self.starting_blackjack

    def get_new_player_hand(self):
        self.current_player.new_hand(
            [self.current_deck.deal(), self.current_deck.deal()]
        )

    def get_dealers_hand(self):
        """Returns dealer's hand"""
        return self.current_dealer.get_hand()

    def get_new_dealer_hand(self):
        self.current_dealer.new_hand(
            [self.current_deck.deal(), self.current_deck.deal()]
        )

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
