#from service.shuffle import shuffle_cards
from service import playerNumber



def test_shuffle_cards(deck):
    result = shuffle_cards(deck)
    assert len(result) == 52


