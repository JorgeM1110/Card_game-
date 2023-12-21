import card

class Shark(card.Card):

    def __init__(self):
        max_hp = 2
        sigil = " Waterborne"
        super.__init__("Shark", max_hp, sigil)

    def attack(self, entity):
        damage = 4
        entity.take_damage(damage)
        return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."