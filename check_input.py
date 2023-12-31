import card

def range_int(text, min, max):
    num = 0 
    valid = False

    while not valid:
        try:
            num = int(input(text))
            if num >= min and num <= max:
                valid = True
            else:
                print("Invalid input - it should be within " + str(min) + " - " + str(max) + ".")
        except ValueError:
            print("Input should be an integer.")
    
    return num

def yes_no(text):
    valid = False
    while not valid:
        val = input(text).upper()
        if val == "YES" or val == "Y":
            return True
        elif val == "NO" or val == "N":
            return False
        else:
            print("Invalid input, should be `y` or `n`")

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
            choice = range_int("Enter choice: ", 1, counter - 1)

            if deck[choice - 1] is not None:
                if return_index:
                    return deck[choice - 1], choice - 1
                else:
                    return deck[choice - 1]
            else:
                print("There's no card there, choose again. ")

# print("\nChoose a card from your hand")
    # counter = 1
    # for card in playerHand:
    #     print(f"{str(counter)}. {card}")
    #     print()
    #     counter += 1
    # num = check_input.range_int("Enter choice: ", 1, counter - 1)

    # #Problem - when the user chooses none, make a check_input function
    # pickedCard = playerHand[num - 1]
    # playerHand[num - 1] = None