import card

class MagPie(card.Card):

    def __init__(self):
        max_hp = 1
        sigil = "Airborne"
        super.__init__("MagPie", max_hp, sigil)

    def attack(self, entity):
        damage = 1
        entity.take_damage(damage)
        return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."

    def desc(self):
        return "When this card is played, choose a card from your deck to be drawn immediately."