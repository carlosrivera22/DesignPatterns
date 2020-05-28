import abc

class AbstractFactory(abc.ABC):

    @abc.abstractmethod
    def createProduct(self):
        pass
    
