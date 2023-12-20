import card 
import random

class Deck:

    def __init__(self):
        self._cards = []

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
            print("Your power has upgrade to 1\n")
        else:
            card._max_health += 1
            print("Your max health has upgrade to 1\n")
        
        player_choice = input(f" would you like to upgrade again? 50% change\n Y/N")
        chance = 50

        while player_choice == 'Y':

            cards = random.randint(1,2)
            if cards == 1:
                print(hello)


            




        
        



        







    

    


    


