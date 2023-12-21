import card_factory
import random

class GrassFactory(card_factory.CardFactory):
    """
    factory to create Grass enemies.
    """

    def create_random_card(self):
        
        grass_enemies = random.randint(1,3)

        if grass_enemies == 1:
            return bear.Bear()
        
        elif grass_enemies == 2:
            return skunk.Skunk()
        
        elif grass_enemies == 3:
            return snake.Snake()