from play_mod import exit_game, play
from builders import Deck_Stack
from views_mod import show_balance

balance = 500
ref_deck = Deck_Stack(1)
# print(ref_deck.reference)

while True:
    print("\n====BLACKJACK!====")
    show_balance(balance)
    wager = input("What do you wager? ").lower()
    if (wager == 'q' or wager == 'quit'):
        break
    try:
        wager = int(wager)
    except ValueError:
        print("Invalid bet!!!")
        continue
    if (wager < 1):
        print("You must wager at least $1!")
        continue
    if (wager > balance):
        print(
            f"You don't have enough funds to cover this bet!\nThe maximum bet is ${balance:.2f}")
        continue
    print("Playing blackjack...")
    balance += int(wager * play(ref_deck))
    # print(ref_deck.remaining_cards())
    if balance < 1:
        show_balance(balance)
        print("You are broke!!")
        break
exit_game()
