
from abstract_product import AbstractProduct

class OneProduct(AbstractProduct):

    def execute(self):
        print("Executing one product")

class AnotherProduct(AbstractProduct):

    def execute(self):
        print("Executing another product")

