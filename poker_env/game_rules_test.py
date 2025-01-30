from card import Card, Face, Suit
from scoring_type import Scoring
from random import shuffle
from typing import List
import unittest
import game_rules as gr


class TestGameRules(unittest.TestCase):
    # NOTE: Testcase examples should always be input in Most Significant Card sort order
    # Suits are sorted SPADE > HEART > DIAMOND > CLUB

    PERMCOUNT = 5

    def n_perms(self, example: List[Card], amount: int):
        """
        Produces `amount` random permutations of the input cards\n
        Returns a List of Lists of Cards"""
        perms = []
        for _ in range(amount):
            perm = example[:]
            shuffle(perm)
            perms.append(perm)
        return(perms)



    def test_straight_flush(self):
        example1 = [
            # These cards make the Straight Flush
            Card(Face.TEN, Suit.HEARTS), 
            Card(Face.NINE, Suit.HEARTS), 
            Card(Face.EIGHT, Suit.HEARTS), 
            Card(Face.SEVEN, Suit.HEARTS),
            Card(Face.SIX, Suit.HEARTS),
            # These are random cards
            Card(Face.JACK, Suit.CLUBS),
            Card(Face.FOUR, Suit.DIAMONDS),
        ]
        example2 = [
            # These cards make the Straight Flush
            Card(Face.ACE, Suit.CLUBS), 
            Card(Face.KING, Suit.CLUBS), 
            Card(Face.QUEEN, Suit.CLUBS), 
            Card(Face.JACK, Suit.CLUBS),
            Card(Face.TEN, Suit.CLUBS),
            # These are random cards
            Card(Face.JACK, Suit.HEARTS),
            Card(Face.TEN, Suit.HEARTS),
        ]
        examples = [example1, example2]

        for example in examples:
            for perm in self.n_perms(example, self.PERMCOUNT):
                self.assertEqual(
                    Scoring.get_scoring_given_hand(perm),
                    Scoring.StraightFlush,
                )
                self.assertEqual(
                    gr.is_straight_flush(perm),
                    example[0:5],
                )

    def test_four_of_a_kind(self):
        example1 = [
            # These cards make Four of a Kind
            Card(Face.ACE, Suit.SPADES),
            Card(Face.ACE, Suit.HEARTS),
            Card(Face.ACE, Suit.DIAMONDS),
            Card(Face.ACE, Suit.CLUBS),
            # These are random cards
            Card(Face.TEN, Suit.SPADES),
            Card(Face.SIX, Suit.CLUBS),
            Card(Face.FOUR, Suit.DIAMONDS),
        ]
        example2 = [
            # These cards make Four of a Kind
            Card(Face.THREE, Suit.SPADES),
            Card(Face.THREE, Suit.HEARTS),
            Card(Face.THREE, Suit.DIAMONDS),
            Card(Face.THREE, Suit.CLUBS),
            # These are random cards
            Card(Face.ACE, Suit.SPADES),
            Card(Face.ACE, Suit.CLUBS),
            Card(Face.FOUR, Suit.DIAMONDS),
        ]
        examples = [example1, example2]

        for example in examples:
            for perm in self.n_perms(example, self.PERMCOUNT):
                self.assertEqual(
                    Scoring.get_scoring_given_hand(perm),
                    Scoring.FourOfAKind,
                )
                self.assertEqual(
                    gr.is_four_of_a_kind(perm),
                    example[0:5],
                )

    def test_full_house(self):
        example1 = [
            # These cards make a Full House
            Card(Face.EIGHT, Suit.SPADES),
            Card(Face.EIGHT, Suit.DIAMONDS),
            Card(Face.EIGHT, Suit.CLUBS),
            Card(Face.FOUR, Suit.HEARTS),
            Card(Face.FOUR, Suit.CLUBS),
            # These are random cards
            Card(Face.THREE, Suit.HEARTS),
            Card(Face.THREE, Suit.CLUBS),
        ]
        example2 = [
            # These cards make a Full House
            Card(Face.TWO, Suit.SPADES),
            Card(Face.TWO, Suit.HEARTS),
            Card(Face.TWO, Suit.CLUBS),
            Card(Face.ACE, Suit.DIAMONDS),
            Card(Face.ACE, Suit.CLUBS),
            # These are random cards
            Card(Face.JACK, Suit.HEARTS),
            Card(Face.FIVE, Suit.CLUBS),
        ]
        example3 = [
            # These cards make a Full House
            Card(Face.EIGHT, Suit.HEARTS),
            Card(Face.EIGHT, Suit.DIAMONDS),
            Card(Face.EIGHT, Suit.CLUBS),
            Card(Face.FIVE, Suit.HEARTS),
            Card(Face.FIVE, Suit.DIAMONDS),
            # These are random cards
            Card(Face.JACK, Suit.CLUBS),
            Card(Face.FIVE, Suit.CLUBS),
        ]
        examples = [example1, example2, example3]
        for example in examples:
            for perm in self.n_perms(example, self.PERMCOUNT):
                self.assertEqual(
                    Scoring.get_scoring_given_hand(perm),
                    Scoring.FullHouse,
                )
                self.assertEqual(
                    gr.is_full_house(perm),
                    example[0:5],
                )

    def test_flush(self):
        example1 = [
            # These cards make a Flush
            Card(Face.QUEEN, Suit.SPADES),
            Card(Face.JACK, Suit.SPADES),
            Card(Face.TEN, Suit.SPADES),
            Card(Face.SEVEN, Suit.SPADES),
            Card(Face.THREE, Suit.SPADES),
            # These are random cards
            Card(Face.SEVEN, Suit.HEARTS),
            Card(Face.TWO, Suit.SPADES),
        ]
        example2 = [
            # These cards make a Flush
            Card(Face.QUEEN, Suit.SPADES),
            Card(Face.JACK, Suit.SPADES),
            Card(Face.TEN, Suit.SPADES),
            Card(Face.SEVEN, Suit.SPADES),
            Card(Face.TWO, Suit.SPADES),
            # These are random cards
            Card(Face.KING, Suit.HEARTS),
            Card(Face.NINE, Suit.HEARTS),
        ]
        examples = [example1, example2]
        
        for example in examples:
            for perm in self.n_perms(example, self.PERMCOUNT):
                self.assertEqual(
                    Scoring.get_scoring_given_hand(perm),
                    Scoring.Flush,
                )
                self.assertEqual(
                    gr.is_flush(perm),
                    example[0:5],
                )

    def test_straight(self):
        example1 = [
            # These cards make the Straight
            Card(Face.NINE, Suit.HEARTS),
            Card(Face.EIGHT, Suit.SPADES),
            Card(Face.SEVEN, Suit.CLUBS),
            Card(Face.SIX, Suit.HEARTS),
            Card(Face.FIVE, Suit.DIAMONDS),
            # These are random cards
            Card(Face.JACK, Suit.HEARTS),
            Card(Face.FOUR, Suit.DIAMONDS),
        ]
        example2 = [
            # These cards make the Straight
            Card(Face.ACE, Suit.HEARTS),
            Card(Face.KING, Suit.SPADES),
            Card(Face.QUEEN, Suit.CLUBS),
            Card(Face.JACK, Suit.HEARTS),
            Card(Face.TEN, Suit.DIAMONDS),
            # These are random cards
            Card(Face.KING, Suit.HEARTS),
            Card(Face.FOUR, Suit.DIAMONDS),
        ]
        example3 = [
            # These cards make the Straight
            Card(Face.FIVE, Suit.HEARTS),
            Card(Face.FOUR, Suit.SPADES),
            Card(Face.THREE, Suit.CLUBS),
            Card(Face.TWO, Suit.HEARTS),
            Card(Face.ACE, Suit.DIAMONDS),
            # These are random cards
            Card(Face.FOUR, Suit.HEARTS),
            Card(Face.FOUR, Suit.DIAMONDS),
        ]
        examples = [example1, example2, example3]
        
        for example in examples:
            for perm in self.n_perms(example, self.PERMCOUNT):
                self.assertEqual(
                    Scoring.get_scoring_given_hand(perm),
                    Scoring.Straight,
                )
                self.assertEqual(
                    gr.is_straight(perm),
                    example[0:5],
                )

    def test_three_of_a_kind(self):
        example1 = [
            # These cards make Three of a Kind
            Card(Face.JACK, Suit.HEARTS),
            Card(Face.JACK, Suit.DIAMONDS),
            Card(Face.JACK, Suit.CLUBS),
            # These are random cards
            Card(Face.SEVEN, Suit.SPADES),
            Card(Face.SIX, Suit.DIAMONDS),
            Card(Face.FOUR, Suit.HEARTS),
            Card(Face.TWO, Suit.DIAMONDS),
        ]
        example2 = [
            # These cards make Three of a Kind
            Card(Face.JACK, Suit.HEARTS),
            Card(Face.JACK, Suit.DIAMONDS),
            Card(Face.JACK, Suit.CLUBS),
            # These are random cards
            Card(Face.ACE, Suit.SPADES),
            Card(Face.KING, Suit.DIAMONDS),
            Card(Face.QUEEN, Suit.HEARTS),
            Card(Face.TWO, Suit.DIAMONDS),
        ]
        examples = [example1, example2]
        
        for example in examples:
            for perm in self.n_perms(example, self.PERMCOUNT):
                self.assertEqual(
                    Scoring.get_scoring_given_hand(perm),
                    Scoring.ThreeOfAKind,
                )
                self.assertEqual(
                    gr.is_three_of_a_kind(perm),
                    example[0:5],
                )

    def test_two_pair(self):
        example1 = [
            # These cards make the Two Pair
            Card(Face.QUEEN, Suit.HEARTS),
            Card(Face.QUEEN, Suit.DIAMONDS),
            Card(Face.JACK, Suit.DIAMONDS),
            Card(Face.JACK, Suit.CLUBS),
            # These are random cards
            Card(Face.ACE, Suit.SPADES),
            Card(Face.SIX, Suit.SPADES),
            Card(Face.FOUR, Suit.SPADES),
        ]
        examples = [example1]
        
        for example in examples:
            for perm in self.n_perms(example, self.PERMCOUNT):
                self.assertEqual(
                    Scoring.get_scoring_given_hand(perm),
                    Scoring.TwoPairs,
                )
                self.assertEqual(
                    gr.is_two_pair(perm),
                    example[0:5],
                )
    
    def test_one_pair(self):
        example1 = [
            # These cards make One Pair
            Card(Face.TEN, Suit.HEARTS),
            Card(Face.TEN, Suit.DIAMONDS),
            # These are random cards
            Card(Face.QUEEN, Suit.CLUBS),
            Card(Face.JACK, Suit.DIAMONDS),
            Card(Face.SEVEN, Suit.SPADES),
            Card(Face.FOUR, Suit.CLUBS),
            Card(Face.TWO, Suit.SPADES),
        ]
        examples = [example1]
        
        for example in examples:
            for perm in self.n_perms(example, self.PERMCOUNT):
                self.assertEqual(
                    Scoring.get_scoring_given_hand(perm),
                    Scoring.OnePair,
                )
                self.assertEqual(
                    gr.is_pair(perm),
                    example[0:5],
                )

    def test_no_pairs(self):
        example1 = [
            # This is the High Card
            Card(Face.ACE, Suit.SPADES),
            # These are random cards
            Card(Face.QUEEN, Suit.DIAMONDS),
            Card(Face.JACK, Suit.HEARTS),
            Card(Face.TEN, Suit.CLUBS),
            Card(Face.EIGHT, Suit.DIAMONDS),
            Card(Face.SEVEN, Suit.SPADES),
            Card(Face.FOUR, Suit.SPADES),
        ]
        examples = [example1]
        
        for example in examples:
            for perm in self.n_perms(example, self.PERMCOUNT):
                self.assertEqual(
                    Scoring.get_scoring_given_hand(perm),
                    Scoring.NoPair,
                )
                self.assertEqual(
                    gr.is_no_pair(perm),
                    example[0:5],
                )

    def test_scoring_equality(self):
        self.assertEqual(
            Scoring.Flush,
            Scoring.Flush,
        )
        self.assertEqual(
            Scoring.Straight,
            Scoring.Straight,
        )
        self.assertNotEqual(
            Scoring.Flush,
            Scoring.StraightFlush,
        )
        self.assertNotEqual(
            Scoring.TwoPairs,
            Scoring.NoPair,
        )

if __name__ == '__main__':
    unittest.main()
