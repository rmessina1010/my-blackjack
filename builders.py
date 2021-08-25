import random


def build_deck():
    deck = build_deck_alias()
    for c in range(0, 13):
        for h in range(0, 4):
            i = h + c*4
            deck[i] = build_card(h, c, i)
    return deck


def build_card(h, c, i):
    value = c if (c < 10) else 10
    color = "white" if (h % 2) else "red"
    suits = ["♠", "♥", "♣", "♦"]
    honors = ["J", "Q", "K"]
    face = str(c) if (c < 10) else honors[c-10]
    if (face == "0"):
        face = "A"
    card = {
        "value": value,
        "face": face,
        "suit": suits[h],
        "color": color,
        "icon": None,
        "id": i
    }
    return card


def build_deck_alias():
    return list(range(0, 52))
