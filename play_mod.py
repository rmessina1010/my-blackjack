import random
from views_mod import show_draw, show_hands


def play(ref_deck):
    player_hand = []
    house_hand = []
    reshuffle_at = ref_deck.depth * 52 * .25

    result = 0

    deal_in(ref_deck, house_hand, player_hand)
    house_pt = 0
    player_pt = user_plays(player_hand, ref_deck, house_hand)

    if player_pt > 21 or (house_pt > player_pt and house_pt < 22):
        result = -1
    elif player_pt > house_pt:
        result = 1.5 if len(player_hand) == 2 else 1
    elif player_pt == 21 and len(player_hand) == 2 and house_pt == 21 and len(house_hand) != 2:
        result = 1.5
    if result == 1.5:
        print("BLACKJACK!!!")
    if result > 0:
        print("You Win!")
    elif result < 0:
        print("You lose!")
    else:
        print("PUSH!")
      # return random.choice([-1, -1, -1, 0, 1, 2])
    return result


def house_plays(house_pt, player_pt, house_hand, ref_deck):
    while player_pt < 22 and house_pt < 17 and house_pt < player_pt:
        new_card = ref_deck.draw_card()
        show_draw("The house ", new_card)
        house_hand.append(new_card)
        house_pt += new_card["value"]
    return house_hand


def user_plays(player_hand,  ref_deck, house_hand):
    print(player_hand)
    player_pt = tally(player_hand)
    while True:
        choice = False
        while choice != "h" and choice != "s":
            choice = input("[H]it or [S]tand? ").lower()[0]
        if choice == "s":
            return player_pt
        new_card = ref_deck.draw_card()
        show_draw("You ", new_card)
        player_hand.append(new_card)
        player_pt = tally(player_hand)
       # print(player_hand)
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
    for i in range(2):
        house.append(ref_deck.draw_card())
        player.append(ref_deck.draw_card())
    show_hands(house, player, True)

# note: run tally operation after each draw!!!
