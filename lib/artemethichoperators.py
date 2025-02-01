#   ArtemethicOperators

class ArtemethicOperators(object):

    def Addition(self, x, y):
        return x + y

    def Subtraction(self, x, y):
        return x - y

    def Multiplication(self, x, y):
        return x * y
    
    def Exponentiation(self, x:int, base:int, expo:int):
        return self.Multiplication(x , base ** expo)
    
    def Remainder(self, x, y):
        return x % y
    
    def Quotient(self, x, y):
        return x // y
    