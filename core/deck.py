import random

#COMPLETE
def build_standard_deck() -> list[dict]:
    VALUES = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    SUITS = ["H","C","D","S"]

    deck = []
    for value in VALUES:
        for suit in SUITS:
            card = {"rank" : value, "suit" : suit}
            deck.append(card)

    return deck

# TODO:
# def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
#     swapped = 0

#     #remove 
#     swaps = 10
#     while swapped <= swaps:
#         # get idecies
#         i = random.randint(0,51)
#         card_i = deck[i] 

#         while True:
#             card_i = deck[i] 
#             j = random.randint(0,51)

#             print("---------TEST-------------")
#             print(f" i = {card_i}")
#             print(f" j = {j}")

#             #validate indecies
#             print("idx-----",i," : " ,j)
#             if i != j:
#                 continue

#             # test "H"
#             if card_i["suit"] == "H" and j % 5 == 0: 
#                 print("H")
#                 break
#             # test "C"
#             elif card_i["suit"] == "C" and j % 3 == 0:
#                 print("C")
#                 break
#             # test "D"
#             elif card_i["suit"] == "D" and j % 2 == 0:
#                 print("D")
#                 break
#             # test "S"
#             elif card_i["suit"] == "S" and j % 7 == 0:
#                 print("S")
#                 break
#             else:
#                 print("none valid")
#                 continue
        
#         print("--VALID CARD -", card_i, j)

#         break


#TEMPORARY 
def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    return random.shuffle(deck)





