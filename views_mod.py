import colors


def show_hands(house, player, hide):
    house_str = ""
    player_str = ""
    try:
        for card in house:
            if hide and house_str == "":
                house_str = "?? | "
                continue
            house_str += card['color']+card['face'] + \
                card['suit'] + colors.DEF_COL + " | "
        for card in player:
            player_str += card['color']+card['face'] + \
                card['suit'] + colors.DEF_COL + " | "
        print("\nThe house has: " + house_str)
        print("You have: " + player_str + "\n")
    except (KeyError, TypeError):
        print("No card.")
        return


def show_draw(who, card):
    try:
        print(who, "drew a " + card['color'] +
              card['face'] + card['suit'] + "\033[0m")
    except (TypeError, KeyError):
        print("No card.")
        return


def show_balance(balance):
    print(f"Your Balance is: ${balance:.2f}")
