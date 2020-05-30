from abc import ABC, abstractmethod
from context import Context
from expressions import *
class Expression(ABC):

    @abstractmethod
    def one(self):
        pass

    @abstractmethod
    def four(self):
        pass

    @abstractmethod
    def five(self):
        pass

    @abstractmethod
    def nine(self):
        pass

    @abstractmethod
    def multiplier(self):
        pass


    def interpret(self,context):
        if len(context.get_input()) == 0:
            return 
        
        if context.get_input().startswith(self.nine()):
            context.set_output(context.get_output()+ (9*self.multiplier()))
            context.set_input(context.get_input()[2:])

        elif context.get_input().startswith(self.four()):
            context.set_output(context.get_output()+ (4*self.multiplier()))
            context.set_input(context.get_input()[2:])

        elif context.get_input().startswith(self.five()):
            context.set_output(context.get_output()+ (5*self.multiplier()))
            context.set_input(context.get_input()[1:])

        while context.get_input().startswith(self.one()):
            context.set_output(context.get_output()+ (1*self.multiplier()))
            context.set_input(context.get_input()[1:])

