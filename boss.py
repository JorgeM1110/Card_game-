import deck 
import player 
import state_normal

class Boss:

    def __init__(self, name):

        self._state = state_normal.StateNormal()
        self._deck = deck.Deck()
        self._name = name
        self._plays = 0
        self._mechanic = 0

    @property
    def plays(self):
        return self._plays
    
    @property
    def mechanic(self):
        return self._mechanic
    
    def change_state(self, new_state):
        """
        updates the boss state to the new state.
        """
        self._state = new_state

    def attack(self):
        """
        calls the play method for whichever state the boss is in.
        """
        return self._state.plays(self)
    
    def power(self):
        """
        calls the mechanic method for whichever state the boss is in.
        """
        return self._sate.mechanic(self)
    


    
