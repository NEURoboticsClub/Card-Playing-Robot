# https://bicyclecards.com/how-to-play/basics-of-poker

from enum import Enum
from card import Card



def is_straight_flush(hand: set[Card]):
    return is_flush(hand) & is_straight(hand)

def is_flush(hand: set[Card]):
    #dictionary of unique suits
    suits = {card.suit for card in hand}
    #if there is more than one suit, return false
    if len(suits) > 1:
        return False

def is_straight(hand: set[Card]):
    #list of sorted cards by their value
    sorted_hand = sorted(hand, key=lambda card: card.face.value)
    #the correct, consecutive sequence for a straight flush 
    values = list(range(sorted_hand[0], sorted_hand[len(sorted_hand) - 1]))
    for i in values:
        if (sorted[i] != values[i]):
            return False
    return True

def is_straight_flush(hand: set[Card]):
    return is_flush(hand) & is_straight(hand)

def is_royal_flush(hand: set[Card]):
    if not is_flush(hand):
        return False
    values = sorted_hand = sorted(hand, key=lambda card: card.face.value)
    royal_values = list(1, 10, 11, 12, 13)
    for i in values:
        if (sorted[i] != values[i]):
            return False
    return True

def is_four_of_a_kind(hand:set[Card]):
    values = sorted_hand = sorted(hand, key=lambda card: card.face.value)
    return values[0] == values[2] | values[1] == values[3]

def is_full_house(hand: set[Card]):
    #dictionary of unique suits
    values = {card.value for card in hand}
    #if there is more than one suit, return false
    if len(values) != 2:
        return False
    
    key_list = values.keys()
    return (key_list[0] == key_list[1] & key_list[2] == key_list[4]) | (key_list[0] == key_list[2] & key_list[3] == key_list[4])


def is_three_of_a_kind(hand:set[Card]):
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

def rank_frequency(hand:set[Card]):
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

def is_two_pair(hand:set[Card]):
    freq = rank_frequency(hand)
    return sorted(freq) == [1, 2, 2]

def is_pair(hand:set[Card]):
    freq = rank_frequency(hand)
    return sorted(freq) == [1, 1, 1, 2]


        
# def compare_hand(hand1: set[Card], hand2: set[Card]):
#     if len(hand1) != 4:
#         raise ValueError('Hand must be length 4')
#     if len(hand2) != 4:
#         raise ValueError('Hand must be length 4')

#     # check for straight flush
#     if sorted(hand1, key=lambda card: card.face.value) == list(range(min(l), max(l)+1))
