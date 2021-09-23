
def do_you_trust(player_choice_cards, player):  
    while True:
        choice = input("Do you trust? choice \"Yes\" or \"No\" or \"Add\" to add more cards: ")
        if choice == "Yes":
            if sorted(player_choice_cards[1]) == sorted(player_choice_cards[2]):
                player_choice_cards[1].clear()
                player_choice_cards[2].clear()
                break

            else:
                if len(player_choice_cards[0]) > player + 1:
                    player_choice_cards[0][player].extend(player_choice_cards[1])
                    player_choice_cards[1].clear()
                    player_choice_cards[2].clear()
                    break

                elif len(player_choice_cards[0]) == player + 1:
                    player_choice_cards[0][0].extend(player_choice_cards[1])
                    player_choice_cards[1].clear()
                    player_choice_cards[2].clear()
                    break


        elif choice == "No":
            if sorted(player_choice_cards[1]) == sorted(player_choice_cards[2]):

                if len(player_choice_cards[0]) > player + 1:
                    player_choice_cards[0][player+1].extend(player_choice_cards[1])
                    player_choice_cards[1].clear()
                    player_choice_cards[2].clear()
                    break

                elif len(player_choice_cards[0]) == player + 1:
                    player_choice_cards[0][0].extend(player_choice_cards[1])
                    player_choice_cards[1].clear()
                    player_choice_cards[2].clear()
                    break

            else:
                player_choice_cards[0][player].extend(player_choice_cards[1])
                player_choice_cards[1].clear()
                player_choice_cards[2].clear()
                break
            
        elif choice == "Add":
            player_choice_cards[2].clear()
            return player_choice_cards


        else:
            print("Please write right answer, Yes,  No, or add")
            continue
    
    return player_choice_cards

