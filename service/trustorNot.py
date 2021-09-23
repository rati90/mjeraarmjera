def hands_table_clear(player_hands_table_say):
    player_hands_table_say[1].clear()
    player_hands_table_say[2].clear()


def do_you_trust(player_hands_table_say, player):  
    while True:
        choice = input("Do you trust? choice \"Yes\" or \"No\" or \"Add\" to add more cards: ")
        if choice == "Yes":
            if sorted(player_hands_table_say[1]) == sorted(player_hands_table_say[2]):
                hands_table_clear(player_hands_table_say)
                break

            else:
                if len(player_hands_table_say[0]) > player + 1:
                    player_hands_table_say[0][player].extend(player_hands_table_say[1])
                    hands_table_clear(player_hands_table_say)
                    break

                elif len(player_hands_table_say[0]) == player + 1:
                    player_hands_table_say[0][0].extend(player_hands_table_say[1])
                    hands_table_clear(player_hands_table_say)
                    break


        elif choice == "No":
            if sorted(player_hands_table_say[1]) == sorted(player_hands_table_say[2]):

                if len(player_hands_table_say[0]) > player + 1:
                    player_hands_table_say[0][player+1].extend(player_hands_table_say[1])
                    hands_table_clear(player_hands_table_say)
                    break

                elif len(player_hands_table_say[0]) == player + 1:
                    player_hands_table_say[0][0].extend(player_hands_table_say[1])
                    hands_table_clear(player_hands_table_say)
                    break

            else:
                player_hands_table_say[0][player].extend(player_hands_table_say[1])
                hands_table_clear(player_hands_table_say)
                break
            
        elif choice == "Add":
            player_hands_table_say[2].clear()
            return player_hands_table_say


        else:
            print("Please write right answer, Yes,  No, or add")
            continue
    
        
        return player_hands_table_say

