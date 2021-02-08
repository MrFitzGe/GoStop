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
                  
    def deal(self):
        for p in self.num_players:
            self.player_hand[p] = Deck.draw_card(self.hand_size)
                
        self.common_cards = Deck.draw_card(self.number_starting_common_cards)
                            
            
class Player:
    
    def __init__(self):
        self.player_hand = []
        self.player_scoreboard = []
        self.player_points= 0
        self.player_num_go = 0

    def play_card(self, which_card):
        #check which_card in range (0:len(self.player_hand))
        self.player_hand = self.player_hand - chosen_card
        return chosen_card
    
        