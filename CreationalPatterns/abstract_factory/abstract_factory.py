import abc

class AbstractFactory(abc.ABC):

    @abc.abstractmethod
    def createProductA(self):
        pass

    @abc.abstractmethod
    def createProductB(self):
        pass



    
