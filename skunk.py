import card

class Skunk(card.Card):

    def __init__(self):
        max_hp = 3
        sigil = "Stinky"
        super.__init__("Skunk", max_hp, sigil)

    def attack(self, entity, dmg):
        damage = 0
        entity.take_damage(damage)
        return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."