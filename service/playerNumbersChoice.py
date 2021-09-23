   
from typing import List
import numpy as np


def player_numbers(deck: List):
    #Cards are distributes to as many people as you enter, but only for 2 or 4 people
    player_hands = []
    while True:   
        players = input("Choose Number Of Players(choice 2 to 8): ")
        if int(players) > 1 or int(players) < 9:
            break
        else:
            print("Please enter correct numbers")
            continue

    splited = np.array_split(deck, int(players))

    for array in splited:
        player_hands.append(list(array))
    
    return player_hands, len(player_hands)
