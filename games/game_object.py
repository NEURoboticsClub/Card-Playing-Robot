from card import Card

class GameObject:
    """Represents a generic game piece, with an (x, y) position on the board, a piece type (such as player x or player y), 
    and a card object that contains the card suit and value."""

    def __init__(self, position: tuple[int, int], type: str, card: Card):
        self.position = position
        self.type = type
        self.card = card
        
    """Move the game object a given x and/or y distance in millimeters and update the object's position field.
    
    Args:
        x_dist (optional): the horizontal distance to move the object
        y_dist (optional): the vertical distance to move the object
    """
    def move(self, x_dist: int = 0, y_dist: int = 0) -> None:
        cur_x = self.position[0]
        cur_y = self.position[1]

        new_pos = (cur_x + x_dist, cur_y + y_dist)

        self.position = new_pos

        
    
