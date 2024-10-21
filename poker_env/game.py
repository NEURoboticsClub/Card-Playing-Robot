from card import Card
from scoring_type import Scoring
from enum import Enum
from typing import List


class PokerAction(Enum):
    CALL = 0
    RAISE = 1
    FOLD = 2
    CHECK = 3

class Player:
    name: str
    chips: int
    current_bet: int
    current_action: PokerAction
    hand: List[Card]

    def __init__(self, name: str, hand: List[Card], chips: int):
        self.name = name
        self.hand = hand
        self.chips = chips
        self.current_bet = 0

    # call is when same number of chips is bet
    # raise is when more chips are bet
    # fold is when no chips are bet
    # check defers

    def bet(self, number_of_chips: int):
        self.current_bet = number_of_chips

    def discard(self):
        self.hand = []

    def add_card_to_hand(self, card: Card):
        self.hand.append(card)
    
    def set_action(self, action: PokerAction):
        self.current_action = action

class PokerGame:
    players: List[Player]
    deck: List[Card]
    table_hand: List[Card]
    pot: int

    def __init__(self, players: List[Player], deck: List[Card], pot: int):
        self.players = players
        self.deck = deck
        self.pot = pot
    
    def play_to_table(self, number_of_cards: int):
        for _ in range(number_of_cards):
            if len(deck) != 0:
                table_hand.append(deck[0])
                deck.remove(0)
            else:
                break

    def betting_round(self):
        previous_player_checked = False
        for player in players:
            if player.current_action == PokerAction.CALL:
                ...
            elif player.current_action == PokerAction.RAISE:
                ...
            elif player.current_action == PokerAction.FOLD:
                ...
            elif player.current_action == PokerAction.CHECK:
                ...
                previous_player_checked = True

    def determine_winning_hand(self):
        scores = {i.name : Scoring.get_scoring_given_hand(i.hand) for i in players}
        scores = {name : (scoring, scoring.value) for name, scoring in scores}
        maximum_score = max(list(scores.values()))

        best_players = []
        for name, (_, value) in scores:
            if value == maximum_score:
                best_players.append(name)

        if len(best_players) == 1:
            return best_players[0].name

        best_cards_and_players = {}
        for player_name in best_players:
            highest_card = Card(Face.TWO, Suit.SPADES)
            for player in players:
                if player.name == player_name:
                    current_player = player
            
            for card in current_player.hand:
                if card.face.value > highest_card.face.value \
                    and card.suit.value >= highest_card.suit.value:
                    highest_card = card

            best_cards_and_players[current_player.name] = highest_card

        return max(best_cards_and_players, key=lambda k: best_cards_and_players[k])

# method on card to compare cards or convert it to an integer value
