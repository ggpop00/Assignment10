import Assignment9_2 as m
class Invalidinput(Exception):
    def __init__(self,message):
        super().__init__(message)  
try:
    num1=int(input("enter num1: "))
    num2=int(input("enter num2: "))
except ValueError as error:
    raise Invalidinput("the provided values are invalid")  from error
opr = m.MathOp(num1,num2)
print("Choose from below: ")
print("1) Addition\n2) Subtraction\n3) Trignometric")
n=int(input("Enter your choice: "))
if n==1:
    add = opr.addition()
    print("Addition:", add)
elif n==2:
    sub= opr.subtraction()
    print("Subtraction:", sub)
elif n==3:
    print("Choose from below: ")
    print("1) Sine\n2) Cosine ")
    if n==1:
        print("Sine: ",opr.sin())
    elif n==2:
        print("Cosine: ")
    else:
        print("Wrong Choice")

else:
    print("Invalid Choice")
