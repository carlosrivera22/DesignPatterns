import abc
class AbstractProductA(abc.ABC):
    @abc.abstractmethod
    def actionA(self): pass

class AbstractProductB(abc.ABC):
    @abc.abstractmethod
    def actionB(self): pass



