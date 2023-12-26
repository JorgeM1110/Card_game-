import card

class Bear(card.Card):

    def __init__(self):
        max_hp = 6
        sigil = "None"
        super().__init__("Bear", 3, 4, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."

    def desc(self):
        return "This card has no sigil"