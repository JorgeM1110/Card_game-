import card

class Snake(card.Card):

    def __init__(self):
        max_hp = 1
        sigil = "Touch of Death"
        super().__init__("Snake", 2 , 1, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return "This card instantly kills any card it damages."