# OOP Class for a Game and all associated actions required to play

## Dependencies
from datetime import datetime
import numpy as np
import pandas as pd


## Classes

class Deck:
# cards is the full map of all possible cards
# deck is the current deck in play for one game. A shuffle call creates a deck.

# To add, cut function
    def __init__(self):
        self.cards = pd.DataFrame(
        {
            "Number": np.array(range(0,48)),
            "Month": pd.Categorical(["Jan", "Jan", "Jan", "Jan", "Feb", "Feb", "Feb", "Feb", "Mar", "Mar", "Mar", "Mar", "Apr", "Apr", "Apr", "Apr", "May", "May", "May", "May", "Jun", "Jun", "Jun", "Jun", "Jul", "Jul", "Jul", "Jul", "Aug", "Aug", "Aug", "Aug", "Sep", "Sep", "Sep", "Sep", "Oct", "Oct", "Oct", "Oct", "Nov", "Nov", "Nov", "Nov", "Dec", "Dec", "Dec", "Dec"]) ,
            "Group": pd.Categorical(["bright", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "bright", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "bright", "animal", "junk", "junk", "junk", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "bright", "junk", "junk", "junk", "bright", "animal", "ribbon", "junk"]),
            "Special": pd.Categorical(["None", "Red_Writing", "None", "None", "Bird", "Red_Writing", "None", "None", "None", "Red_Writing", "None", "None", "Bird", "Red_Blank", "None", "None", "Maybe_DoubleJunk", "Red_Blank", "None", "None", "None", "Blue_Writing", "None", "None", "None", "Red_Blank", "None", "None", "None", "Bird", "None", "None", "DoubleJunk", "Blue_Writing", "None", "None", "None", "Blue_Writing", "None", "None", "None", "DoubleJunk", "None", "None", "SadMan", "DeadBird", "DeadRibbon", "DoubleJunk"])
        }
)

    def shuffle(self):
        self.deck = self.cards.sample(frac = 1)  
    
    def draw_card(self, num_cards = 1):
        dispensed_cards = self.cards.head(num_cards) 
        self.cards = self.cards.iloc[num_cards:len(self.deck.index)]
        return dispensed_cards


class Game:
    # Class for rules and interaction functions
    def __init__(self):
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
        
    def get_starting_params(self):
        self.num_players = int(input("Enter Number of Players : ")) # it takes user input
        self.deck_size = 48
        self.turn_num = 0

        if self.num_players == 2:
            self.hand_size = 10
            self.points_threshold = 5
            self.number_starting_common_cards = 8

        elif self.num_players == 3:
            self.hand_size = 8
            self.points_threshold = 3
            self.number_starting_common_cards = 6

        elif self.num_players == 4:
            self.hand_size = 5
            self.points_threshold = 3
            self.number_starting_common_cards = 8
    
        else:
            print("Unacceptable number of players")
                  
    def deal_hand(self, Player):
        Player.hand = Deck.draw_card(self.hand_size)
              
    def deal_common_cards(self):
        self.common_cards = Deck.draw_card(self.number_starting_common_cards)    
                            
            
class Player:
    
    def __init__(self):
        self.hand = pd.DataFrame() # dataframe of cards. Each row is a card in hand
        self.scoreboard = pd.DataFrame() #dataframe of cards collected to be scored. Each row is a collected card.
        self.points_accumulated = 0
        self.num_go = 0

    def play_card(self, which_card, common_cards, play_position):
        #check which_card in range (0:len(self.hand))
        chosen_card = self.hand.iloc[[which_card]]
        self.hand = self.hand.drop[[which_card]]
        
        if chosen_card['Month'] == common_cards.iloc[[play_position]]['Month']:
            self.scoreboard.append(chosen_card)
            self.scoreboard.append(common_cards.iloc[[play_position]])
            
            common_cards.drop[[play_position]]
            Deck.draw_card(1)
            
        else:
            common_cards.append(chosen_card)
            Deck.draw_card(1)
            
            ##~ask Mike about crapping logic
        
    
    
    def collect_cards(self, card_pairs):
        self.scoreboard = self.scoreboard.append(card_pairs)
        
    def say_go(self):
        self.num_go += 1
    
    def tally_points(self):
        self.scoreboard ==> points.py
        