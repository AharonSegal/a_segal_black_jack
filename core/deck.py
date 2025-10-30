import random

def build_standard_deck() -> list[dict]:
    VALUES = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    SUITS = ["H","C","D","S"]

    deck = []
    for value in VALUES:
        for suit in SUITS:
            card = {"rank" : value, "suit" : suit}
            deck.append(card)

    return deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for _ in range(swaps):
        # get idecies
        i = random.randint(0,51)
        card_i = deck[i] 


        while True:
            j = random.randint(0,51)
            #validate indecies
            if i == j: 
                continue
            # test "H"
            if card_i["suit"] == "H" and j % 5 == 0: 
                break
            # test "C"
            elif card_i["suit"] == "C" and j % 3 == 0:
                break
            # test "D"
            elif card_i["suit"] == "D" and j % 2 == 0:
                break
            # test "S"
            elif card_i["suit"] == "S" and j % 7 == 0:
                break
            else:
                continue

        temp =deck[i]
        deck[i] = deck[j]
        deck[j] = temp
        
    return deck

        
