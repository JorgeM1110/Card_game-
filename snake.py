import card

class Snake(card.Card):

    def __init__(self):
        max_hp = 1
        sigil = "Touch of Death"
        super.__init__("Snake", max_hp, sigil)

    def attack(self, entity, dmg):
        damage = 1
        entity.take_damage(damage)
        return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."