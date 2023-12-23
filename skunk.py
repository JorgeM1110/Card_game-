import card

class Skunk(card.Card):

    def __init__(self):
        max_hp = 3
        sigil = "Stinky"
        super.__init__("Skunk", 1, 0, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return "The creature opposing this card loses 1 Power."