import random


def play():
    house_pt = 0
    player_pt = 0
    player_hand = 0

    result: 0
    if player_pt > 21 or house_pt > player_pt:
        result = -1
    elif player_pt > house_pt:
        result = 1.5 if player_hand == 2 else 1

    # return random.choice([-1, -1, -1, 0, 1, 2])
    return result
