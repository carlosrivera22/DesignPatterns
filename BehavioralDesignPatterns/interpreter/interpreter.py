# The Interpreter pattern has a limited area where it can be applied. We can dsicuss the 
# Interpreter pattern only in terms of formal grammars but in this area there are better 
# solutions and this is the reason why this pattern is not so frequenlty used. 
# This pattern can be applied for parssing light expressions defined in simple grammars and 
# sometimes in simple rule engines.


from expressions import *
from context import Context

roman = "MCMXXVIII"
context = Context(roman)

# Build the parse tree
tree = []
tree.append(ThousandExpression())
tree.append(HundredExpression())
tree.append(TenExpression())
tree.append(OneExpression())

# Interpret
for exp in tree:
    exp.interpret(context)

print(roman + " = " + str(context.get_output()))