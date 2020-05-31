#CONTEXT
from behaviors import *
class Robot:
    def __init__(self,name):
        self.name = name
        self.behavior = None

    def set_behavior(self,behavior):
        self.behavior = behavior

    def get_behavior(self):
        return self.behavior

    def move(self):
        print(self.name + ": Based on current position" + " the behavior object decides the next move:")

        command = self.behavior.move_command()

        #sends the command to mechanisms
        print("\t The result returned by the behavior object " + 
        "is sent to the movement mechanisms " + " for the robot ' " +
        self.name + "'")

    def get_name(self):
        return self.name


    def set_name(self,name):
        self.name = name


