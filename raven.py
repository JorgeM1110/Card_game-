import card

class Raven(card.Card):

    def __init__(self):
        max_hp = 3
        sigil = "Airborne"
        super.__init__("Raven", max_hp, sigil)

    def attack(self, entity, dmg):
        damage = 2
        entity.take_damage(damage)
        return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."