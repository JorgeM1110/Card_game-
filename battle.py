import random
import deck
import card
import player
from boss_file import boss
from cards import shrimp
import check_input
from terminal_utils import clear_terminal, pause, delay_print, delay_input, delay

def choose_card(text, deck, return_index=False):
    if all(card is None for card in deck):
        return None
    else:
        print(text)
        counter = 1 
        for card in deck:
            print(f"{counter}. {card}")
            print()
            counter += 1

        valid = False
        while not valid:
            choice = check_input.range_int("Enter choice: ", 1, counter - 1)

            if deck[choice - 1] is not None:
                if return_index:
                    return deck[choice - 1], choice - 1
                else:
                    return deck[choice - 1]
            else:
                print("There's no card there, choose again. ")

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

def display_board(upcoming_attack, curr_attack, curr_hero, scale):
    """ hows current board """
    print(f"\nScale: {scale}")
    print("~~~~~~~~ The Board ~~~~~~~~")
    counter = 1
    for index, card in enumerate(upcoming_attack):
        if card is None:
            print("None", end=" ")
        else:
            print(card.name, end=" ")
    print("-> Upcoming attack")
    print()

    counter = 2
    for index, card in enumerate(curr_attack):
        if card is None:
            print("None", end=" ")
        else:
            print(card.name, end=" ")
    print("-> Current attack")
    print()        
    
    counter = 3
    for index, card in enumerate(curr_hero):
        if card is None:
            print("None", end=" ")
        else:
            print(card.name, end=" ")
    print("-> Current hero")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def villian_draw_card(villian, upcoming_attack):
    """ Randomly add cards to upcoming_attack """
    for index, card in enumerate(upcoming_attack):
        if random.randint(0, 1) == 1 and upcoming_attack[index] is None:  
            upcoming_attack[index] = villian._deck.draw_card()

def villian_play_card(upcoming_attack, curr_attack):
    """ Pushes it to curr_attack"""
    
    for index in range(len(upcoming_attack)):
        if upcoming_attack[index] is not None and curr_attack[index] is None:
            curr_attack[index] = upcoming_attack[index]
            if upcoming_attack[index] is not None:
                upcoming_attack[index] = None

def villian_attack(upcoming_attack, curr_attack, curr_hero, scale):
    """ attacks hero """
    for index, card in enumerate(curr_attack):
        if card is not None:
            if curr_hero[index] is None:
                scale -= card.power
                print(f"The villian's {card.name} dealt {card.power} damage to you ")
            else:
                if curr_hero[index].barrier == False:
                    curr_hero[index].take_damage(curr_attack[index].power)
                    print("The villian's " + str(curr_attack[index].name) + " dealt " + str(curr_attack[index].power) + " damage to your " + str(curr_hero[index].name))
                    if curr_hero[index].hp == 0:
                        print(f"villian {card.name} has slayed your {curr_hero[index].name}")
                        curr_hero[index] = None
                else:
                    print(f"{curr_hero[index].name} has a barrier, and {str(curr_attack[index].name)} dealt 0 damage")
                    print(f"{curr_hero[index].name} barrier broke")
                    curr_hero[index].barrier = False 
    display_board(upcoming_attack, curr_attack, curr_hero, scale)
    return scale 

def villian_turn(villian, upcoming_attack, curr_attack, curr_hero, scale):
    """ Pushes it to curr_attack and attacks hero """

    villian_draw_card(villian, upcoming_attack)
    return villian_attack(upcoming_attack, curr_attack, curr_hero, scale) 
 
