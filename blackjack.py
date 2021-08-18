import random

balance = 500

while True:
    print("====BLACKJACK!====")
    print("Your Balance is:", balance)
    wager = input("What do you wager? ")
    if (wager.lower() == 'quit'):
        break
    try:
        wager = int(wager)
    except ValueError:
        wager = 0
    if (wager < 1 or wager > balance):
        print("Invalid bet!!!")
        continue
    print("playing blackjack")
    balance += wager * random.choice([-1, -1, -1, 0, 1, 2])
    if balance < 1:
        print("Your Balance is:", balance)
        print("You are broke!!")
        break
print("Goodbye.")
