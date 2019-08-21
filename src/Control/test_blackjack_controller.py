import unittest

from Control.blackjack_controller import BlackjackController
from Control import player, dealer
from Control import config

from Model.deck import Deck

class BlackJackControllerTest(unittest.TestCase):
    def setUp(self):
        self.bjc = BlackjackController()
        self.currentDeck = self.bjc.currentDeck
        self.currentDeck.shuffle()
        self.bet_amount = 100
        self.win = False
        self.default_balance = 10000
        self.starting_blackjack = False
        self.test_player = self.bjc.currentPlayer
        self.test_dealer = self.bjc.currentDealer


    def test_hit_dealer(self):
        """

        testing that the return of hit_dealer is among these return string statements


        1 player_bust test
        2 dealer_bust
        3 player BLACKJACK WIN
        4 player BLACKJACK WIN when both equal 21 but dealer is not blackjack
        5 player  win
        6 player  loses, dealer wins.
        7 Dealer wins with blackjack
        8 tie game
        """
        print("Hit_dealer Return value:", self.bjc.hit_dealer())
        print("Player Score : ", self.test_player.get_score())
        print("Dealer Score:", self.test_dealer.get_score())

        if self.test_player.get_score() > 21:
            self.assertEqual(self.bjc.hit_dealer(), "You bust and lose!", "player Bust  check")
        elif self.test_dealer.get_score() > 21:
            self.assertEqual(self.bjc.hit_dealer(), "Dealer busts! You win!", "Dealer Bust check")
        elif (self.test_player.get_score() != self.test_dealer.get_score()) and self.test_player.has_blackjack():
            self.assertEqual(self.bjc.hit_dealer(), "Blackjack! You Win!", "win condition check player BJ")
        elif (self.test_player.get_score() == self.test_dealer.get_score()) and self.test_player.has_blackjack() and not self.test_dealer.has_blackjack():
            self.assertEqual(self.bjc.hit_dealer(), "BlackJack! You Win!", "player has bj and beats dealers 21 not bj")
        elif self.test_player.get_score() > self.test_dealer.get_score() and not self.test_player.get_score() > 21:
            self.assertEqual(self.bjc.hit_dealer(), "You win!", "Player wins higher score than dealer")
        elif self.test_dealer.get_score() > self.test_player.get_score() and not self.test_dealer.get_score() > 21:
            self.assertEqual(self.bjc.hit_dealer(), "You lose!", "Player loses Dealer had higher score")
        elif self.test_player.get_score()== self.test_dealer.get_score() and self.test_dealer.has_blackjack() and not self.test_player.has_blackjack():
            self.assertEqual(self.bjc.hit_dealer(),"Dealer has BlackJack! You Lose!", "Dealer had BJ player didnt LOSS")
        else:

            self.assertEqual(self.bjc.hit_dealer(), "It's a Tie!", "tie game check")












