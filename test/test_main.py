from io import StringIO

from service.shuffle import shuffle_cards
from service.playerNumbersChoice import player_numbers, player_names
from service.playerChoice import player_choice_cards, player_choice_outloud, player_say
from service.trustorNot import do_you_trust, hands_table_clear
from service.playerHandCheck import check_end, check_hand_zero

deck = [ 
        '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks', 'as',
        '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh', 'ah',
        '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd', 'ad',
        '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc', 'ac'
        ]

players_hands = ([
                 ['3c', '4h', '2d', '7s', '9c', '6d', '9h', 'jc', 'jh', '2h', '6h', '7h', '4c'], 
                 ['8h', '3s', 'jd', '10s', '7c', '9d', 'js', 'qs', '3d', '5d', '3h', '10h', 'ks'], 
                 ['5s', 'qc', '10c', '8s', '4d', 'ah', '4s', '5h', 'as', 'qd', 'kh', '2c', '8d'], 
                 ['10d', 'ac', '6s', '9s', '7d', 'kc', 'qh', '6c', '8c', 'ad', '5c', 'kd', '2s']],
                 4)



player = 0
table = []



#............     shuffle      .............
def test_shuffle_cards():
        cards = shuffle_cards(deck)

        assert len(cards) == 52


#............    playerNumbersChoice     ..............
def test_player_numbers(monkeypatch): 
        monkeypatch.setattr('sys.stdin', StringIO('4\n'))
        players_cards = player_numbers(deck)
        
        assert len(players_cards[0]) == 4


def test_player_names():
        player_position = player_names(players_hands)

        assert  player_position[0][1][0][9] == '2' 


#............    playerChoice     ..............
#ორ ინფუთის შეთხვევაში როგორ ვაწვდი?
"""def test_player_choice_cards(monkeypatch):
        monkeypatch.setattr('sys.stdin', number_inputs2)
        cards = player_choice_cards(players_hands, table, player, deck)

        assert len(cards[1]) == 4"""

#იგივე პრობლემა. ორჯერ უნდა მიწოდება ინფუთის
"""def test_player_choice_outloud(monkeypatch):
        
        player_input = '1'
        player_in = ['3c', '4h', '2d', '7s', '9c', '6d', '9h', 'jc', 'jh', '2h', '6h', '7h', '4c']
        table = ['3c']
        monkeypatch.setattr('sys.stdin', number_inputs2)
        choice = player_choice_outloud(player_input, player_in, table, deck)
        assert choice == '3c'"""

def test_player_say(monkeypatch):
        monkeypatch.setattr('sys.stdin', StringIO('3s\n'))
        choice_cards = player_say("1", deck)

        assert  choice_cards[0] == "3s"


#............    trustorNot     ..............

"""def test_do_you_trust(monkeypatch):
        monkeypatch.setattr('sys.stdin', StringIO('Yes\n'))
        player_hands_table_say = (players_hands[0], ['2s, 2d'], ["2s, 2d"])

        choice = do_you_trust(player_hands_table_say, 0)

        assert len(choice[1]) == 0"""

def test_hands_table_clear():

        table = hands_table_clear(['2s, 2d'], ["2s, 2d"])

        assert len(table[0]) == 0 and len(table[1]) == 0
        

#............    HandCheck     ..............
def test_check_end():
        player_hands_table_say =([["Player N 2",'10d', '5c', 'kd', '2s']],
                                ['2s', '2d'], 
                                ["2s", "2d"])

        hands =  check_end( player_hands_table_say)

        assert hands == None


def test_check_hand_zero():
        player_hands_table_say =([["Player N 1", '2c'],
                                ["Player N 2",'10d', '5c', 'kd', '2s'],
                                ["Player N 3"]],
                                ['2s', '2d'], 
                                ["2s", "2d"])

        hand = check_hand_zero(player_hands_table_say)
        
        assert len(hand[0]) == 2 and len(hand[1]) == 2 and len(hand[2]) == 2


