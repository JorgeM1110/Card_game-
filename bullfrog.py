import card

class BullFrog(card.Card):

    def __init__(self):
        max_hp = 2
        sigil = "Might Leap"
        super.__init__("BullFrog", max_hp, sigil)

    def attack(self, entity):
        damage = 1
        entity.take_damage(damage)
        return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."