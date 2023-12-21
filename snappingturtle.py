import card

class SnappingTurtle(card.Card):

    def __init__(self):
        max_hp = 6
        sigil = "none"
        super.__init__("SnappingTurtle", max_hp, sigil)

    def attack(self, entity):
        damage = 1
        entity.take_damage(damage)
        return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."


        
       