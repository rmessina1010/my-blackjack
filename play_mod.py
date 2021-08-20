import random


def play():
    house_pt = 0
    player_pt = 0
    player_hand = 0

    result: 0
    if player_pt > 21 or house_pt > player_pt:
        result = -1
        print("You Lose!!")
    elif player_pt > house_pt:
        result = 1.5 if player_hand == 2 else 1
        if (result == 1.5):
            print("BLACKJACK!!!")
        print("You Win!!")
    else:
        print("PUSH")
    # return random.choice([-1, -1, -1, 0, 1, 2])
    return result


def tally(hand):
    sum = 0
    aces = 0
    for card in hand:
        if card.face == "A":
            aces += 1
        else:
            sum += card.value
    sum = sum + (aces * 11)
    for x in range(0, aces):
        if sum > 21:
            sum -= 10

    return sum
