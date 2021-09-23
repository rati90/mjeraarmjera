from service.shuffle import shuffle_cards
from service.playerNumbersChoice import player_numbers
from service.playerChoice import player_choice_cards
from service.trustorNot import do_you_trust

deck = [
        '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks', 'as',
        '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh', 'ah',
        '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd', 'ad',
        '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc', 'ac'
    ]

table = []    


def main():
    shuffle_cards(deck)
    player_cards_and_numbers = player_numbers(deck)

    print(player_cards_and_numbers)

    for player in range(player_cards_and_numbers[1]):

        player_hands_table_outloud = player_choice_cards(player_cards_and_numbers[0], table, player, deck)


        print(player_hands_table_outloud)
        
        do_you_trust(player_hands_table_outloud, player)



if __name__ == "__main__":
    main()