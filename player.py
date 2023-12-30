import deck
import map
import random

class Player():
    def __init__(self, name):
        self._name = name
        self._deck = deck.Deck()
        self._items = []
        self._location = [5, 2]
        self._currCost = 0

    @property
    def location(self):
        return self._location
    
    def displayItems(self):
        for item in self._items:
            print(item, end=" ")

    def displayDeck(self):
        count = 0
        for card in self._deck:
            print(f"{count}. {card.name}")
            count += 1

    def shopItem(self):
        print("Welcome to meh shop! \nPick whichever tickles your fancy!")
        print("1. Dagger - Cut out your eye and place it on scale, giving you one points toward victory.")
        print("2. Boulder - Place it to block enemies attack up to 5 hit points")
        print("3. Squirrel Bottle - A squirell will go right into your hand")

        flag = False
        while not flag:
            choice = input("Your choice: ")
            if choice == "1":
                self._items.append("Dagger")
                flag = True
            elif choice == "2":
                self._items.append("Boulder")
                flag = True
            elif choice == "3":
                self._items.append("Squirrel Bottle")
                flag = True
            else:
                print("Invalid input")

    def __str__(self):
        return f"Name: {self._name} \nItems: {self.displayItems()} \nDeck: {self.displayDeck()}"
  
    def go_forward(self):
        m = map.Map()
        if len(self._location) - 1 < len(m) - 1:
            if self._location[0] > 0 and m[self.location[0] - 1][self.location[1]] != "-":
                self._location[0] -= 1
                return m[self.location[0]][self.location[1]]
            else:
                print("\nYou cannot go that way\n")
                return 'o'
        return 'o'

    def go_right(self):
        m = map.Map()
        if len(self._location) - 1 < len(m) - 1:
            if self._location[1] < 4 and self._location[0] > 0 and m[self.location[0] - 1][self.location[1] + 1] != "-":
                self._location[1] += 1
                self._location[0] -= 1 
                return m[self.location[0]][self.location[1]]
            else:
                print("\nYou cannot go that way\n")
                return 'o'
        else:
            return 'o'

    def go_left(self):
        m = map.Map()
        if len(self._location) - 1 < len(m) - 1:
            if self._location[1] > 0 and self._location[0] > 0 and m[self.location[0] - 1][self.location[1] - 1] != "-":
                self._location[1] -= 1
                self._location[0] -= 1
                return m[self.location[0]][self.location[1]]
            else:
                print("\nYou cannot go that way\n")
                return 'o'
        else:
            return 'o'
