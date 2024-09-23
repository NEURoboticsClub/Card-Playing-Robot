# https://bicyclecards.com/how-to-play/basics-of-poker

from enum import Enum
from card import Card


def is_straight_flush(hand: set[Card]):
    sorted_hand = sorted(hand1, key=lambda card: card.face.value)
    list(range(min(l, key=lambda card: card.face.value), max(l)+1))


# def compare_hand(hand1: set[Card], hand2: set[Card]):
#     if len(hand1) != 4:
#         raise ValueError('Hand must be length 4')
#     if len(hand2) != 4:
#         raise ValueError('Hand must be length 4')

#     # check for straight flush
#     if sorted(hand1, key=lambda card: card.face.value) == list(range(min(l), max(l)+1))
