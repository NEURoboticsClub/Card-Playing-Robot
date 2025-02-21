from random import shuffle
from typing import List
from card import Card, generate_all_cards
from scoring_type import Scoring


TRIALS = 10000
def prob_win(hand: List[Card], table: List[Card], num_players: int):
    """
    Runs `TRIALS` simulations, determining the probabalistic chance of winning given:\n
    `hand` (personal hand): 2 cards\n
    `table`: between 0 and 5 cards\n
    `num_players`: Number of players EXCLUDING you (in range [1,21])
    """
    assert num_players >= 1 and num_players <= 21
    
    wins = 0
    deck = generate_all_cards()

    # Remove all preexistent cards
    for card in table + hand:
        deck.remove(card)


    # Run trials
    for _ in range(TRIALS):
        t_table = table[:]
        players: List[List[Card]] = [[] for _ in range(num_players)]
        shuffle(deck)

        # Populate table
        for i in range(5 - len(table)):
            t_table.append(deck[-(i + 1)])

        # Distribute cards to other players
        for i in range(num_players):
            players[i].append(deck[2 * i])
            players[i].append(deck[2 * i + 1])
            players[i].extend(t_table)

        # Determine win
        if _hand_won(hand + t_table, players):
            wins+=1

    return (wins/TRIALS)

def _hand_won(hand: List[Card], players: List[List[Card]]):
    """
    Given the personal and community cards `hand`,
    and the same for other players 'players',
    Determines if you won the simulation.
    """
    self_score = Scoring.get_scoring_given_hand(hand)
    player_scores = [0] * len(players)
    
    # Find what all other players scored
    for i in range(len(players)):
        player_scores[i] = Scoring.get_scoring_given_hand(players[i])

    # The type of the strongest hand the rest of the table has
    strongest_score = min(player_scores, key=lambda score: score.value)  # Use the .value for comparison

    # Compare using the enum values (integers)
    if self_score.value > strongest_score.value:
        return False
    if self_score.value < strongest_score.value:
        return True

    # Tied score
    if self_score.value == strongest_score.value:
        # Gather all players who have the strongest score
        strongest_players = [i for i in range(len(players)) if player_scores[i] == strongest_score]
        
        # If the player is in consideration and didn't lose a single tiebreaker, return True
        if all(Scoring.tiebreak(hand1=hand, hand2=players[i], score=self_score) != 2 for i in strongest_players):
            return True

    return False