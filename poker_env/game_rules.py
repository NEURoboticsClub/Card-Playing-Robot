# https://bicyclecards.com/how-to-play/basics-of-poker

from enum import Enum
from card import Card
from collections import Counter
from typing import List


def is_straight_flush(hand: List[Card]):
    return is_flush(hand) and is_straight(hand)

def is_flush(hand: List[Card]):
    #dictionary of unique suits
    suits = {i.suit.value for i in hand}
    #if there is more than one suit, return false
    return len(suits) == 1

def is_straight(hand: List[Card]):
    values = [i.face.value for i in hand]

    # checks if is in ascending order
    ascending = sorted(values) == list(range(min(values), max(values) + 1))
    # checks if in descending order
    descending = sorted(values, reverse=True) == list(range(max(values), min(values) - 1, -1))

    return ascending or descending

def is_royal_flush(hand: List[Card]):
    # checks if flush
    if not is_flush(hand):
        return False
    values = sorted_hand = sorted(hand, key=lambda card: card.face.value)
    # checks if values are royal flush
    royal_values = list(1, 10, 11, 12, 13)
    for i in values:
        if (sorted[i] != values[i]):
            return False
    return True

def is_four_of_a_kind(hand: List[Card]):
    count = {}
    for i in hand:
        if i.face not in count:
            count[i.face] = 1
        else:
            count[i.face] += 1
    
    # checks if there are at least 4 of the same face
    return any(i >= 4 for i in count.values())

def is_full_house(hand: List[Card]):
    #dictionary of unique suits and faces
    faces = {card.face.value for card in hand}
    #if there is more than one face, return false
    if len(faces) != 2:
        return False
    
    return True
    
def is_three_of_a_kind(hand: List[Card]):
    # Dictionary to store the frequency of each card rank
    rank_count = {}

    # Count the occurrences of each rank (face value)
    for card in hand:
        if card.face.value in rank_count:
            rank_count[card.face.value] += 1
        else:
            rank_count[card.face.value] = 1

    # Full House should have exactly two distinct ranks, one with 3 occurrences and one with 2
    counts = list(rank_count.values())
    
    return sorted(counts) == [1, 1, 3]

def rank_frequency(hand: List[Card]):
    # Dictionary to store the frequency of each card rank
    rank_count = {}

    # Count the occurrences of each rank (face value)
    for card in hand:
        if card.face.value in rank_count:
            rank_count[card.face.value] += 1
        else:
            rank_count[card.face.value] = 1

    # Full House should have exactly two distinct ranks, one with 3 occurrences and one with 2
    counts = list(rank_count.values())
    return counts

def is_two_pair(hand: List[Card]):
    freq = rank_frequency(hand)
    return sorted(freq) == [1, 2, 2]

def is_pair(hand: List[Card]):
    freq = rank_frequency(hand)
    return sorted(freq) == [1, 1, 1, 2]
