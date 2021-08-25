import random
from views_mod import show_draw


def play():
    house_pt = 0
    player_pt = 0
    player_hand = []
    house_hand = []

    result: 0
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


def house_plays(house_pt, player_pt, house_hand, alias):
    while player_pt < 22 and house_pt < 17 and house_pt < player_pt:
        new_card = draw_from_alias(alias)
        show_draw("The house ", new_card)
        house_hand.append(new_card)
        house_pt += new_card.value
    return house_hand


def user_plays(player_hand, player_pt, alias):
    while True:
        choice = input("Hit or Stand? ")
        if choice.lower()[0] == "s":
            break
        new_card = draw_from_alias(alias)
        show_draw("You ", new_card)
        player_pt += new_card.value
        player_hand.append(new_card)
        if player_pt > 21:
            print("You Bust!!")
            break


def tally(hand):
    sum = 0
    aces = 0
    for card in hand:
        if card.face == "A":
            aces += 1
        else:
            sum += card.value
    sum = sum + (aces * 11)
    for i in range(0, aces):
        if sum > 21:
            sum -= 10

    return sum


def draw_from_alias(alias):
    l = len(alias)
    if l < 1:
        return False
    i = random.randint(0, l-1)
    card = alias.pop(i)
    return card
