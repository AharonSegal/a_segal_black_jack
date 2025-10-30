#COMPLETE
def calculate_hand_value(hand: list[dict]) -> int:
    hand_sum = 0
    for card in hand:
        value = card["rank"]
        if value == "A":
            hand_sum += 1
        elif isinstance(value, str):
            hand_sum += 10
        else:
            hand_sum += value
    return hand_sum 

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    return

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    return

def ask_player_action() -> str:
    return

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    return




###############--------------------

player = {"hand": [ ] }
dealer = {"hand": [ ] }

deck = [{'rank': 3, 'suit': 'H'}, {'rank': 'K', 'suit': 'S'}, {'rank': 'Q', 'suit': 'S'}, {'rank': 5, 'suit': 'C'}, {'rank': 'J', 'suit': 'D'}, {'rank': 'A', 'suit': 'H'}, {'rank': 'K', 'suit': 'C'}, {'rank': 2, 'suit': 'H'}, {'rank': 8, 'suit': 'S'}, {'rank': 10, 'suit': 'D'}, {'rank': 5, 'suit': 'S'}, {'rank': 4, 'suit': 'D'}, {'rank': 'J', 'suit': 'H'}, {'rank': 6, 'suit': 'S'}, {'rank': 3, 'suit': 'S'}, {'rank': 'Q', 'suit': 'C'}, {'rank': 9, 'suit': 'C'}, {'rank': 5, 'suit': 'D'}, {'rank': 8, 'suit': 'C'}, {'rank': 2, 'suit': 'C'}, {'rank': 'Q', 'suit': 'H'}, {'rank': 7, 'suit': 'H'}, {'rank': 'J', 'suit': 'C'}, {'rank': 5, 'suit': 'H'}, {'rank': 8, 'suit': 'H'}, {'rank': 9, 'suit': 'D'}, {'rank': 'J', 'suit': 'S'}, {'rank': 6, 'suit': 'C'}, {'rank': 4, 'suit': 'H'}, {'rank': 3, 'suit': 'C'}, {'rank': 4, 'suit': 'C'}, {'rank': 10, 'suit': 'H'}, {'rank': 10, 'suit': 'S'}, {'rank': 'K', 'suit': 'H'}, {'rank': 4, 'suit': 'S'}, {'rank': 7, 'suit': 'D'}, {'rank': 2, 'suit': 'S'}, {'rank': 9, 'suit': 'H'}, {'rank': 'A', 'suit': 'D'}, {'rank': 2, 'suit': 'D'}, {'rank': 7, 'suit': 'C'}, {'rank': 'K', 'suit': 'D'}, {'rank': 'Q', 'suit': 'D'}, {'rank': 8, 'suit': 'D'}, {'rank': 'A', 'suit': 'S'}, {'rank': 3, 'suit': 'D'}, {'rank': 10, 'suit': 'C'}, {'rank': 'A', 'suit': 'C'}, {'rank': 6, 'suit': 'H'}, {'rank': 6, 'suit': 'D'}, {'rank': 9, 'suit': 'S'}, {'rank': 7, 'suit': 'S'}]

hand = [{'rank': 'K', 'suit': 'S'}, {'rank': 8, 'suit': 'D'}, {'rank': "A", 'suit': 'C'}]
