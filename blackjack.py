from play_mod import exit_game, play, exit_message
from builders import Deck_Stack
from views_mod import show_balance
import colors

initial_bal = 500
balance = initial_bal
ref_deck = Deck_Stack(1)
message = None
# print(ref_deck.reference)

while True:
    print(f"\n===={colors.TITLE_COL}BLACKJACK!\033[0m====")
    show_balance(balance)
    wager = input("What do you wager? ").lower()
    if (wager == 'q' or wager == 'quit'):
        message = exit_message(balance, initial_bal)
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
    print("Playing blackjack...\n")
    play_hand = play(ref_deck)
    # forced exit
    if play_hand == None:
        message = exit_message(balance, initial_bal)
        break
    ##
    balance += int(wager * play_hand)
    # print(ref_deck.remaining_cards())
    if balance < 1:
        message = "You are broke!!"
        break
show_balance(balance)
exit_game(message)
