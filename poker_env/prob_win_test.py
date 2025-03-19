import unittest
from random import shuffle
from card import Card, Face, Suit
from prob_win import prob_win

# Constants for tolerance and expected probabilities for specific test cases
DELTA = 0.05  # Tolerance for probability error
TEST1PROB = 0.68  # Expected probability for test case 1
TEST2PROB = 0.33  # Expected probability for test case 2
TEST3PROB = 0.15  # Expected probability for test case 3
TEST4PROB = 1.00  # Expected probability for test case 4
TEST5PROB = 0.54  # Expected probability for test case 5
TEST6PROB = 0.66  # Expected probability for test case 6
TEST7PROB = 0.36  # Expected probability for test case 7
TEST8PROB = 0.74  # Expected probability for test case 8

class TestProbWin(unittest.TestCase):

    # Test 1: Preflop, single player
    def test_prob_win_preflop_single_player(self):
        hand = [Card(Face.ACE, Suit.CLUBS), 
                Card(Face.KING, Suit.CLUBS)]
        table = []
        num_players = 1
        
        calculated_prob = prob_win(hand, table, num_players)
        self.assertAlmostEqual(calculated_prob, TEST1PROB, delta=DELTA)

    # Test 2: Flop, two players
    def test_prob_win_flop_two_players(self):
        hand = [Card(Face.ACE, Suit.CLUBS), 
                Card(Face.QUEEN, Suit.HEARTS)]
        table = [Card(Face.TEN, Suit.DIAMONDS), 
                 Card(Face.SEVEN, Suit.CLUBS), 
                 Card(Face.THREE, Suit.SPADES)]
        num_players = 2
        
        calculated_prob = prob_win(hand, table, num_players)
        self.assertAlmostEqual(calculated_prob, TEST2PROB, delta=DELTA)

    # Test 3: Turn, three players
    def test_prob_win_turn_three_players(self):
        hand = [Card(Face.ACE, Suit.CLUBS), 
                Card(Face.QUEEN, Suit.HEARTS)]
        table = [Card(Face.TEN, Suit.DIAMONDS), 
                 Card(Face.SEVEN, Suit.CLUBS), 
                 Card(Face.THREE, Suit.SPADES), 
                 Card(Face.TWO, Suit.HEARTS)]
        num_players = 3
        
        calculated_prob = prob_win(hand, table, num_players)
        self.assertAlmostEqual(calculated_prob, TEST3PROB, delta=DELTA)

    # Test 4: River, four players
    def test_prob_win_river_four_players(self):
        hand = [Card(Face.FOUR, Suit.CLUBS), 
                Card(Face.SIX, Suit.HEARTS)]
        table = [Card(Face.TEN, Suit.DIAMONDS), 
                 Card(Face.SEVEN, Suit.CLUBS), 
                 Card(Face.THREE, Suit.SPADES), 
                 Card(Face.TWO, Suit.HEARTS), 
                 Card(Face.FIVE, Suit.SPADES)]
        num_players = 9
        
        calculated_prob = prob_win(hand, table, num_players)
        self.assertAlmostEqual(calculated_prob, TEST4PROB, delta=DELTA)

    # Test 5: River, five players (more players means more competition)
    def test_prob_win_river_five_players(self):
        hand = [Card(Face.ACE, Suit.SPADES), 
                Card(Face.ACE, Suit.DIAMONDS)]
        table = [Card(Face.TEN, Suit.HEARTS), 
                 Card(Face.SEVEN, Suit.CLUBS), 
                 Card(Face.THREE, Suit.SPADES), 
                 Card(Face.TWO, Suit.HEARTS)]
        num_players = 5
        
        calculated_prob = prob_win(hand, table, num_players)
        self.assertAlmostEqual(calculated_prob, TEST5PROB, delta=DELTA)

    # Test 6: All cards known, the hand should win against 3 players
    def test_prob_win_all_known_cards(self):
        hand = [Card(Face.TEN, Suit.SPADES), 
                Card(Face.SEVEN, Suit.HEARTS)]
        table = [Card(Face.TEN, Suit.HEARTS), 
                 Card(Face.SEVEN, Suit.SPADES), 
                 Card(Face.FIVE, Suit.SPADES), 
                 Card(Face.ACE, Suit.SPADES)]
        num_players = 3
        
        calculated_prob = prob_win(hand, table, num_players)
        self.assertAlmostEqual(calculated_prob, TEST6PROB, delta=DELTA)

    # Test 7: All possible players, but no strong hand
    def test_prob_win_no_strong_hand(self):
        hand = [Card(Face.TWO, Suit.SPADES), 
                Card(Face.THREE, Suit.HEARTS)]
        table = [Card(Face.SEVEN, Suit.CLUBS), 
                 Card(Face.EIGHT, Suit.DIAMONDS), 
                 Card(Face.NINE, Suit.SPADES), 
                 Card(Face.TEN, Suit.HEARTS), 
                 Card(Face.JACK, Suit.CLUBS)]
        num_players = 5
        
        calculated_prob = prob_win(hand, table, num_players)
        self.assertAlmostEqual(calculated_prob, TEST7PROB, delta=DELTA)

    # Test 8: Preflop case with no table cards
    def test_prob_win_no_table_cards(self):
        hand = [Card(Face.ACE, Suit.CLUBS), 
                Card(Face.ACE, Suit.HEARTS)]
        table = []
        num_players = 2
        
        calculated_prob = prob_win(hand, table, num_players)
        self.assertAlmostEqual(calculated_prob, TEST8PROB, delta=DELTA)

if __name__ == '__main__':
    unittest.main()