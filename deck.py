import card 
import random
import bear
import bullfrog
import skunk 
import snake
import shark
import raven
import kingfisher
import magpie
import snappingturtle

class Deck:

    def __init__(self):
        self._cards = []
        
        enemies = [bear.Bear(), snake.Snake(), skunk.Skunk(), 
                   bullfrog.BullFrog(), shark.Shark(), snappingturtle.SnappingTurtle(), 
                   kingfisher.KingFisher(), magpie.MagPie(), raven.Raven()]
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
        
    def __len__(self):
        """
        return the number of cards remaining in the deck.
        """
        return len(self._cards)

    def __str__(self):
        for card in self._cards:
            print(card)
    
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

        while player_choice == 'Y' and 'y' and chance > 0 :
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
                    self.removeCard(0)
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
                    self.removeCard(0)
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
                    self.removeCard(0)
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
                    self.removeCard(0)
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
                    self.removeCard(0)
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
                    self.removeCard(0)
                    print("You fail me") 
                    chance = 0 

            chance //= 2
            if chance is not 0: 
                player_choice = input(f" would you like to upgrade again? " + str(chance) + '%' " change\n Y/N\n")

    def sacrifice(self, deadcard, gaincard):
        if deadcard in self._cards:
            self._cards.remove(deadcard)
            gaincard.sigil = deadcard.sigil

    def removeCard(self, index):
        print(self._deck[index].name, " is removed")
        return self._deck.pop(index)

