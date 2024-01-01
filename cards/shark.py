import card

class Shark(card.Card):

    def __init__(self):
        max_hp = 2
        sigil = "Waterborne"
        super().__init__("Shark", 3, 4, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."
    
    def desc(self):
        return "Dives underwater, unkillable unless attack is reflected or gets hurt while doing damage."