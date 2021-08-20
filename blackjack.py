from play_mod import play
from builders import build_deck

balance = 500
ref_deck = build_deck()

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
    print("playing blackjack")
    balance += wager * play()
    if balance < 1:
        print("Your Balance is:", balance)
        print("You are broke!!")
        break
print("Goodbye.")
