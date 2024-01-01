import card

class Jellyfish(card.Card):

    def __init__(self):
        name = "Jellyfish"
        cost = 2
        power = 1
        max_hp = 2
        sigil = "Swarm" # Summons additional coppies of itself when played
        super().__init__(name, cost, power, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return f"{self.name} that costs {self.cost} with {self.max_hp}, and {self.power}. Sigil: {self.sigil}"