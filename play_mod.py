from views_mod import show_draw, show_hands
from calc_odds import hit_or_stand
import colors


def play(ref_deck):
    player_hand = []
    house_hand = []
    reshuffle_at = (18, 23, 26)
    reshuffle_idx = ref_deck.depth-1 if ref_deck.depth < 3 else 2

    if ref_deck.remaining_cards() < reshuffle_at[reshuffle_idx]:
        print("---New card deck!---")
        ref_deck.refresh_stack()

    result = 0

    deal_in(ref_deck, house_hand, player_hand)
    player_pt = user_plays(player_hand, ref_deck, house_hand)
    if (player_pt == None):
        return
    house_pt = house_plays(player_pt, house_hand, ref_deck)
    show_hands(house_hand, player_hand, False)

    if player_pt > 21 or (player_pt < house_pt < 22):
        if (house_pt == 21 and len(house_hand) == 2):
            print("HOUSE HAS BLACKJACK!!!")
        result = -1
    elif player_pt == 21 and len(player_hand) == 2:
        result = 0 if (house_pt == 21 and len(house_hand) == 2) else 1.5
    elif house_pt > 21 or (house_pt < player_pt < 22):
        result = 1

    if result == 1.5:
        print("YOU HAVE BLACKJACK!!!")
    if result > 0:
        print("You Win!")
    elif result < 0:
        print("You lose!")
    else:
        print("PUSH!")
    return result


def house_plays(player_pt, house_hand, ref_deck):
    print(f"\n---{colors.TURN_COL}House's Turn{colors.DEF_COL}---")
    house_pt = tally(house_hand)
    while house_pt < 17 and (house_pt < player_pt < 22):
        new_card = eodeck_check(ref_deck.draw_card())
        show_draw("The house ", new_card)
        house_hand.append(new_card)
        house_pt += new_card["value"]
    if house_pt > 21:
        print("House Busts!!")
    return house_pt


def user_plays(player_hand,  ref_deck, house_hand):
    print(f"---{colors.TURN_COL}Your Turn{colors.DEF_COL}---")
    # print(player_hand)
    player_pt = tally(player_hand)
    while True:
        choice = False
        while choice != "h" and choice != "s" and choice != "q" and choice != "?":
            if player_pt == 21:
                return player_pt
            choice = input("[H]it or [S]tand? ")
            choice = None if len(choice) < 1 else choice[0].lower()
        if choice == "?":
            suggestion = hit_or_stand(player_pt, ref_deck)
            print("I suggest you " + suggestion)
            continue
        if choice == "q":
            return
        if choice == "s":
            return player_pt
        new_card = eodeck_check(ref_deck.draw_card())
        show_draw("You ", new_card)
        player_hand.append(new_card)
        player_pt = tally(player_hand)
        # print(player_hand)
        # print(player_pt)
        show_hands(house_hand, player_hand, True)
        if player_pt > 21:
            print("You Bust!!")
            return player_pt


def tally(hand):
    sum = 0
    aces = 0
    for card in hand:
        if card['face'] == "A":
            aces += 1
        else:
            sum += card['value']
    sum = sum + (aces * 11)
    for i in range(0, aces):
        if sum > 21:
            sum -= 10

    return sum


def deal_in(ref_deck, house, player):
    """
        test = ref_deck.blackjack()
        player.extend(test)
    """
    print(f"---{colors.TURN_COL}Dealing Hands{colors.DEF_COL}---")
    for i in range(2):
        house.append(eodeck_check(ref_deck.draw_card()))
        player.append(eodeck_check(ref_deck.draw_card()))
    show_hands(house, player, True)


def exit_game(message=False):
    if message:
        print(message)
    print("Goodbye.")
    exit()


def eodeck_check(card):
    if card == False:
        exit_game("No cards left to play.")
    return card


def exit_message(balance, initial_bal):
    if (initial_bal == balance):
        return "You broke even."
    return "You come out ahead by $" + str(balance - initial_bal) if initial_bal < balance else "You lost a total of $" + str(initial_bal - balance)
