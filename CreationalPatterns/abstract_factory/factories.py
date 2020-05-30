from abstract_factory import AbstractFactory
from products import *
# Concrete factories:
class Factory1(AbstractFactory):
    def createProductA(self): return ProductA()
    def createProductB(self): return ProductB()

class Factory2(AbstractFactory):
    def createProductA(self): return ProductA2()
    def createProductB(self): return ProductB2()