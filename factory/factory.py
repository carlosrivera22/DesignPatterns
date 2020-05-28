# Creates objects without exposing the instantiation logic to the client. 
# Refers to the newly created object through a common interface. 

# The advantage is that new products can be added without changing a single line
# of code

# The problem with this implementation is that once we add a new product call we should
# modify the Factory class.

# The Factory class is usually used as a singleton
from products import *

class Factory:
    instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if Factory.instance != None:
            raise Exception("This class is a singleton!")
        else:
            Factory.instance = self

    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Factory.instance == None:
            Factory()
        return Factory.instance

    def createProduct(self,product_id):
        if (product_id == 1):
            return OneProduct()
        if (product_id == 2):
            return AnotherProduct()

        return None

