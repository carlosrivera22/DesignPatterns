# Chain of Responsability avoids attaching the sender of a request to its receiver,
# giving this way other objects of possibility of handling the request too. 

# The objects become parts of a chain and the request is sent from one object to
# another across the chain until one of the objects will handle it. 

# This pattern allows an object to send a command without knowing what object will 
# receive it and handle it. 

# The most usual example of a machine using the chain of reponsability is the vending 
# machine coin slot. Rather than having a slot for each type of coin, the machine 
# has only one slot for all of them. 

# Situations in which to use this pattern:
    # More than one object can handle a command
    # The handler is not known in advance
    # The handler should be determined automatically
    # It's wished that the request is addressed to a group of objects without explicitly specifying its receiver
    # The group of objects that may handle the command must be specified in a dynamic way. 


from handlers import *
from request import Request
#Set up chain of responsability
h1 = Handler1()
h2 = Handler2()
h3 = Handler3()

h1.set_next(h2)
h2.set_next(h3)

#Send requests to the chain
h1.handle(Request('Negative ',-1))
h1.handle(Request('Zero ',0))
h1.handle(Request('Positive ', 1))
h1.handle(Request('Negative ', -5))
