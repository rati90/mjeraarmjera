
def player_say(player_input:str, deck:list):
    """
    Function takes input that players want to say out loud for the next player
    :param player input is str, only from deck cards
    :param deck list of all cards

    :return player_say list that player choose to say out loud
    """
    player_say = []
    print("Choice the cards to Say out Loud! \n")
    while int(player_input) > len(player_say):
        say_choice = input("Choice the cards to say as many as you put: ")
        
        if len(player_say) == 0 and say_choice in deck:
            player_say.append(say_choice)
            continue
        
        elif len(player_say) > 0 and say_choice in deck and player_say[0][0] == say_choice[0] and say_choice not in player_say:
            player_say.append(say_choice)
            continue

        else:
            print("Please choice cards from deck and with same name \n")
            continue

    return player_say


def player_choice_cards(player_hands: list, table: list, player: int, deck: list): 
    """
    Shows the player the cards. Gets how many cards wants to put and which one.
    :param player_hands is list of players cards
    :param table list
    :param player - N of player that plays at this moment.
    :param deck list of cards

    :return player_hands - list of player cards, 
    :return table - list that player put on table
    :return player_outloud - list of cards player said outloud
    
    """       
    while True:
        player_in = player_hands[player]
        print(f"{player_in[0]} this are your cards {player_in[1:]} \n")

        player_input = input(f"Player please choose how many cards to select:\n ")
        if player_input.isnumeric():
            if len(player_in) > 5 and int(player_input) > 4:
                print("print write number up to 4 \n")
                continue

            elif len(player_in) < 5 and int(player_input) > len(player_in) - 1:
                print(f"print write number up to {len(player_hands[player])} \n")
                continue
            
            elif int(player_input) == 0:
                print("Please choice the possitive number \n")
                continue
            
            else:
                break
        
        else:
            print("print only numbers\n")
            continue
    
    count = 0
    while int(player_input) > count:
        print(player_in[1:])
        player_choice = input("Please choose the card:\n")
        
        if player_choice in player_in:
            table.append(player_choice)
            player_in.remove(player_choice)
            count += 1
            continue
        else:
            print("Please choice the cards you have\n")
            continue
        
    player_outloud = player_say(player_input, deck)
    
    return player_hands, table, player_outloud





    
