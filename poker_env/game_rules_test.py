from card import Card, Face, Suit
from scoring_type import Scoring
from itertools import permutations
import unittest


class TestGameRules(unittest.TestCase):
    def test_straight_flush(self):
        example1 = [
            Card(Face.TEN, Suit.HEARTS), 
            Card(Face.NINE, Suit.HEARTS), 
            Card(Face.EIGHT, Suit.HEARTS), 
            Card(Face.SEVEN, Suit.HEARTS),
            Card(Face.SIX, Suit.HEARTS),
        ]

        self.assertEqual(Scoring.get_scoring_given_hand(
                example1
            ),
            Scoring.StraightFlush
        )
        self.assertEqual(Scoring.get_scoring_given_hand(
                example1[::-1]
            ),
            Scoring.StraightFlush
        )

        example2 = [
            Card(Face.ACE, Suit.CLUBS), 
            Card(Face.KING, Suit.CLUBS), 
            Card(Face.QUEEN, Suit.CLUBS), 
            Card(Face.JACK, Suit.CLUBS),
            Card(Face.TEN, Suit.CLUBS),
        ]

        self.assertEqual(Scoring.get_scoring_given_hand(
                example2
            ),
            Scoring.StraightFlush
        )
        self.assertEqual(Scoring.get_scoring_given_hand(
                example2[::-1]
            ),
            Scoring.StraightFlush
        )

    def test_four_of_a_kind(self):
        example1 = [
            Card(Face.ACE, Suit.SPADES),
            Card(Face.ACE, Suit.CLUBS),
            Card(Face.ACE, Suit.HEARTS),
            Card(Face.ACE, Suit.DIAMONDS),
            Card(Face.TEN, Suit.SPADES),
        ]
        example2 = [
            Card(Face.THREE, Suit.SPADES),
            Card(Face.THREE, Suit.CLUBS),
            Card(Face.THREE, Suit.HEARTS),
            Card(Face.THREE, Suit.DIAMONDS),
            Card(Face.ACE, Suit.SPADES),
        ]
        examples = [example1, example2]

        for example in examples:
            for i in list(permutations(example1)):
                self.assertEqual(
                    Scoring.get_scoring_given_hand(i),
                    Scoring.FourOfAKind,
                )

    def test_full_house(self):
        example1 = [
            Card(Face.EIGHT, Suit.SPADES),
            Card(Face.EIGHT, Suit.CLUBS),
            Card(Face.EIGHT, Suit.DIAMONDS),
            Card(Face.FOUR, Suit.CLUBS),
            Card(Face.FOUR, Suit.HEARTS),
        ]

        self.assertEqual(
            Scoring.get_scoring_given_hand(example1),
            Scoring.FullHouse
        )

    def test_flush(self):
        example1 = [
            Card(Face.QUEEN, Suit.SPADES),
            Card(Face.TEN, Suit.SPADES),
            Card(Face.JACK, Suit.SPADES),
            Card(Face.SEVEN, Suit.SPADES),
            Card(Face.TWO, Suit.SPADES),
        ]

        for i in list(permutations(example1)):
            self.assertEqual(
                Scoring.get_scoring_given_hand(i),
                Scoring.Flush,
            )

    def test_straight(self):
        example1 = [
            Card(Face.NINE, Suit.HEARTS),
            Card(Face.EIGHT, Suit.SPADES),
            Card(Face.SEVEN, Suit.CLUBS),
            Card(Face.SIX, Suit.HEARTS),
            Card(Face.FIVE, Suit.DIAMONDS),
        ]

        self.assertEqual(Scoring.get_scoring_given_hand(
                example1
            ),
            Scoring.Straight
        )
        self.assertEqual(Scoring.get_scoring_given_hand(
                example1[::-1]
            ),
            Scoring.Straight
        )

    def test_three_of_a_kind(self):
        example1 = [
            Card(Face.JACK, Suit.DIAMONDS),
            Card(Face.JACK, Suit.HEARTS),
            Card(Face.JACK, Suit.CLUBS),
            Card(Face.SEVEN, Suit.SPADES),
            Card(Face.FOUR, Suit.DIAMONDS),
        ]

        for i in list(permutations(example1)):
            self.assertEqual(
                Scoring.get_scoring_given_hand(i),
                Scoring.ThreeOfAKind,
            )

    def test_two_pair(self):
        example1 = [
            Card(Face.QUEEN, Suit.DIAMONDS),
            Card(Face.QUEEN, Suit.HEARTS),
            Card(Face.JACK, Suit.CLUBS),
            Card(Face.JACK, Suit.DIAMONDS),
            Card(Face.SEVEN, Suit.SPADES),
        ]

        for i in list(permutations(example1)):
            self.assertEqual(
                Scoring.get_scoring_given_hand(i),
                Scoring.TwoPairs,
            )
    
    def test_one_pair(self):
        example1 = [
            Card(Face.TEN, Suit.DIAMONDS),
            Card(Face.TEN, Suit.HEARTS),
            Card(Face.JACK, Suit.CLUBS),
            Card(Face.QUEEN, Suit.DIAMONDS),
            Card(Face.SEVEN, Suit.SPADES),
        ]

        for i in list(permutations(example1)):
            self.assertEqual(
                Scoring.get_scoring_given_hand(i),
                Scoring.OnePair,
            )

    def test_no_pairs(self):
        example1 = [
            Card(Face.NINE, Suit.DIAMONDS),
            Card(Face.TEN, Suit.HEARTS),
            Card(Face.JACK, Suit.CLUBS),
            Card(Face.QUEEN, Suit.DIAMONDS),
            Card(Face.SEVEN, Suit.SPADES),
        ]

        for i in list(permutations(example1)):
            self.assertEqual(
                Scoring.get_scoring_given_hand(i),
                Scoring.NoPair,
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
