from play_mod import play
from builders import Deck_Stack

balance = 500
ref_deck = Deck_Stack(1)

while True:
    print("\n====BLACKJACK!====")
    print("Your Balance is:", balance)
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
    balance += wager * play(ref_deck)
    print(ref_deck.remaining_cards())
    if balance < 1:
        print("Your Balance is:", balance)
        print("You are broke!!")
        break
print("Goodbye.")
