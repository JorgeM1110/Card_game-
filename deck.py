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
    
    def upgrade(self, card):
        cards = random.randint(1,2)
        if cards == 1:
            card._power += 1
            print("Your power has upgrade to " + card._power + "\n")
        else:
            card._max_health += 1
            print("Your max health has upgrade to " + card._max_health + "\n")
        
        player_choice = input(f" would you like to upgrade again? 50% change\n Y/N")
        chance = 50

        while player_choice == 'Y' and chance > 0 :
            random_num = random.randint(1,100)
            if chance == 50:
                if random_num <= 50:
                    print("Well done you have Luck!")
                    if random_num <= 25:
                        card._power += 1
                        print("Your power has upgrade to " + card._power + "\n")
                    else:
                        card._max_health += 2
                        print("Your max health has upgrade to " + card._max_health + "\n")
                else:
                    card.pop(0)
                    print("Better luck next time")

            elif chance == 25:
                if random_num <= 25:
                    print("Well done you have Luck Again!")
                    if random_num <= 12:
                        card._power += 1
                        print("Your power has upgrade to " + card._power + "\n")
                    else:
                        card._max_health += 2
                        print("Your max health has upgrade to " + card._max_health + "\n")
                else:
                    card.pop(0)
                    print("Your Luck runs out")

            elif chance == 12:
                if random_num <= 12:
                    print("You're on Fire!!")
                    if random_num <= 6:
                        card._power += 1
                        print("Your power has upgrade to " + card._power + "\n")
                    else:
                        card._max_health += 2
                        print("Your max health has upgrade to " + card._max_health + "\n")
                else:
                    card.pop(0)
                    print("You got too Greedy")

            elif chance == 6:
                if random_num <= 6:
                    print("You're Crazy!!")
                    if random_num <= 3:
                        card._power += 1
                        print("Your power has upgrade to " + card._power + "\n")
                    else:
                        card._max_health += 2
                        print("Your max health has upgrade to " + card._max_health + "\n")
                else:
                    card.pop(0)
                    print("Your time has come to end")

            elif chance == 3:
                if random_num <= 3:
                    print("You won't do it again")
                    if random_num <= 1:
                        card._power += 1
                        print("Your power has upgrade to " + card._power + "\n")
                    else:
                        card._max_health += 2
                        print("Your max health has upgrade to " + card._max_health + "\n")
                else:
                    card.pop(0)
                    print("Finally")
            
            elif chance == 1:
                if random_num == 1:
                    print("Congrants you did it!!")
                    if random_num <= 1:
                        card._power += 1
                        card._max_health += 2
                        print("Your power has upgrade to " + card._power + "\n")
                        print("Your max health has upgrade to " + card._max_health + "\n")
                else:
                    card.pop(0)
                    print("You fail me") 

            chance //= 2
            player_choice = input(f" would you like to upgrade again? " + chance + " {%} change\n Y/N")

    def sacrifice(self, deadcard, gaincard):
        if deadcard in self._cards:
            self._cards.remove(deadcard)
            gaincard.sigil = deadcard.sigil

