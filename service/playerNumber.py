   
from typing import List
import numpy as np


def player_number(deck: List):
    while True:
        try:
            parts = []
            question = int(input("Choose Number Of Players: "))
            splited = np.array_split(deck, question)

            for array in splited:
                parts.append(list(array))
            return parts   
                        
        except ValueError:
            print("Enter valid input")
            continue


