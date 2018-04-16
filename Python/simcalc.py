#SIMPLE CALC
# logic- Using def add(arg1, arg2):
#           return("The Two numbers sum is"+arg1 + arg2)

#Number Functions
def add(x, y ):
    """Adding two numbers!"""
    return x + y

def subtract(x , y):
    """Subtract two numbers!"""
    return x - y
def divide(x , y):
    """Divide two numbers!"""
    return x / y
def multiply(x , y):
    """Mutiply Two Numbers"""
    return x * y

#Logic
type = int(input("Please choose 1,2,3 or 4\n[1] Add\n[2] Subtract\n[3] Mutiply\n[4] Divide"))
num1 = int(input("Please enter your first number!"))
num2= int(input("Please enter your second number!"))
if type == 1:
    print(num1,"+",num2,"=",add(num1,num2))
elif type == 2:
    print(num1,"-",num2,"=",subtract(num1,num2))
elif type == 3:
    print(num1,"*",num2,"=",multiply(num1,num2))
elif type == 4:
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid Response")


