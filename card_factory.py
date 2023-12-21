import abc 

class CardFactory(abc.Abc):

    @abstractmethod
    def create_random_card(self):
        """
        Abstract method (no code) that each concrete 
        factory overrides to create and return Card objects.
        """
        pass 