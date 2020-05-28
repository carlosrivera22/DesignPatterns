from abstract_product import AbstractProduct
from abstract_factory import AbstractFactory

class Product(AbstractProduct):

    def execute(self):
        print("executing product")

    class Factory:
        def createProduct(self): return Product()


class Product2(AbstractProduct):
    def execute(self):
        print("executing product 2")

    class Factory:
        def createProduct(self): return Product2()