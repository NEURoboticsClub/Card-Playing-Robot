
from enum import Enum

class CardSuit(Enum):
    """Enum for the 4 possible card suits"""
    HEARTS = "hearts"
    SPADES = "spades"
    CLUBS = "clubs"
    DIAMONDS = "diamonds"

class CardValue(Enum):
    """Enum for the possible card values"""
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 1

class Card:
    """Represents a playing card with a suit and a card value"""
    
    def __init__(self, suit: CardSuit, value: CardValue):
        self.suit = suit
        self.value = value

