from itertools import count


deck = [
        '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'js', 'qs', 'ks', 'as',
        '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'jh', 'qh', 'kh', 'ah',
        '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'jd', 'qd', 'kd', 'ad',
        '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'jc', 'qc', 'kc', 'ac'
    ]

table = []    


def shuffle():
   pass 

n = 4
lst = []
def player_number(n):
    number = len(deck) // n 
    count = 1
    for i in range(0, 52, number):
        lst.append([f"player{count}", deck[i:number+i]])
        count += 1
    print(lst)

player_number(n)   


# irchevs da chadis magidaze
def player_choice_cards():
    pass


def player_say():
    pass


def mjera_armjera_damateba():
    pass


def mjera():
    pass


def armjera():
    pass


def damateba():
    pass