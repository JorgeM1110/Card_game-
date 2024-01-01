import random
import deck
import card
import player
from boss_file import boss
from cards import squirrel
import check_input


def random_card(deck):
    """ From a deck of cards, pick a random card """
    if len(deck) <= 0:
        print("You have nothing left.")
        return None
    cardNum = random.randint(0, len(deck) - 1)
    card = deck.remove_card(cardNum)
    return card 

def show_hand(hand):
    """ Display current hand """
    print("\n~~~ Current Hand ~~~")
    for card in hand:
        print(card)
        print()

    print("~~~~~~~~~~~~~~~~~~~~\n")

def display_board(upcoming_attack, curr_attack, curr_hero):
    """ hows current board """
    print("\n~~~~~~~~ The Board ~~~~~~~~")
    counter = 1
    for index, card in enumerate(upcoming_attack):
        if card == None:
            print("None", end=" ")
        else:
            print(upcoming_attack[index].name, end=" ")
    print("-> Upcoming attack")
    print()

    counter = 2
    for index, card in enumerate(curr_attack):
        if card == None:
            print("None", end=" ")
        else:
            print(curr_attack[index].name, end=" ")
    print("-> Current attack")
    print()        
    
    counter = 3
    for index, card in enumerate(curr_hero):
        if card == None:
            print("None", end=" ")
        else:
            print(curr_hero[index].name, end=" ")
    print("-> Current hero")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def villain_turn(villain, upcoming_attack, curr_attack, curr_hero):
    """ Randomly add cards to upcoming_attack, pushes it to curr_attack and attacks hero """
    curr_attack = upcoming_attack
    upcoming_attack = [None,None,None,None]

    for index, card in enumerate(upcoming_attack):
        if random.randint(0, 1) == 1:
            upcoming_attack[index] = villain._deck.draw_card()
    
    display_board(upcoming_attack, curr_attack, curr_hero)

    for index, card in enumerate(curr_attack):
        if curr_attack[index] is not None:
            if curr_hero[index] is None:
                scale += card.power
                print(f"The villian's {card.name} dealt {card.power} damage to you ")
            else:
                card.take_damage(curr_attack[index].power)
                print("The villian's " + str(curr_attack[index].name) + " dealt " + str(curr_attack[index].power) + " damage to your " + str(card.name))

def hero_turn(hero_hand, play_deck, squirrel_count, my_squirrel, curr_hero, scale, upcoming_attack, curr_attack):
    """ Draws and sacerfices cards, and attacks villian """
    draw_card(hero_hand, play_deck, squirrel_count, my_squirrel)
    done = False
    while not done:
        print("1. Place a card down \n2. End turn")
        choice = check_input.range_int("Enter choice: ", 1, 2)
        if choice == 1:
            placeCard(hero_hand, curr_hero)
        elif choice == 2:
            heroAttack(curr_hero, curr_attack, scale)
            done = True
        display_board(upcoming_attack, curr_attack, curr_hero)

def draw_card(hero_hand, play_deck, squirrel_count, my_squirrel):
    """ User chooses a card of squirrel """
    show_hand(hero_hand)
    print("1. Draw from deck \n2. Draw a squirrel")
    choice = check_input.range_int("Enter choice: ", 1, 2)
    if choice == 1:
        hero_hand.append(random_card(play_deck))
        show_hand(hero_hand)
    elif choice == 2:
        if squirrel_count > 0:
            hero_hand.append(my_squirrel)
            show_hand(hero_hand)
            squirrel_count -= 1

def placeCard(hero_hand, curr_hero):
    """ Place and sacerfice cards """

    done_choosing = False
    has_enough = 0
    picked_card = None
    while not done_choosing:
        picked_card, index = check_input.choose_card("\nChoose a card from your hand", hero_hand, return_index=True)
        if picked_card.cost > 0: 
            for card in curr_hero:
                if card is not None:
                    has_enough += 1
        if has_enough >= picked_card.cost:
            hero_hand[index] = None
            done_choosing = True
        else:
            print("This card requires more creatures to sacerfice then what you currently have on the board.")
            has_enough = 0

    curr_sac = 0
    if curr_sac < picked_card.cost:
        print(f"\nThis card needs {picked_card.cost} sacerfices. Choose wisely.")
        while curr_sac < picked_card.cost:
            print("Which card would you like to sacerfice?")
            choice_card, index= check_input.choose_card("", curr_hero, return_index=True)
            curr_hero[index] = None
            curr_sac += 1
            print(f"You have sacerficed {choice_card.name} sacerfices: {curr_sac}/{picked_card.cost}")

    cardPlace = False
    while not cardPlace:
        print("Where would you like to place the card? Slot 1, 2, 3, or 4")
        choice = check_input.range_int("Enter choice: ", 1, 4)
        if curr_hero[choice - 1] is None:
            curr_hero[choice - 1] = picked_card
            cardPlace = True
        else:
            print("There is already a card in that slot, pick somewhere else.")

def heroAttack(curr_hero, curr_attack, scale):
    for index, card in enumerate(curr_hero):
        if card is not None:
            if curr_attack[index] is None:
                scale -= card.power
                print(f"You have done {card.power} to the villian!")
            else:
                curr_attack[index].take_damage(card.power)
                print(f"{card.name} delt {card.power} to {curr_attack.name}")
        else:
            print(f"No cards placed in slot {index + 1}")

def battle(hero, villian):
    print("---------- Battle Start! ----------")
    
    # Initializes starting deck and hand
    squirrel_count = 20
    my_squirrel = squirrel.Squirrel()
    hero_hand = []
    play_deck = hero._deck 
    play_deck.shuffle()
    for _ in range(4):
        hero_hand.append(random_card(play_deck))

    villian._deck.shuffle()
    
    scale = 0
    turn = 1
    upcoming_attack = [None, None, None, None]
    curr_attack =     [None, None, None, None]
    curr_hero =     [None, None, None, None]

    while scale > -5 and scale < 5:
        print(f"Scale: {scale}")
        # villian turn
        if turn == 1:
            villain_turn(villian, upcoming_attack, curr_attack, curr_hero)
            turn = 0
            print(f"Scale: {scale}")
        # Hero turn
        elif turn == 0:
            hero_turn(hero_hand, play_deck, squirrel_count, my_squirrel, curr_hero, scale, upcoming_attack, curr_attack)
            turn = 1
            print(f"Scale: {scale}")


    # To-do
    """
        add a loop to every input checking if the user input what we expect or make a check_input
        player sacerficing a card to gain a cost, cost is per turn meaning the cost gets reset to 0 every turn (If we want to follow how the actual game works)
            - Each card sacerficed in play doesn't return to deck (Unless we want to add it) but gets added back after battle
            - Each card will equal to 1 sacerfice, doesn't matter how much power or health it does 
        placing a card in the currPlayer where the card is now in play and will take and deal damage
            - checking if a card is already there (don't want to overwrite)
            - If currPlayer is full, player can only either sacerfice, draw a squirrel, or end turn 
        At each end turn, whoever turn is it, their card deals damage to the opposing entity 
            - Add/Subtract to scale if there is no card blocking or the card attack is airborne and the card opposing can't block it 
        add the villian turn
            - Randomly choose an enemy card and place it in it's upcoming_attack where the player can see what is comming next
            - Move the upcoming_attack to curr_attack and replace upcoming_attack if we want it to continue, so we can have 2 - 3 rounds where the villian has a chance to places a card 
            - Deals damage to player or player's card 
        Once everything works (so just simple health, power, and cost), work on sigil, and items
        Maybe add a put down card, if the user chooses a card but then changes their mind
    """
        