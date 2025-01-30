from enum import Enum
from card import Card
from typing import List
import game_rules as gr


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
        if gr.is_straight_flush(hand):
            return Scoring.StraightFlush
        if gr.is_four_of_a_kind(hand):
            return Scoring.FourOfAKind
        if gr.is_full_house(hand):
            return Scoring.FullHouse
        if gr.is_flush(hand):
            return Scoring.Flush
        if gr.is_straight(hand):
            return Scoring.Straight
        if gr.is_three_of_a_kind(hand):
            return Scoring.ThreeOfAKind
        if gr.is_two_pair(hand):
            return Scoring.TwoPairs
        if gr.is_pair(hand):
            return Scoring.OnePair
        return Scoring.NoPair
