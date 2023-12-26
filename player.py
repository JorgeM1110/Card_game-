import deck
import map
import random

class Player():
    def __init__(self, name, items):
        self._name = name
        self._deck = deck.Deck()
        self._items = []
        self._location = [0, 0]

    @property
    def location(self):
        return self._location
    
    def displayItems(self):
        for item in self._items:
            print(item, end=" ")

    def displayDeck(self):
        for card in self._deck:
            print(card, end=" ")

    def __str__(self):
        return f"Name: {self._name} \nItems: {self.displayItems()} \nDeck: {self.displayDeck()}"
    
    def go_north(self):
        m = map.Map()
        if len(self._location) - 1 < len(m) - 1:
            if self._location[0] > 0:
                self._location[0] -= 1
                m.reveal(self.location)
                return m[self.location[0]][self.location[1]]
            else:
                return 'o'
        return 'o'

    def go_south(self):
        m = map.Map()
        if len(self._location) - 1 < len(m) - 1:
            if self._location[0] < 4:
                self._location[0] += 1
                m.reveal(self.location)
                return m[self.location[0]][self.location[1]]
            else:
                return 'o'
        else:
            return 'o'

    def go_east(self):
        m = map.Map()
        if len(self._location) - 1 < len(m) - 1:
            if self._location[1] < 4:
                self._location[1] += 1
                m.reveal(self.location)
                return m[self.location[0]][self.location[1]]
            else:
                return 'o'
        else:
            return 'o'

    def go_west(self):
        m = map.Map()
        if len(self._location) - 1 < len(m) - 1:
            if self._location[1] > 0:
                self._location[1] -= 1
                m.reveal(self.location)
                return m[self.location[0]][self.location[1]]
            else:
                return 'o'
        else:
            return 'o'