def hero_turn(hero_hand, play_deck, shrimp_count, my_shrimp, curr_hero, scale, upcoming_attack, curr_attack, villian):
    """ Draws and sacerfices cards, and attacks villian """
    draw_card(hero_hand, play_deck, shrimp_count, my_shrimp)
    sigil = False 
    done = False
    while not done:
        print("\n1. Look at your cards \n2. Look at board \n3. Place a card down \n4. Use an item \n5. Use Sigil \n6. End turn")
        choice = check_input.range_int("Enter choice: ", 1, 6)
        if choice == 1:
            show_hand(hero_hand)
        elif choice == 2:
            display_board(upcoming_attack, curr_attack, curr_hero, scale)
        elif choice == 3:
            placeCard(hero_hand, curr_hero)
            display_board(upcoming_attack, curr_attack, curr_hero, scale)
        elif choice == 4:
            use_item(hero_hand, play_deck,curr_hero)

        elif choice == 5:
            if sigil is False:
                use_sigil(villian, upcoming_attack, curr_attack, curr_hero, scale)
                sigil = True
            else: 
                print("\nYou can only use one sigil per turn, good luck!")
        else:
            villian_play_card(upcoming_attack, curr_attack)
            display_board(upcoming_attack, curr_attack, curr_hero, scale)
            done = True
    return heroAttack(curr_hero, curr_attack, scale)

def draw_card(hero_hand, play_deck, shrimp_count, my_shrimp):
    """ User chooses a card of shrimp """
    print("1. Draw from deck \n2. Draw a shrimp")
    choice = check_input.range_int("Enter choice: ", 1, 2)
    if choice == 1:
        new_card = random_card(play_deck)
        hero_hand.append(new_card)
        print(f"\nYou drew a {new_card.name}.")
    elif choice == 2:
        if shrimp_count > 0:
            hero_hand.append(my_shrimp)
            print("\nYou drew a shrimp.")
            shrimp_count -= 1

def placeCard(hero_hand, curr_hero):
    """ Place and sacerfice cards """

    done_choosing = False
    has_enough = 0
    picked_card = None
    while not done_choosing:
        #picked_card, index = check_input.choose_card("\nChoose a card from your hand", hero_hand, return_index=True)
        picked_card, index = choose_card("\nChoose a card from your hand", hero_hand, return_index=True)
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
            #choice_card, index= check_input.choose_card("", curr_hero, return_index=True)
            choice_card, index = choose_card("", curr_hero, return_index=True)
            curr_hero[index] = None
            curr_sac += 1
            print(f"You have sacerficed {choice_card.name} sacerfices: {curr_sac}/{picked_card.cost}")

    card_place = False
    while not card_place:
        print("Where would you like to place the card? Slot 1, 2, 3, or 4")
        choice = check_input.range_int("Enter choice: ", 1, 4)
        if curr_hero[choice - 1] is None:
            curr_hero[choice - 1] = picked_card
            card_place = True
        else:
            print("There is already a card in that slot, pick somewhere else.")

def heroAttack(curr_hero, curr_attack, scale):
    for index, card in enumerate(curr_hero):
        if card is not None:
            if curr_attack[index] is None:
                scale += card.power
                print(f"Your {card.name} have done {card.power} to the villian!")
            else:
                curr_attack[index].take_damage(card.power)
                print(f"Your {card.name} delt {card.power} damage to villian {curr_attack[index].name}")
                if curr_attack[index].hp == 0:
                    print(f"Your {card.name} has slayed villian {curr_attack[index].name} ")
                    curr_attack[index] = None 
        else:
            print(f"No cards placed in slot {index + 1}")
    return scale

def use_item(hero_hand, play_deck, curr_hero, scale, item):
    if item == "Dagger":
        scale += 1 
    elif item == "Boulder":
        boulder = card.Card("Boulder", 0, 0, 5, None, False)
        hero_hand.append(boulder)
    elif item == "Shrimp Bottle":
        shrimp = card.Card("Shrimp", 0, 0, 0, None, False)
        hero_hand.append(shrimp)

