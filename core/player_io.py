def ask_player_action() -> str:
    while True:
        request = input("S or H ? : ")
        if request == "S":
            return "S"
        elif request == "H":
            return "H"
        

