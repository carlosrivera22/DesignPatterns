# Define the skeleton of an algorithm in an operation, deferring some steps to subclasses.
# Template method lets subclasses redefine certain steps of an algorithm without letting them
# change the algorithms structure. 

from packages import *

p = PackageA()
p.perform_trip()

