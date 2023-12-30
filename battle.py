import random
import deck
import card
import player
import boss
import squirrel
import check_input


def random_card(deck):
    """ From a deck of cards, pick a random card """
    if len(deck) <= 0:
        print("You have nothing left.")
        return None
    cardNum = random.randint(0, len(deck) - 1)
    card = deck.removeCard(cardNum)
    return card 

def show_hand(hand):
    """ Display current hand """
    print("\n~~~ Current Hand ~~~")
    for card in hand:
        print(card)
        print()

    print("~~~~~~~~~~~~~~~~~~~~\n")

def displayBoard(upcomingAttack, currAttack, currPlayer):
    """ hows current board """
    print("\n~~~~~~~~ The Board ~~~~~~~~")
    counter = 1
    for index, card in enumerate(upcomingAttack):
        if card == None:
            print("None", end=" ")
        else:
            print(upcomingAttack[index].name, end=" ")
    print("-> Upcoming attack")
    print()

    counter = 2
    for index, card in enumerate(currAttack):
        if card == None:
            print("None", end=" ")
        else:
            print(currAttack[index].name, end=" ")
    print("-> Current attack")
    print()        
    
    counter = 3
    for index, card in enumerate(currPlayer):
        if card == None:
            print("None", end=" ")
        else:
            print(currPlayer[index].name, end=" ")
    print("-> Current player")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def bossTurn(boss, upcomingAttack, currAttack, currPlayer):
    """ Randomly add cards to UpcomingAttack, pushes it to currAttack and attacks player """
    currAttack = upcomingAttack
    upcomingAttack = [None,None,None,None]

    for index, card in enumerate(upcomingAttack):
        if random.randint(0, 1) == 1:
            upcomingAttack[index] = boss._deck.draw_card()
    
    displayBoard(upcomingAttack, currAttack, currPlayer)

    for index, card in enumerate(currAttack):
        if currAttack[index] is not None:
            if currPlayer[index] is None:
                scale += card.power
                print(f"The boss's {card.name} dealt {card.power} damage to you ")
            else:
                card.take_damage(currAttack[index].power)
                print("The Boss's " + str(currAttack[index].name) + " dealt " + str(currAttack[index].power) + " damage to your " + str(card.name))

def playerTurn(playerHand, playDeck, squirrelCount, mySquirell, currPlayer, scale, upcomingAttack, currAttack):
    """ Draws and sacerfices cards, and attacks boss """
    drawCard(playerHand, playDeck, squirrelCount, mySquirell)
    done = False
    while not done:
        print("1. Place a card down \n2. End turn")
        choice = check_input.range_int("Enter choice: ", 1, 2)
        if choice == 1:
            placeCard(playerHand, currPlayer)
        elif choice == 2:
            playerAttack(currPlayer, currAttack, scale)
            done = True
        displayBoard(upcomingAttack, currAttack, currPlayer)

def drawCard(playerHand, playDeck, squirrelCount, mySquirell):
    """ User chooses a card of squirrel """
    show_hand(playerHand)
    print("1. Draw from deck \n2. Draw a squirrel")
    choice = check_input.range_int("Enter choice: ", 1, 2)
    if choice == 1:
        playerHand.append(random_card(playDeck))
        show_hand(playerHand)
    elif choice == 2:
        if squirrelCount > 0:
            playerHand.append(mySquirell)
            show_hand(playerHand)
            squirrelCount -= 1

def placeCard(playerHand, currPlayer):
    """ Place and sacerfice cards """
    print("\nChoose a card from your hand")
    counter = 1
    for card in playerHand:
        print(f"{str(counter)}. {card}")
        print()
        counter += 1
    num = check_input.range_int("Enter choice: ", 1, counter - 1)

    #Problem - when the user chooses none, make a check_input function
    pickedCard = playerHand[num - 1]
    playerHand[num - 1] = None

    if pickedCard.cost > 0:
        print(f"This card needs {pickedCard.cost} sacerfices")
        currCost = 0
        while currCost < pickedCard.cost:
            print("Which card would you sacerfice?")
            counter = 1
            for card in currPlayer:
                if card is not None:
                    print(f"{counter}. {card}") 
                else:
                    print(f"{counter}. No card")
                counter += 1 
            choice = check_input.range_int("Enter choice: ", 1, counter)
            if currPlayer[choice - 1] is not None:
                currCost += 1
                print(f"You have sacerficed {currCost}/{pickedCard.cost}")
                currPlayer[choice - 1] = None
            else:
                print("There's no card")

    cardPlace = False
    while not cardPlace:
        print("Where would you like to place the card? Slot 1, 2, 3, or 4")
        choice = check_input.range_int("Enter choice: ", 1, 4)
        if currPlayer[choice - 1] is None:
            currPlayer[choice - 1] = pickedCard
            cardPlace = True
        else:
            print("There is already a card in that slot, pick somewhere else.")

def playerAttack(currPlayer, currAttack, scale):
    for index, card in enumerate(currPlayer):
        if currAttack[index] is None:
            scale -= card.power
            print(f"You have done {card.power} to the boss!")
        else:
            currAttack[index].take_damage(card.power)
            print(f"{card.name} delt {card.power} to {currAttack.name}")

def battle(player, boss):
    print("---------- Battle Start! ----------")
    
    # Initializes starting deck and hand
    squirrelCount = 20
    mySquirell = squirrel.Squirrel()
    playerHand = []
    playDeck = player._deck 
    playDeck.shuffle()
    for _ in range(4):
        playerHand.append(random_card(playDeck))

    boss._deck.shuffle()
    
    scale = 0
    turn = 1
    upcomingAttack = [None, None, None, None]
    currAttack =     [None, None, None, None]
    currPlayer =     [None, None, None, None]

    while scale > -5 and scale < 5:
        # Boss turn
        if turn == 1:
            bossTurn(boss, upcomingAttack, currAttack, currPlayer)
            turn = 0
        # Player turn
        elif turn == 0:
            playerTurn(playerHand, playDeck, squirrelCount, mySquirell, currPlayer, scale, upcomingAttack, currAttack)
            turn = 1


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
        add the boss turn
            - Randomly choose an enemy card and place it in it's upcomingAttack where the player can see what is comming next
            - Move the upcomingAttack to currAttack and replace upcomingAttack if we want it to continue, so we can have 2 - 3 rounds where the boss has a chance to places a card 
            - Deals damage to player or player's card 
        Once everything works (so just simple health, power, and cost), work on sigil, and items
        Maybe add a put down card, if the user chooses a card but then changes their mind
    """
        