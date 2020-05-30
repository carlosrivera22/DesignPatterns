import abc

class AbstractProduct(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        pass

    