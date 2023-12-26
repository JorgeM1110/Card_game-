import random

def random_card(deck):
    if len(deck) == 0:
        print("You have nothing left.")
        return None
    cardNum = random.randint(0, len(deck) - 1)
    card = deck.removeCard(cardNum)
    return card 

def show_hand(hand):
    for card in hand:
        print(card)

def battle(hero, boss):
    print("~~~ Battle Start! ~~~~")

    # Player hand
    squirrelCount = 20
    hero._deck.shuffle()
    for _ in range(4):
        heroHand = random_card(hero._deck)
    
    # Cards that will be in play next round
    boss._deck.shuffle()
    upcomingAttack = []
    for _ in range(4):
        if random.randint(0, 1) == 1:
            card = random_card(boss_deck)
            if card:
                upcomingAttack.append(card)
        