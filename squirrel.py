import card
class Squirrel(card.Card):

    def __init__(self):
        max_hp = 1
        sigil = "None"
        super().__init__("Squirrel", 0, 0, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."
    
    def desc(self):
        return "It's a squirrel..."