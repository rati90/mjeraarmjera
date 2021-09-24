
def check_end(player_hands_table_say: tuple):
    """
    The fun checks if there are only one player left with the cards. Therefore ends the game
    :param player_hands_table_say tuple. all cards on game

    :return None or the same cards
    """
    count = 0
    for i in player_hands_table_say[0]:
        if len(i) == 0:
            count += 1

    if count == len(player_hands_table_say[0]) - 1:
        return None
    else:
        return player_hands_table_say 


def check_hand_zero(player_hands_table_say: tuple):
    """
    After the one sesion checks if player have any cards in hand. if yes he is out (a winner)
    """
    for cards in player_hands_table_say[0]:
        if len(cards) == 1:
            player_hands_table_say[0].remove(cards)
            print(f"!! {cards[0]} is out of game !! \n")
    
    return player_hands_table_say


