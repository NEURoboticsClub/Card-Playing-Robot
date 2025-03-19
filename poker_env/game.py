from card import Card
from card import Face
from card import Suit
from scoring_type import Scoring
from enum import Enum
from typing import List
import copy
import random
from dataclasses import dataclass
import copy

@dataclass
class PokerAction:
    expansiveActionList = ["CALL","RAISE","FOLD","CHECK"]
    
    def generateRaise(action:str, amount:int = -1):
        p = PokerAction()
        p.action = action
        p.amount = amount
        return p


#Players must have the following fields and methods:
#name: str
#chips: int
#current_bet: int
#hand: List[Card]
#getAction() -> PokerAction
#blind: enum class: {SMALL, BIG, NONE}
#bet(number_of_chips: int)

class Player:
    name: str
    chips: int
    current_bet: int
    _current_action: PokerAction
    _hand: List[Card]
    _action_list: List[PokerAction]

    def __init__(self, name: str, chips: int,action_list: List[PokerAction]):
        self.name = name
        self.hand = []
        self.chips = chips
        self.current_bet = 0
        self.action_list = action_list

    # call is when same number of chips is bet
    # raise is when more chips are bet
    # fold is when no chips are bet
    # check defers

    def bet(self, number_of_chips: int):
        self.current_bet = number_of_chips
        self.chips -= number_of_chips

    #remove the current hand
    def discard(self):
        self.hand = []

    def add_card_to_hand(self, card: Card):
        self.hand.append(card)

    def getAction(self):
        return self.action_list.pop(0)
    


    
    

#TO-DO LIST FOR ALL SUBSEQUENT PROGRAMMERS:
#CHECK THEM OFF IF YOU HAVE ALREADY DONE IT

#Task 1: Create a shuffle function(s) to shuffle and randomize the deck. One to shuffle a new deck and one to shuffle all the current cards.

#TASK 1 is now finished. Also made tests for TASK 1

#Task 2: Create function(s) to properly set up all the players and the pot at the start.

#Task 2 is now finished. We need to make tests for it.


#Task 3: Create the ultimate simulator function combining all the previous functions to fully simulate a new game.
#Task 4: Create unit tests for the tasks 1-3
#Task 5: Recreate Betting Round.

class PokerGame:
    players: List[Player]
    _deck: List[Card]
    table_hand: List[Card]
    pot: int
    buy_in: int

    #all players MUST have 0 cards.
    #deck MUST be 52 cards full
    #pot MUST be 0
    def __init__(self, players: List[Player]):
        self.players = players
        self.deck = self.shuffle_deck_full()
        self.pot = 0
        self.buy_in = 0
        self.table_hand = []


    #generates a fully shuffled deck of 52 cards TESTED
    def shuffle_deck_full(self):
        deck = []
        for number_name in Face:
            for suit_name in Suit:
                newCard = Card(number_name,suit_name)
                deck.append(newCard)
        
        #at this point we created a sorted deck of 52 unique cards

        shuffledDeck = []

        while len(deck) > 1:
            randomIndex = random.randint(0,len(deck)-1)
            shuffledDeck.append(deck.pop(randomIndex))
        shuffledDeck.append(deck.pop(0))

        return shuffledDeck
    
    #shuffles a given deck of cards TESTED
    #This will ALTER the previous deck of cards, turning the previous deck into length 0.
    def shuffle_deck_current(self,currentDeck):
        shuffledDeck = []

        while len(currentDeck) > 1:
            randomIndex = random.randint(0,len(currentDeck)-1)
            shuffledDeck.append(currentDeck.pop(randomIndex))
        shuffledDeck.append(currentDeck.pop(0))

        return shuffledDeck
    
    #checks if the deck has enough cards to deal the river.
    #returns true if it can, false if it cannot.
    def is_river_dealable(self):
        return len(self.deck) >= 5
    
    #Deals number_of_cards public cards to the table
    def deal_to_table(self, number_of_cards: int):
        for _ in range(number_of_cards):
            if len(self.deck) != 0:
                self.table_hand.append(self.deck[0])
                self.deck.remove(0)
            else:
                break
    
    #Deals two cards by default to each player from the deck, if there are not enough cards in the deck to do so, return false.
    #otherwise return true to signify that the operation is successful
    def deal_to_players(self, number_of_cards_per_player = 2):
        required_card_total = number_of_cards_per_player * len(self.players)
        if required_card_total > len(self.deck):return False
        for player in self.players:
            plucked_card = self.deck.pop(0)
            plucked_card_2 = self.deck.pop(0)
            player.add_card_to_hand(plucked_card)
            player.add_card_to_hand(plucked_card_2) #possible change this literal intepretation
        return True
    
    #discard all hands from all players
    def remove_all_cards_from_players(self):
        for player in self.players:
            player.discard()
    
    def startNewGame(self):
        self.remove_all_cards_from_players()
        self.deck = self.shuffle_deck_full()
        self.deal_to_players()
        self.betting_round()
        #dealing the river
        self.deal_to_table(3)
        self.betting_round()
        #4th
        self.deal_to_table(1)
        self.betting_round()
        #5th
        self.deal_to_table(1)
        self.betting_round()
        self.award_winnings(self.determine_winning_hand())
    
    
    # award all the money from the pot into the selected player
    def award_winnings(self,winning_player):
        winning_player.chips += self.pot
        self.pot = 0




    #goes through every player and forces each player to take their designated action as determined in the Player class
    def betting_round(self):
        temp_players = self.players.copy()
        x = input("Press Enter to Continue: ")
        for i in range(len(players)):#maybe make a temp list of players so we can exclude players who have folded
            action = temp_players[i].getAction()
            if action.action == "CALL":
                temp_players[i].bet(self.buy_in)
                self.pot += temp_players[i].current_bet
            elif action.action == "RAISE":
                self.buy_in += action.amount
                temp_players[i].bet(self.buy_in)
                self.pot += temp_players[i].current_bet
            elif action.action == "FOLD":
                self.players[i].bet(0)
                self.players.remove(i)
                
            elif action.action == "CHECK":
                temp_players[i].bet(0)

    #When there is five cards left, determine the best hand out of all the players
    def determine_winning_hand(self):
        scores = {i.name : Scoring.get_scoring_given_hand(i.hand) for i in self.players}
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
            for player in self.players:
                if player.name == player_name:
                    current_player = player
            
            for card in current_player.hand:
                if card.face.value > highest_card.face.value \
                    and card.suit.value >= highest_card.suit.value:
                    highest_card = card

            best_cards_and_players[current_player.name] = highest_card

        return max(best_cards_and_players, key=lambda k: best_cards_and_players[k])

# method on card to compare cards or convert it to an integer value

