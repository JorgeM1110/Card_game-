import abc

class BossSate(abc.ABC):

    @abc.abstractmethod
    def plays(self):
        """
        abstract (no code)
        """
        pass

    @abc.abstractmethod
    def mechanic(self, boss):
        """
        abstract (no code)
        """
        pass
