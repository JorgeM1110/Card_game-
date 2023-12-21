import card

class SnappingTurtles(card.Card):

    def __init__(self):
        max_hp = 6
        sigil = "none"
        super.__init__("SnappingTurtles", max_hp, sigil)

    def attack(self, entity, dmg):
        damage = 1
        entity.take_damage(damage)
        return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."

    def desc(self):
        return "This card blocks opposing Airborne creatures."


        
       