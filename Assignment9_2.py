import math 
class MathOp:
    def __init__(self,num1=0,num2=0):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return(self.num1 + self.num2)
        
    def subtraction(self):
        return(self.num1 - self.num2)
        
    def multiplication(self):
        return(self.num1 * self.num2)
        
    def division(self):
        if self.num2 != 0:
            return (self.num1 // self.num2)
        else:
            raise ZeroDivisionError("Cannot divide by zero!")
    def squar(self):
        if self.num1 >= 0:
            return( math.sqrt(self.num1))
        else:
            raise ValueError("Cannot calculate square root of a negative number!")
    
    def sin(self):
        return math.sin(self.num1) , math.sin(self.num2)
