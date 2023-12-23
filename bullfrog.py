import card

class BullFrog(card.Card):

    def __init__(self):
        max_hp = 2
        sigil = "Might Leap"
        super.__init__("BullFrog", 1, 1, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return "This card blocks opposing Airborne creatures."