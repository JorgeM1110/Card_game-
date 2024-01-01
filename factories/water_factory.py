import random
from factories import card_factory
from cards import snappingturtle, bullfrog, shark


class WaterFactory(card_factory.CardFactory):
    """
    factory to create Water enemies.
    """

    def create_random_card(self):
        
        water_enemies = random.randint(1,3)

        if water_enemies == 1:
            return snappingturtle.SnappingTurtle()
        
        elif water_enemies == 2:
            return bullfrog.BullFrog()
        
        elif water_enemies == 3:
            return shark.Shark()