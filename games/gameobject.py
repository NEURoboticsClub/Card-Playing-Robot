from card import Card

class GameObject:
    """Represents a generic game piece, with an (x, y) position on the board, a piece type (such as player x or player y), 
    and a card object that contains the card suit and value."""

    def __init__(self, position: tuple[int, int], type: str, card: Card):
        self.position = position
        self.type = type
        self.card = card
    
