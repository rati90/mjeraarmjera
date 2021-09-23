

def player_say(player_input, deck):
    player_say = []
    print("Choice the cards to Say out Loud!")
    while int(player_input) > len(player_say):
        say_choice = input("Choice the cards to say as many as you put: ")
        
        if len(player_say) == 0 and say_choice in deck:
            player_say.append(say_choice)
            continue
        
        elif len(player_say) > 0 and say_choice in deck and player_say[0][0] == say_choice[0] and say_choice not in player_say:
            player_say.append(say_choice)
            continue

        else:
            print("Please choice cards from deck and with same name")
            continue

    
    return player_say





def player_choice_cards(player_hands, table, player, deck):
    while True:
        print(f"player N {player + 1} this are your cards {player_hands[player]}")
        player_input = input(f"Player N {player + 1} please choose how many cards to select: ")
        if player_input.isnumeric():
            if int(player_input) > 0 and int(player_input) < 5:
                break
            else:
                print("print write number between 1-4")
                continue
        else:
            print("print only numbers")
            continue
    
    count = 0
    while int(player_input) > count:
        print(player_hands[player])
        player_choice = input("Please choose the card:")
        

        if player_choice in player_hands[player]:
            table.append(player_choice)
            player_hands[player].remove(player_choice)
            count += 1
            continue
        else:
            print("Please choice the cards you have")
            continue
    
        
    player_outloud = player_say(player_input, deck)
    
    
    return player_hands, table, player_outloud 





    
