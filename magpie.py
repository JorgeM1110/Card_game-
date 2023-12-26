import card

class MagPie(card.Card):

    def __init__(self):
        max_hp = 1
        sigil = "Airborne"
        super().__init__("MagPie", 2, 1, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return "When this card is played, choose a card from your deck to be drawn immediately."