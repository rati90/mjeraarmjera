def hands_table_clear(table, said_cards):
    """
    for some decisions clears table and say lists
    :param tuple player_hands_table_say not cleared table and say

    :return tuple player_hands_table_say cleared  table and say
    """
    table.clear()
    said_cards.clear()
    return table, said_cards


def do_you_trust(player_hands_table_say: tuple, player: int):
    """
    The function takes next players choices Yes, No, or Add 
    and depend on it give cards to players and removes
    :param player_hands_table_say tuples that included three lists
    :param player the player that made previous decision

    :return  player_hands_table_say  tuple modified depend on choices
    """
    all_players_cards = player_hands_table_say[0]
    table = player_hands_table_say[1]
    said_cards = player_hands_table_say[2]
    next_player = player + 1  

    while True:
        choice = input( f"Player N {player + 2} Do you trust? choice \"Yes\" or \"No\" or \"Add\" to add more cards:")
        if choice == "Yes":
            print(table, said_cards)
            if sorted(table) == sorted(said_cards):
                hands_table_clear(table, said_cards)
                break
            else:
                if len(all_players_cards) > next_player:
                    all_players_cards[next_player].extend(table)
                    hands_table_clear(table, said_cards)
                    break

                elif len(all_players_cards) == next_player:
                    all_players_cards[0].extend(table)
                    hands_table_clear(table, said_cards)
                    break

        elif choice == "No":
            if sorted(table) == sorted(said_cards):

                if len(all_players_cards) > next_player:
                    all_players_cards[next_player].extend(table)
                    hands_table_clear(table, said_cards)
                    break

                elif len(all_players_cards) == next_player:
                    all_players_cards[0].extend(table)
                    hands_table_clear(table, said_cards)
                    break

            else:
                all_players_cards[player].extend(table)
                hands_table_clear(table, said_cards)
                break
            
        elif choice == "Add":
            said_cards.clear()
            return player_hands_table_say

        else:
            print("Please write right answer, Yes,  No, or add\n")
            continue
    
        print("print here2")
        
        return player_hands_table_say

