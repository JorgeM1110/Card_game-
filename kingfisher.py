import card

class KingFisher(card.Card):

    def __init__(self):
        max_hp = 1
        sigil = "Waterborne & Airborne"
        super().__init__("kingFisher", 1, 1, max_hp, sigil)

    def attack(self, entity):
        entity.take_damage(self._power)
        return self._name + " attacks a " + entity._name + " for " + str(self._power) + " damage."
    
    def desc(self):
        return " Waterborne - Dives underwater, unkillable unless attack is reflected or gets hurt while doing damage\n Airborne - When played, choose a card from your deck to be drawn"