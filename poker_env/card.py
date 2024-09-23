from dataclasses import dataclass
from enum import Enum
import itertools


class Face(Enum):
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
    ACE = 14

class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

@dataclass
class Card():
    face: Face
    suit: Suit

    def __init__(self, face: Face, suit: Suit):
        self.face = face
        self.suit = suit

    def __hash__(self):
        return hash((self.face, self.suit))

    def __repr__(self):
        return f'({self.face.__str__()}, {self.suit.__str__()})'

def generate_all_cards():
    return [Card(face, suit) for face, suit in itertools.product(list(Face), list(Suit))]
