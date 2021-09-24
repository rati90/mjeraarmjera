   
from typing import List
import numpy as np


def player_numbers(deck: List):
    #Cards are distributes to as many people as you enter, but only for 2 or 4 people
    player_hands = []
    while True:   
        players = input("Choose Number Of Players(choice 2 to 8): ")
        if players.isnumeric():
            if int(players) > 1 and int(players) < 9:
                break
            else:
                print("Please enter correct numbers\n")
                continue
        else:
            print("Please enter only numbers\n")
            continue
    splited = np.array_split(deck, int(players))

    for array in splited:
        player_hands.append(list(array))
    
    return player_hands, len(player_hands)




def player_names(player_cards_and_numbers):
    position = 1
    for names in player_cards_and_numbers[0]:
        names.insert(0, f"Player N {position}")
        position += 1
        
    return player_cards_and_numbers

