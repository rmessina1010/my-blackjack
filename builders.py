import random


class Deck_Stack:
    def __init__(self, depth):
        self.depth = depth
        self.reference = self.__build_deck()
        self.refresh_stack()

    def remaining_cards(self):
        return len(self.card_stack)

    def draw_card(self):
        l = len(self.card_stack)
        if l < 1:
            return False
        i = random.randint(0, l-1)
        card = self.card_stack.pop(i)
        return self.reference[card]

    def refresh_stack(self):
        self.card_stack = self.__build_deck_alias(self.depth)

    def __build_deck(self):
        deck = self.__build_deck_alias(self.depth)
        for d in range(1, 1+self.depth):
            for c in range(0, 13):
                for h in range(0, 4):
                    i = h + c*4 * d
                    deck[i] = self.__build_card(h, c, i)
        return deck

    def __build_card(self, h, c, i):
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

    def __build_deck_alias(self, depth):
        return list(range(0, 52*depth))
