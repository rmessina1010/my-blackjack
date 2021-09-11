from play_mod import exit_game, play
from builders import Deck_Stack
from views_mod import show_balance

balance = 500
ref_deck = Deck_Stack(1)
# print(ref_deck.reference)

while True:
    print("\n====BLACKJACK!====")
    show_balance(balance)
    wager = input("What do you wager? ")
    if (wager.lower() == 'q' or wager.lower() == 'quit'):
        break
    try:
        wager = int(wager)
    except ValueError:
        wager = 0
    if (wager < 1 or wager > balance):
        print("Invalid bet!!!")
        continue
    print("Playing blackjack...")
    balance += int(wager * play(ref_deck))
    # print(ref_deck.remaining_cards())
    if balance < 1:
        show_balance(balance)
        print("You are broke!!")
        break
exit_game()
