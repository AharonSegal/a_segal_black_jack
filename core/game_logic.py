from core.player_io import ask_player_action

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
    for _ in range(2):
        player["hand"].append(deck.pop())
        dealer["hand"].append(deck.pop())
    return

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"]) < 17:
        dealer["hand"].append(deck.pop())
        if calculate_hand_value(dealer["hand"]) > 21:
            return False
    return True 

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)

    while True:

        print(f"you current hand: {player["hand"]} -> sums to {calculate_hand_value(player["hand"])}")
        choice = ask_player_action()
        if choice == "H":
            player["hand"].append(deck.pop())
            print(f"you current hand: {player["hand"]} -> sums to {calculate_hand_value(player["hand"])}")
            if calculate_hand_value(player["hand"]) > 21:
                return print(f"player_1 you have lost - your hands sum is {calculate_hand_value(player["hand"])}")
        else:
            break
            
    dealer_status = dealer_play(deck,dealer)
    if not dealer_status:
        print(f"player_1 you have won !! the dealers hand is {calculate_hand_value(dealer["hand"])}")
    else:
        if calculate_hand_value(player["hand"]) > calculate_hand_value(dealer["hand"]):
            return print(f"player_1 you have won !! - your hands sum is {calculate_hand_value(player["hand"])} the dealers hand is {calculate_hand_value(dealer["hand"])}")
        elif calculate_hand_value(player["hand"]) < calculate_hand_value(dealer["hand"]):
            return print(f"player_1 you have lost - your hands sum is {calculate_hand_value(player["hand"])} the dealers hand is {calculate_hand_value(dealer["hand"])}")
        else:
            return print(f"its a TIE - your hands sum is {calculate_hand_value(player["hand"])} the dealers hand is {calculate_hand_value(dealer["hand"])}")

