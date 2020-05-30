from abstract_products import *

class ProductA(AbstractProductA):
    def actionA(self,product):
        print("ProductA relates to",
        product.actionB())

class ProductB(AbstractProductB):
    def actionB(self):
        return "ProductB"


class ProductA2(AbstractProductA):
    def actionA(self,product):
        print("ProductA2 relates to",
        product.actionB())

class ProductB2(AbstractProductB):
    def actionB(self):
        return "ProductB2"
        