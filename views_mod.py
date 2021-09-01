def show_hands(house, player, hide):
    house_str = ""
    player_str = ""
    for card in house:
        if card is False:
            return
        if hide and house_str == "":
            house_str = "?? | "
            continue
        house_str += card['face'] + card['suit'] + " | "
    for card in player:
        player_str += card['face'] + card['suit'] + " | "
    print("\nThe house has: " + house_str)
    print("You have: " + player_str + "\n")


def show_draw(who, card):
    if card is False:
        return
    print(who + " drew a " + card['face'] + card['suit'])