def use_sigil(villian, upcoming_attack, curr_attack, curr_hero, scale): 
    end_sigil = False
    while not end_sigil:
        print("Which card do you want to use Sigil? Slot 1, 2, 3, or 4")
        choice = check_input.range_int("Enter choice: ", 1, 4)
        if curr_hero[choice - 1] is not None:
            if curr_hero[choice - 1].sigil == "Bioluminescence":
                for index, card in enumerate(curr_hero):
                    if curr_hero[index] is not None and (curr_hero[index].name == "Angler" or curr_hero[index].name == "Jellyfish" or curr_hero[index].name == "Kraken"):
                        curr_hero[index].power += 1
                        curr_hero[index].hp += 1
                print(f"\n{curr_hero[choice - 1].name} use Bioluminescence and enhances its self, and other abyssal fish cards!")
                end_sigil = True

            elif curr_hero[choice - 1].sigil == "Swarm":
                swarm_clone = 2
                for _ in range(swarm_clone):
                    clone = curr_hero[choice - 1].copy() if curr_hero[choice - 1] is not None else None
                    
                    for i, card in enumerate(curr_hero):
                        if card is None:
                            curr_hero[i] = clone
                            break
                print(f"\n{curr_hero[choice - 1].name} uses Swarm and summons additional copies of itself!")
                end_sigil = True

            elif curr_hero[choice - 1].sigil == "Frenzy":
                if curr_hero[choice - 1].hp is not None and curr_hero[choice - 1].hp < (curr_hero[choice - 1].max_hp //2):
                    curr_hero[choice - 1].power *= 2
                    print(f"\n{curr_hero[choice - 1].name} use Frenzy and now will deals double damage!")
                    end_sigil = True 
                else: 
                    print(f"\n{curr_hero[choice - 1].name} is not low yet, and cannot use Frenzy")

            elif curr_hero[choice - 1].sigil == "Barrier":
                if not curr_hero[choice - 1].barrier:
                    print(f"\n{curr_hero[choice - 1].name} use Barrier and will blocks the next attack!")
                    curr_hero[choice - 1].barrier = True
                    end_sigil = True
                else:
                    print(f"\n{curr_hero[choice - 1].name} already has a Barrier active.")

            elif curr_hero[choice - 1].sigil == "Echolocation":
                print(upcoming_attack)
                print(villian_draw_card(villian, upcoming_attack))
                print(display_board(upcoming_attack.copy(), curr_attack.copy(), curr_hero.copy(), scale))
                print(f"\n{curr_hero[choice - 1].name} use Echolocation and see upcoming attack!")
                end_sigil = True

            elif curr_hero[choice - 1].sigil == "Swift":
                print(f"\n{curr_hero[choice - 1].name} now has 50% chance to avoid attack")
                if random.randint(0, 1) == 1:
                    if curr_attack[choice - 1].power > curr_hero[choice - 1].max_hp or curr_attack[choice - 1].power < curr_hero[choice - 1].max_hp:
                        curr_hero[choice - 1].hp = curr_hero[choice - 1].max_hp
                    else: 
                        curr_hero[choice - 1].hp = curr_attack[choice - 1].power
                end_sigil = True 

            elif curr_hero[choice - 1].sigil == "Shell":
                while not end_sigil:
                    print("Which current attack card do you want to pick to cut the damage in half? Slot 1, 2, 3, or 4")
                    choice_2 = check_input.range_int("Enter choice: ", 1, 4)
                    if curr_attack[choice_2 - 1] is not None:
                        curr_attack[choice_2 - 1].power //= 2
                        print(f"\n {curr_attack[choice_2 - 1].name} card has half the damage now")
                        end_sigil = True
                    else:
                        print("There are no card in that slot, pick somewhere else.")

            elif curr_hero[choice - 1].sigil == "None":
                print("\nThis card has no sigil")
        else:
            print("There are no card in that slot, pick somewhere else.")

def battle(hero, villian):
    print("------------- Battle -------------")
    
    shrimp_count = 20
    my_shrimp = shrimp.Shrimp()

    hero_hand = []
    play_deck = hero._deck 
    play_deck.shuffle()
    for _ in range(4):
        hero_hand.append(random_card(play_deck))

    villian._deck.shuffle()
    
    scale = 0
    turn = 0
    upcoming_attack = [None, None, None, None]
    curr_attack =     [None, None, None, None]
    curr_hero =     [None, None, None, None]

    while scale > -5 and scale < 5:
        

        # villian turn
        if turn == 0:
            print("\n---- Villain Turn ----\n")
            scale = villian_turn(villian, upcoming_attack, curr_attack, curr_hero, scale)
            turn = 1
        # Hero turn
        else:
            pause()
            print("\n---- Hero Turn ----\n")
            scale = hero_turn(hero_hand, play_deck, shrimp_count, my_shrimp, curr_hero, scale, upcoming_attack, curr_attack,villian)
            turn = 0

        
        


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
        
