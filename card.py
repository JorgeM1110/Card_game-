class Card:
    """ Represents a single card
    Attributes:
        <<get>> _name (string): Name of the card
        <<get>> _hp (int): health of the card
        _max_hp (int): max health of the card
        _cost (int): cost of the card
        <<get>> _power (int): power of the card
        _sigil (string): sigil of the card
    """

    def __init__(self, name, cost, power, max_health):
        """ Initializes attributes """
        self._name = name
        self._cost = cost
        self._power = power
        self._max_health = max_health
        self._hp = max_health

    @property
    def name(self):
        """ Getter for name """
        return self._name

    @property
    def hp(self):
        """ Getter for health """
        return self._hp

    @property
    def power(self):
        """ Getter for power """
        return self._power

    def take_damage(self, dmg):
        """ Takes damge, subtracts health from damage """
        if self._hp > dmg:
            self._hp -= dmg
        else:
            self._hp = 0
        return f"{self.name} takes {dmg} damage"

    def attack(self, entity, dmg):
        """ Deals damage to opposing entity """
        entity.take_damage(dmg)
        return f"{entity.name} delts {dmg} to {self.name}"

    def __str__(self):
        """ returns name, health, and sigil """
        return f"{self.name} \n{self._hp}/{self._max_health} \nSigil: {self._sigil}"