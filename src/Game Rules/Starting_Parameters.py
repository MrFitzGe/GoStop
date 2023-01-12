def get_starting_params():
    num_players = int(input("Enter Number of Players : ")) # it takes user input
    deck_size = 48


    if num_players == 2:
        hand_size = 10
        points_threshold = 5
        number_starting_common_cards = 8

    elif num_players == 3:
        hand_size = 8
        points_threshold = 3
        number_starting_common_cards = 6

    elif num_players == 4:
        hand_size = 5
        points_threshold = 3
        number_starting_common_cards = 8
 
    else:
        print("Unacceptable number of players")
 
 
 
get_starting_params()