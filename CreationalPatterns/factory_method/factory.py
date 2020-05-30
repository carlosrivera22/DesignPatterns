# Defines an interface for creating objects, but lets subclasses to decide which class
# to instantiate.

# Refers to the newly created object through common interface. 

# Factory Method is related to the idea on which libraries work:

    # A library uses abstract classes for defining and maintaining relations 
    # between objects. One type of responsability is creating such objects. 

    # The library knows when an object needs to be created, but not what kind of
    # object it should create, this being specific to the application using the
    # library. 

# Benefits:

    # It introduces a separation between the application and a family of classes. 
    # It provides a simple way of extending the family of products with minor changes
    # to the application code. 
    # It provides customization hooks. When the objects are created directly inside
    # the class it's hard to replace them by objects to extend their functionality. 

# Drawback:

    # The factory has to be used for a family of objects. If the classes doesn't extend
    # common base class or interface they cannot be used in a factory design template.

from abstract_factory import AbstractFactory
from products import *
class ProductFactory(AbstractFactory):

    factories = {}
    def addFactory(id, ProductFactory):
        Factory.factories.put[id] = shapeFactory

    addFactory = staticmethod(addFactory)


    def createProduct(id):
        if not id in ProductFactory.factories:
            ProductFactory.factories[id] = \
              eval(id + '.Factory()')
        return ProductFactory.factories[id].createProduct()


    createProduct = staticmethod(createProduct)
