import card

class Raven(card.Card):

    def __init__(self):
        max_hp = 3
        sigil = "Airborne"
        super().__init__("Raven", 2, 2, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return "This card will ignore opposing cards and strike an opponent directly."