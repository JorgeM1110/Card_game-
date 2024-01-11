import card

class Dolphin(card.Card):

    def __init__(self):
        name = "Dolphin"
        cost = 2
        power = 2
        max_hp = 2
        sigil = "Echolocation" # See upcoming attack
        super().__init__(name, cost, power, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return f"{self.name} that costs {self.cost} with {self.max_hp}, and {self.power}. Sigil: {self.sigil}"