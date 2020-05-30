
# The builder pattern defines an instance for creating an object but 
# letting subclasses decide which class to instantiate. 

# Refers to the newly created object through a common interface. 

# This pattern allows a client object to construct a complex object
# by specifying only its type and content. 

# Builder Pattern is used when: 
# (1) The creation algorithm of a complex object is independent from the parts
# that actually compose the object. 

# (2) The system needs to allow different representations for the objects that
# are being built. 

# Use cases:
    # Vehicle Manufacturing
    # Student Tests 
from director import Director
from builders import ConcreteBuilder1
if __name__ == "__main__":


    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()



    print("\n\nStandard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()


    print("\n\nCustom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()