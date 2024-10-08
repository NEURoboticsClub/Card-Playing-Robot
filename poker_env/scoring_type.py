from enum import Enum
from card import Card
from game_rules import is_straight_flush, is_four_of_a_kind, is_full_house
from game_rules import is_flush, is_straight, is_three_of_a_kind, is_two_pair
from game_rules import is_pair
from typing import List


class Scoring(Enum):
    StraightFlush = 1
    FourOfAKind = 2
    FullHouse = 3
    Flush = 4
    Straight = 5
    ThreeOfAKind = 6
    TwoPairs = 7
    OnePair = 8
    NoPair = 9

    def __hash__(self):
        return hash(self)

    @staticmethod
    def get_scoring_given_hand(hand: List[Card]):
        if is_straight_flush(hand):
            return Scoring.StraightFlush
        if is_four_of_a_kind(hand):
            return Scoring.FourOfAKind
        if is_full_house(hand):
            return Scoring.FullHouse
        if is_flush(hand):
            return Scoring.Flush
        if is_straight(hand):
            return Scoring.Straight
        if is_three_of_a_kind(hand):
            return Scoring.ThreeOfAKind
        if is_two_pair(hand):
            return Scoring.TwoPairs
        if is_pair(hand):
            return Scoring.OnePair
        return Scoring.NoPair
