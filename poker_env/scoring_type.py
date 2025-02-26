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
    
    @staticmethod
    def tiebreak(hand1: List[Card], hand2: List[Card], score):
        """
        Assumes the two hands to be of the same scoring type
        Returns 1 if hand1 wins, 2 if hand2 wins, and 0 if there is a tie
        """
        if score == Scoring.StraightFlush:
            h1 = gr.is_straight_flush(hand1)
            h2 = gr.is_straight_flush(hand2)
        elif score == Scoring.FourOfAKind:
            h1 = gr.is_four_of_a_kind(hand1)
            h2 = gr.is_four_of_a_kind(hand2)
        elif score == Scoring.FullHouse:
            h1 = gr.is_full_house(hand1)
            h2 = gr.is_full_house(hand2)
        elif score == Scoring.Flush:
            h1 = gr.is_flush(hand1)
            h2 = gr.is_flush(hand2)
        elif score == Scoring.Straight:
            h1 = gr.is_straight(hand1)
            h2 = gr.is_straight(hand2)
        elif score == Scoring.ThreeOfAKind:
            h1 = gr.is_three_of_a_kind(hand1)
            h2 = gr.is_three_of_a_kind(hand2)
        elif score == Scoring.TwoPairs:
            h1 = gr.is_two_pair(hand1)
            h2 = gr.is_two_pair(hand2)
        elif score == Scoring.OnePair:
            h1 = gr.is_pair(hand1)
            h2 = gr.is_pair(hand2)
        elif score == Scoring.NoPair:
            h1 = gr.is_no_pair(hand1)
            h2 = gr.is_no_pair(hand2)
        else: raise ValueError("scoring type invalid")
        assert (len(h1) == len(h2) == 5), f"Lengths do not match up\nScoring type: {score}\nhand1: {hand1},\nh1: {h1},\nhand2: {hand2},\nh2: {h2}\n"


        for i in range(5):
            val1 = h1[i].face.value
            val2 = h2[i].face.value
            if  val1 == val2: continue
            else:
                if val1 > val2: return 1
                else: return 2
        return 0

