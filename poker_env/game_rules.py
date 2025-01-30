# https://bicyclecards.com/how-to-play/basics-of-poker

from enum import Enum
from card import Card, Face, Suit
from collections import Counter
from typing import List

"""
Read: Notes on ties in Texas Hold'em
A tie is an exceedingly rare occurence as two players need to have completely identical best hands.
In general, most collisions, as seen in example 1 are broken by comparing the most significant cards(s) of a hand against each other

ex1: Full House
p1: 55522
p2: 444AA
p1 wins as (555)>(444)

Sometimes, the most significant card is tied across two hands, as seen in example 2. Then, the next most-significant card(s) are compared

ex2: Two Pair
p1: JJ44A
p2: JJ882
p2 wins as the MSCs (JJ) are equal, and in the next comparison, (88) > (44)

A Tie can only occour if all possible cards are compared to be equal to each other, seen in example 3

ex3: Straight
p1: T9876
p2: T9876
A tie thus occours, winnings are split between the tied players.
Though effectively impossible, a tie can occour between a maximum of 4 players

To assist in later tiebreaking, all hand detection functions return the sorted 5 cards that make up the best winning hand if it is triggered, and an empty list if not.
MSC order is also sorted by suit, in priority SPADE -> HEART -> DIAMOND -> CLUB
"""


def is_straight_flush(hand: List[Card]):
    """
    Identifies if a hand of 7 Cards is a flush. If so, identifies if the 5 returned cards also form a straight\n
    Both `is_straight` and `is_flush` can take less than 7 inputs\n
    `is_straight` is the outer function because of the specific ordering (5432A)
    """
    return is_straight(is_flush(hand))


def is_flush(hand: List[Card]):
    """
    Identifies if a hand of 7 Cards is a flush. If so, return the 5 most significant. If not, return an empty list
    """
    # A flush is when 5 of the 7 cards are of the same suit
    # Define a counter for each suit, check if any counter is greater than or equal to 5
    counters = [0]*4
    for i in hand:
        # suit.value is 1-indexed
        counters[i.suit.value - 1] += 1
    for i in range(len(counters)):
        if (counters[i] >= 5):
            # suit.value is 1-indexed
            return _best_flush(i+1,hand)
    return []

def _best_flush(suit: int, hand: List[Card]):
    """
    Finds the best flush that can be made with a given hand. Assumes the input is a flush
    """
    # Sort the hand in order of card power
    # Then, add all cards that fulfill the condition of being in the right suit to the hand
    # Then, truncate the hand to just the top 5 cards
    best_hand: List[Card] = []
    sorted_hand = sorted(hand, key= lambda card: (card.face.value, card.suit.value), reverse=True)
    for i in sorted_hand:
        if (i.suit.value == suit):
            best_hand.append(i)
    return best_hand[0:5]


def is_straight(hand: List[Card]):
    """
    Identifies if a hand of 7 Cards is a straight. If so, return the 5 most significant. If not, return an empty list
    """
    # A straight is when 5 of the 7 cards are in ascending order
    # Map each value to an array. Search backwards to check if 5 of them in a row are true.
    # Return the first 5 elements of the descending sorted list starting from the start of the best straight
    values = [i.face.value for i in hand]
    hits = [False] * 14
    for i in values:
        # Cards are 1-indexed here (A on both sides)
        if not hits[i-1]:
            hits[i-1] = True
            if i == 14:
                hits [0] = True

    # Check if 5 entries in a row are true, ergo, you have a straight
    true_counter = 0
    for i in reversed(range(len(hits))):
        if hits[i]:
            true_counter += 1
        else:
            true_counter = 0
        if true_counter == 5:
            if i == 0:  # Ace-low straight
                return _best_straight(5, hand, ace_high=False)
            return _best_straight(i + 5, hand)

    return []

def _best_straight(highest: int, hand: List[Card], ace_high: bool = True):
    """
    Finds the best straight that can be made from a given hand. Assumes the input is a straight
    """
    # Check if empty due to is_flush code
    if not hand: return []
    # Sort the hand in descending order
    # Account for A2345 with a seperate lambda
    # Go down through the list, starting from the highest card recorded
    # if the card value is the same as the next previous card added, continue
    if ace_high:
        sorted_hand = sorted(hand, key= lambda card: (card.face.value, card.suit.value), reverse=True)
    else:
        # Cards are 2-indexed and A (14) is treated like 1
        sorted_hand = sorted(hand, key= lambda card: (1 if card.face.value == 14 else card.face.value, card.suit.value), reverse=True)
    best_hand: List[Card] = []
    for c in sorted_hand:
        # Haven't reached the straight yet
        if c.face.value > highest and not best_hand:
            continue
        # If card value not already in straight, add next
        if (not best_hand) or (c.face.value != best_hand[-1].face.value):
            best_hand.append(c)
            # If long enough
            if len(best_hand) == 5:
                return best_hand
    raise ValueError(f"Straight detection failed unexpectedly: {best_hand}")
        


def is_royal_flush(hand: List[Card]):
    """
    Check if it's a straight flush equal to (AKQJT)
    """
    sort_hand = is_straight_flush(hand)
    if not sort_hand: return False
    # Card face values for AKQJT
    wanted = [14,13,12,11,10]
    for i in range(5):
        if sort_hand[i].face.value != wanted[i]: return False
    return sort_hand

