# The Command pattern encapsulates commands (method calls) in objects allowing us
# to issue requests without knowing the requested operation or the requesting object. 

# Command design pattern provides the options to queue commands, undo/redo actions and
# other manipulations

# Allows the parametrization of clients with different requests
# Allows saving the requests in a queue.

# The client asks for a command to be executed
# The invoker takes the command, encapsulates it and places it in a queue, in case 
# there is something else to do first. 
# The command that is in charge of the requested command sends the result to the receiver. 
# The receiver knows how to perform the operations.

# Example: Meal ordering at a restaurant. 
    # The client is the customer. He sends his request to the receiver through the waiter.
    # who is the Invoker. 
    
    # The waiter encapsulates the command (the order in this case) by writing it on the check
    # and then places it, creating the Command object. 

    # The Receiver will be the cook that, after completing work on all the orders that were 
    # sent to him before the command in question, starts working on it. 


from invoker import Invoker
from simple_command import SimpleCommand
from complex_command import ComplexCommand
from receiver import Receiver

if __name__ == "__main__":

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()