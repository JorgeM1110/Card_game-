import card

class Turtle(card.Card):

    def __init__(self):
        max_hp = 6
        sigil = "none"
        super.__init__("Turtle", max_hp, sigil)

    def attack(self, entity, dmg):
        damage = 1
        entity.take_damage(damage)
        return self._name + " attacks a " + entity._name + " for " + str(damage) + " damage."


        
       