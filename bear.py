import card


class Bear(card.Card):

    def __init__(self):
        max_hp = 6
        sigil = "None"
        super.__init__("Bear", max_hp, sigil)

    def attack(self, entity, dmg):
        damage = 4
        entity.take_damage(damage)
        return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."