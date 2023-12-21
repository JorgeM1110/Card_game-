import card_factory
import random

class WindFactory(card_factory.CardFactory):
    """
    factory to create Wind enemies.
    """

    def create_random_card(self):
        
        wind_enemies = random.randint(1,3)

        if wind_enemies == 1:
            return raven.Raven()
        
        elif wind_enemies == 2:
            return KingFisher.kingfisher()
        
        elif wind_enemies == 3:
            return Magpie.Magpie()