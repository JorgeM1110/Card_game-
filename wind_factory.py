import card_factory
import random
import raven
import kingfisher
import magpie

class WindFactory(card_factory.CardFactory):
    """
    factory to create Wind enemies.
    """

    def create_random_card(self):
        
        wind_enemies = random.randint(1,3)

        if wind_enemies == 1:
            return raven.Raven()
        
        elif wind_enemies == 2:
            return kingfisher.kingfisher()
        
        elif wind_enemies == 3:
            return magpie.MagPie()