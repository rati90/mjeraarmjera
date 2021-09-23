

def player_choice_cards(player_cards, table):
    #choice cards to put in table, you can choice 1 to 4 cards
    while True:
        player_input = input("Please choose how many cards to select: ")
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
        print(player_cards)
        player_choice = input("Please choose the card:")
        

        if player_choice in player_cards:
            table.append(player_choice)
            player_cards.remove(player_choice)
            count += 1
            continue
        else:
            print("Please choice the cards you have")
            continue

