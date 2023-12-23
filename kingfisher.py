import card

class KingFisher(card.Card):

    def __init__(self):
        max_hp = 1
        sigil = "Waterborne & Airborne"
        super.__init__("kingFisher", 1, 1, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."