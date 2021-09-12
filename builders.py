import random
import colors


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
            for c in range(1, 14):
                for h in range(0, 4):
                    i = h + (c-1)*4 * d
                    deck[i] = self.__build_card(h, c, i)
        return deck

    def __build_card(self, h, c, i):
        value = c if (c < 10) else 10
        color = colors.R_CARD_COL if (h % 2) else colors.K_CARD_COL
        suits = ["♠", "♥", "♣", "♦"]
        honors = ["J", "Q", "K"]
        face = str(c) if (c < 11) else honors[c-11]
        if (face == "1"):
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


"""
    def blackjack(self):
        self.card_stack.pop(0)
        self.card_stack.pop(50)
        return self.reference[0], self.reference[51]
"""
