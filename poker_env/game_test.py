from card import Card, Face, Suit
from scoring_type import Scoring
from card import Card
from card import Face
from card import Suit
from scoring_type import Scoring
from enum import Enum
from typing import List
from game import PokerGame, PokerAction, Player
import random
from itertools import permutations
import unittest

class TestGame(unittest.TestCase):
    def test_shuffle_deck_full(self):
        spade_list = [Card(Face.TWO,Suit.SPADES)
                      ,Card(Face.THREE,Suit.SPADES)
                      ,Card(Face.FOUR,Suit.SPADES)
                      ,Card(Face.FIVE,Suit.SPADES)
                      ,Card(Face.SIX,Suit.SPADES)
                      ,Card(Face.SEVEN,Suit.SPADES)
                      ,Card(Face.EIGHT,Suit.SPADES)
                      ,Card(Face.NINE,Suit.SPADES)
                      ,Card(Face.TEN,Suit.SPADES)
                      ,Card(Face.JACK,Suit.SPADES)
                      ,Card(Face.QUEEN,Suit.SPADES)
                      ,Card(Face.KING,Suit.SPADES)
                      ,Card(Face.ACE,Suit.SPADES)]
        heart_list = [Card(Face.TWO,Suit.HEARTS)
                      ,Card(Face.THREE,Suit.HEARTS)
                      ,Card(Face.FOUR,Suit.HEARTS)
                      ,Card(Face.FIVE,Suit.HEARTS)
                      ,Card(Face.SIX,Suit.HEARTS)
                      ,Card(Face.SEVEN,Suit.HEARTS)
                      ,Card(Face.EIGHT,Suit.HEARTS)
                      ,Card(Face.NINE,Suit.HEARTS)
                      ,Card(Face.TEN,Suit.HEARTS)
                      ,Card(Face.JACK,Suit.HEARTS)
                      ,Card(Face.QUEEN,Suit.HEARTS)
                      ,Card(Face.KING,Suit.HEARTS)
                      ,Card(Face.ACE,Suit.HEARTS)]
        club_list = [Card(Face.TWO,Suit.CLUBS)
                      ,Card(Face.THREE,Suit.CLUBS)
                      ,Card(Face.FOUR,Suit.CLUBS)
                      ,Card(Face.FIVE,Suit.CLUBS)
                      ,Card(Face.SIX,Suit.CLUBS)
                      ,Card(Face.SEVEN,Suit.CLUBS)
                      ,Card(Face.EIGHT,Suit.CLUBS)
                      ,Card(Face.NINE,Suit.CLUBS)
                      ,Card(Face.TEN,Suit.CLUBS)
                      ,Card(Face.JACK,Suit.CLUBS)
                      ,Card(Face.QUEEN,Suit.CLUBS)
                      ,Card(Face.KING,Suit.CLUBS)
                      ,Card(Face.ACE,Suit.CLUBS)]
        diamond_list = [Card(Face.TWO,Suit.DIAMONDS)
                      ,Card(Face.THREE,Suit.DIAMONDS)
                      ,Card(Face.FOUR,Suit.DIAMONDS)
                      ,Card(Face.FIVE,Suit.DIAMONDS)
                      ,Card(Face.SIX,Suit.DIAMONDS)
                      ,Card(Face.SEVEN,Suit.DIAMONDS)
                      ,Card(Face.EIGHT,Suit.DIAMONDS)
                      ,Card(Face.NINE,Suit.DIAMONDS)
                      ,Card(Face.TEN,Suit.DIAMONDS)
                      ,Card(Face.JACK,Suit.DIAMONDS)
                      ,Card(Face.QUEEN,Suit.DIAMONDS)
                      ,Card(Face.KING,Suit.DIAMONDS)
                      ,Card(Face.ACE,Suit.DIAMONDS)]
        
        def suitChecker(currentSUIT,suitList):
            suitCounter = 0
            for i in suitList:
                if i.suit == currentSUIT:suitCounter += 1
            return suitCounter
        testPokerGame = PokerGame([])
        testDeck = testPokerGame.shuffle_deck_full()


        self.assertEqual(len(testDeck),52)

        self.assertEqual(suitChecker(Suit.SPADES,spade_list),13)

        # for i in testDeck:
        #     print(type(i.suit))

        self.assertEqual(suitChecker(Suit.CLUBS,testDeck),13)

        self.assertEqual(set(spade_list).issubset(set(testDeck)),True)

        self.assertEqual(set(heart_list).issubset(set(testDeck)),True)

        self.assertEqual(set(club_list).issubset(set(testDeck)),True)

        self.assertEqual(set(diamond_list).issubset(set(testDeck)),True)

    def test_shuffle_deck_current(self):
        testPokerGame = PokerGame([])
        testDeck = testPokerGame.shuffle_deck_full()
        

        testDeck.pop(0)
        testDeck.pop(0)
        testDeck.pop(0)
        testDeck2 = testPokerGame.shuffle_deck_current(testDeck)

        self.assertEqual(49,len(testDeck2))

        
if __name__ == '__main__':
    unittest.main()