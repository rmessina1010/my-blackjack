def hit_or_stand(total, deck, tolerance=50):
    total = 21 - total
    if total < 1:
        bust_chance = 100
    if total > 10:
        bust_chance = 0
    else:
        ace_val = 11 if total > 10 else 1
        remain = deck.remaining_cards()
        busters = 0
        for ci in deck.card_stack:
            card = deck.reference[ci]
            val = ace_val if card['face'] == "A" else card['value']
            if val > total:
                busters += 1
        bust_chance = busters/remain * 100
    return ("hit" if bust_chance < tolerance else "stand")+" ["+str(bust_chance)+"]"
