def show_hands(house, player, hide):
    house_str = ""
    player_str = ""
    try:
        for card in house:
            if hide and house_str == "":
                house_str = "?? | "
                continue
            house_str += card['face'] + card['suit'] + " | "
        for card in player:
            player_str += card['face'] + card['suit'] + " | "
        print("\nThe house has: " + house_str)
        print("You have: " + player_str + "\n")
    except (KeyError, TypeError):
        print("No card.")
        return


def show_draw(who, card):
    try:
        print(who, "drew a " + card['face'] + card['suit'])
    except (TypeError, KeyError):
        print("No card.")
        return


def show_balance(balance):
    print(f"Your Balance is: ${balance:.2f}")
