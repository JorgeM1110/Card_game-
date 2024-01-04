import card 
import random
import check_input
from cards.tropical import dolphin, otter, turtle
from cards.oceanic import leviathan, manta_ray, shark
from cards.abyssal import angler, jellyfish, kraken
from terminal_utils import clear_terminal, pause, delay_print, delay_input, delay

class Deck:

    def __init__(self):
        self._cards = []
                   
        enemies = [dolphin.Dolphin(), otter.Otter(), turtle.Turtle(),
                    leviathan.Leviathan(), manta_ray.MantaRay(), shark.Shark(),
                    angler.Angler(), jellyfish.Jellyfish(), kraken.Kraken()]

        for i in enemies:
            for j in range(3):
                self._cards.append(i)

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        self._i += 1
        if self._i >= len(self._cards):
            raise StopIteration
        else:
            return self._cards[self._i]
    
    def __len__(self):
        """
        return the number of cards remaining in the deck.
        """
        return len(self._cards)

    def __str__(self):
        for card in self._cards:
            print(card)
        
    def shuffle(self):
        """
        shuffles the deck.
        """
        random.shuffle(self._cards)
    
    def draw_card(self):
        """
        remove the topmost card from the deck and return it.
        """
        if len(self._cards) > 0:
            top_card = self._cards.pop(0)
            return top_card

    def remove_card(self, index):
        return self._cards.pop(index)

    def choose_card(self, text, deck, return_index=False):
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


    def sacrifice(self):
        print("------------- Sacrifice -------------")
        print("Here you will sacerfice a card and either transfer its sigil or one of the its stats to another ...\n")
        pause()
        clear_terminal()

        print("Choose a card to sacerfice (You will lose this card)")
        counter = 1
        for index, card in enumerate(self._cards):
            print(f"{counter}. {self._cards[index].name}")
            counter += 1
        
        choice = check_input.range_int("\nEnter choice: ", 1, counter)
        sac_card = self._cards[choice - 1]
        self.remove_card(choice - 1)
        print(f"You have chosen the {sac_card.name}\n")
        pause()
        clear_terminal()
        print(f"What would you like to transfer the: \n1. {sac_card.sigil} sigil \n2. Cost ({sac_card.cost}) \n3. Power ({sac_card.power}) \n4. Health ({sac_card.hp})")
        gain_choice = check_input.range_int("\nEnter choice: ", 1, 4)
        print()
        pause()
        clear_terminal()
            
        print("Now choose a card to gain its new stat or sigil")
        counter = 1
        for index, card in enumerate(self._cards):
            print(f"{counter}. {self._cards[index].name}")
            counter += 1
        choice = check_input.range_int("\nEnter choice: ", 1, counter)
        gain_card = self._cards[choice - 1]
        print()
        clear_terminal()

        print(gain_card)
        print("\nturned to\n")

        if gain_choice == 1:
            gain_card.sigil = f"{sac_card.sigil} and {gain_card.sigil}"
        elif gain_choice == 2:
            gain_card.cost = sac_card.cost
        elif gain_choice == 3:
            gain_card.power = sac_card.power
        else:
            gain_card.hp = sac_card.hp
            gain_card.max_health = sac_card.max_health
        
        print(gain_card)
        print()
        pause()
        clear_terminal()

    def upgrade(self, card):
        cards = random.randint(1,2)
        if cards == 1:
            card._power += 1
            print("Your power has upgrade to " + str(card._power) + "\n")
        else:
            card._max_health += 1
            print("Your max health has upgrade to " + str(card._max_health) + "\n")
        
        player_choice = input(f" would you like to upgrade again? 50% change\n Y/N\n")
        chance = 50

        while player_choice == 'Y' or player_choice == 'y' and chance > 0 :
            random_num = random.randint(1,100)
            if chance == 50:
                if random_num <= 50:
                    print("Well done you have Luck!")
                    if random_num <= 25:
                        card._power += 1
                        print("Your power has upgrade to " + str(card._power) + "\n")
                    else:
                        card._max_health += 2
                        print("Your max health has upgrade to " + str(card._max_health) + "\n")
                else:
                    self.remove_card(0)
                    print("Better luck next time")
                    chance = 0 

            elif chance == 25:
                if random_num <= 25:
                    print("Well done you have Luck Again!")
                    if random_num <= 12:
                        card._power += 1
                        print("Your power has upgrade to " + str(card._power) + "\n")
                    else:
                        card._max_health += 2
                        print("Your max health has upgrade to " + str(card._max_health) + "\n")
                else:
                    self.remove_card(0)
                    print("Your Luck runs out")
                    chance = 0 

            elif chance == 12:
                if random_num <= 12:
                    print("You're on Fire!!")
                    if random_num <= 6:
                        card._power += 1
                        print("Your power has upgrade to " + str(card._power) + "\n")
                    else:
                        card._max_health += 2
                        print("Your max health has upgrade to " + str(card._max_health) + "\n")
                else:
                    self.remove_card(0)
                    print("You got too Greedy")
                    chance = 0 

            elif chance == 6:
                if random_num <= 6:
                    print("You're Crazy!!")
                    if random_num <= 3:
                        card._power += 1
                        print("Your power has upgrade to " + str(card._power) + "\n")
                    else:
                        card._max_health += 2
                        print("Your max health has upgrade to " + str(card._max_health) + "\n")
                else:
                    self.remove_card(0)
                    print("Your time has come to end")
                    chance = 0 

            elif chance == 3:
                if random_num <= 3:
                    print("You won't do it again")
                    if random_num <= 1:
                        card._power += 1
                        print("Your power has upgrade to " + str(card._power) + "\n")
                    else:
                        card._max_health += 2
                        print("Your max health has upgrade to " + str(card._max_health) + "\n")
                else:
                    self.remove_card(0)
                    print("Finally")
                    chance = 0 
            
            elif chance == 1:
                if random_num == 1:
                    print("Congrants you did it!!")
                    if random_num <= 1:
                        card._power += 1
                        card._max_health += 2
                        print("Your power has upgrade to " + str(card._power) + "\n")
                        print("Your max health has upgrade to " + str(card._max_health) + "\n")
                else:
                    self.remove_card(0)
                    print("You fail me") 
                    chance = 0 

            chance //= 2
            if chance is not 0: 
                player_choice = input(f" would you like to upgrade again? " + str(chance) + '%' " change\n Y/N\n")