def is_four_of_a_kind(hand: List[Card]):
    """
    Identifies if a hand of 7 Cards is four of a kind. If so, return the 5 most significant. If not, return an empty list
    """
    count = _count_card_nums(hand)
    
    # Checks if there are 4 of the same face
    for i in range(2,15):
        if count[i - 2] == 4:
            return _best_four(i, hand)
    return []


def _best_four(i: int, hand: List[Card]):
    # We already know all 4 of these cards will be present
    best_hand = [Card(Face(i), Suit.SPADES),
                 Card(Face(i), Suit.HEARTS),
                 Card(Face(i), Suit.DIAMONDS),
                 Card(Face(i), Suit.CLUBS),]
    sorted_hand = sorted(hand, key= lambda card: (card.face.value, card.suit.value), reverse=True)
    # The next MSC will either be the first card in `sorted_hand` or the 5th card
    if sorted_hand[0].face.value != i:
        best_hand.append(sorted_hand[0])
    else:
        best_hand.append(sorted_hand[4])
    assert len(best_hand) == 5
    return best_hand
        

def is_full_house(hand: List[Card]):
    """
    Identifies if a hand of 7 Cards is a Full house (Triple + Pair). If so, return the 5 most significant. If not, return an empty list
    """
    count = _count_card_nums(hand)
    three = False
    two = False
    for i in reversed(range(2,15)):
        if not three:
            if count[i - 2] == 3:
                three = i
                continue
        if not two:
            if count[i - 2] >= 2:
                two = i
    if three and two:
        return _best_full_house(three, two, hand)
    return []

def _best_full_house(three: int, two: int, hand: List[Card]):
    """
    Finds the best full house that can be made with `hand`, given that\n
    `three` represents the optimal triple and `two` represents the optimal double
    """
    sorted_hand = sorted(hand, key= lambda card: (card.face.value, card.suit.value), reverse=True)
    best_hand: List[Card] = []
    for c in sorted_hand:
        if c.face.value == three and len(best_hand) < 3:
            best_hand.append(c)
    for c in sorted_hand:
        if c.face.value == two and len(best_hand) < 5:
            best_hand.append(c)
    assert len(best_hand) == 5
    return best_hand
    
def is_three_of_a_kind(hand: List[Card]):
    """
    Identifies if a hand of 7 Cards is a Three of a kind. If so, return the 5 most significant. If not, return an empty list
    """
    count = _count_card_nums(hand)
    for i in reversed(range(2, 15)):
        if count[i - 2] == 3:
            return _best_triple(i, hand)
    return []

def _best_triple(i: int, hand: List[Card]):
    """
    Finds the best triple that can be made with `hand`
    """
    sorted_hand = sorted(hand, key= lambda card: (card.face.value, card.suit.value), reverse=True)
    best_hand: List[Card] = []
    # Add the triple
    for c in sorted_hand:
        if c.face.value == i:
            best_hand.append(c)
    # Add the 2 highest remaining cards
    for c in sorted_hand:
        if c.face.value != i:
            best_hand.append(c)
        if len(best_hand) == 5:
            break
    return best_hand


def is_two_pair(hand: List[Card]):
    """
    Identifies if a hand of 7 Cards is a Two Pair. If so, return the 5 most significant. If not, return an empty list
    """
    count = _count_card_nums(hand)
    pair1 = False
    pair2 = False
    for i in reversed(range(2,15)):
        if not pair1:
            if count[i - 2] == 2:
                pair1 = i
            continue
        if not pair2:
            if count[i - 2] == 2:
                pair2 = i
                break
    if pair1 and pair2:
        assert pair1 != pair2
        return _best_two_pair(pair1, pair2, hand)
    return []

def _best_two_pair(p1: int, p2: int, hand: List[Card]):
    """
    Finds the best two pairs that can be made with `hand`
    """
    sorted_hand = sorted(hand, key= lambda card: (card.face.value, card.suit.value), reverse=True)
    best_hand: List[Card] = []
    for c in sorted_hand:
        if c.face.value == p1:
            best_hand.append(c)
        if c.face.value == p2:
            best_hand.append(c)
    for c in sorted_hand:
        if c.face.value != p1 and c.face.value != p2:
            best_hand.append(c)
            break
    return best_hand

def is_pair(hand: List[Card]):
    """
    Identifies if a hand of 7 Cards is a Pair. If so, return the 5 most significant. If not, return an empty list
    """
    count = _count_card_nums(hand)
    for i in reversed(range(2,15)):
        if count[i - 2] == 2:
            return _best_pair(i, hand)
    return []

def _best_pair(pair_index: int, hand: List[Card]):
    """
    Finds the best pair that can be made with `hand`
    """
    sorted_hand = sorted(hand, key= lambda card: (card.face.value, card.suit.value), reverse=True)
    best_hand: List[Card] = []
    for c in sorted_hand:
        if c.face.value == pair_index:
            best_hand.append(c)
    for c in sorted_hand:
        if c.face.value != pair_index:
            best_hand.append(c)
            if len(best_hand) == 5:
                break
    return best_hand

def _count_card_nums(hand: List[Card]):
    """
    Counts the occourences of the numbers for each card in a hand. Indexes are shifted by 2 from the normal
    """
    count = [0]*14
    for c in hand:
        # values are 2-indexed
        count[c.face.value - 2] += 1
    return count

def is_no_pair(hand: List[Card]):
    return sorted(hand, key= lambda card: (card.face.value, card.suit.value), reverse=True)[0:5]
