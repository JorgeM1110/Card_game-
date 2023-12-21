import card

class KingFisher(card.Card):

    def __init__(self):
        max_hp = 1
        sigil = "Waterborne & Airborne"
        super.__init__("kingFisher", max_hp, sigil)

    def attack(self, entity):
        damage = 1
        entity.take_damage(damage)
        return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."

    def desc(self):
        return "This card blocks opposing Airborne creatures."