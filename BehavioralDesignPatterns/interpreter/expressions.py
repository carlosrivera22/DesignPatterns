from abstract_expression import Expression

class ThousandExpression(Expression):

    def one(self):
        return "M"
    
    def four(self):
        return " "

    def five(self):
        return " "
    
    def nine(self):
        return " "

    def multiplier(self):
        return 1000


class HundredExpression(Expression):

    def one(self):
        return "C"
    
    def four(self):
        return "CD"

    def five(self):
        return "D"
    
    def nine(self):
        return "CM"

    def multiplier(self):
        return 100


class TenExpression(Expression):

    def one(self):
        return "X"
    
    def four(self):
        return "XL"

    def five(self):
        return "L"
    
    def nine(self):
        return "V"

    def multiplier(self):
        return 10



class OneExpression(Expression):
    def one(self):
        return "I"
    
    def four(self):
        return "IV"

    def five(self):
        return "V"
    
    def nine(self):
        return "IX"

    def multiplier(self):
        return 1
    
