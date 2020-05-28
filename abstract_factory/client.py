# Abstract Factory offers the interface for creating a family
# of related objects, without explicitly specifying their
# classes. 

# Abstract Factory is a super-factory which creates other
# factories (Factory of factories)

# We should use the Abstract Factory design pattern when 
# (1) The system needs to be independent from the way the 
# products it works with are created. 

# (2) The system is or should be configured to work with
# multiple families of products. 

# (3) A family of products is designed to work all together

# (4) The creation of a library of products is needed, for 
# which is relevant only the interface, not the implementation,
# too. 

# Benefits:
    # It isolates the creation of objects from the client that needs
    # them. (Makes manipulation easier)

    # If the products of a family are meant to work together, the 
    # Abstract Factory makes it easy to use the objects from one 
    # family at a time. 

# Drawbacks:
    # Adding new products to the existing factories is difficult, 
    # because the Abstract Factory interface uses fixed set of
    # products that can be created. (Involves changing the Abstract
    # Factory and all its subclasses)

# Recommended to use Factories as Singletons
from factories import Factory1,Factory2
class Client:
    def __init__(self, factory):
        self.factory = factory
        self.a = factory.createProductA()
        self.b = factory.createProductB()

    def execute(self):
        self.a.actionA(self.b)

g1 = Client(Factory1())
g2 = Client(Factory2())
g1.execute()
g2.execute()