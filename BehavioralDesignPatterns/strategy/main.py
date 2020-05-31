# Define a family of algorithms, encapsulate each one, and make them interchangeable.
# Strategy lets the algorithm vary independently from clients that use it. 


from behaviors import *
from robot import Robot

r1 = Robot("Big Robot")
r2 = Robot("C3PO")
r3 = Robot("R2D2")

r1.set_behavior(AgressiveBehavior())
r2.set_behavior(DefensiveBehavior())
r3.set_behavior(NormalBehavior())

r1.move()
r2.move()
r3.move()

print("\r\n New behaviors: " + 
    "\r\n\t 'Big Robot' gets really scared" + 
    "\r\n\t, 'C3PO' becomes really mad because it's always attacked by other robots" +
    "\r\n\t and R2 keeps its calm.\r\n")

r1.set_behavior(DefensiveBehavior())
r2.set_behavior(AgressiveBehavior())

r1.move()
r2.move()
r3.move()