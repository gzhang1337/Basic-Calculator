operations = ["add","subtract","multiply","divide","power", "+", "-", "*", "/", "**"]
value1 = input("Please enter your first number: ")
value2 = input("Please enter your second number: ")
question = input("What would you like to do? ")

value1_float = float(value1)
value2_float= float(value2)

def add(num1=0, num2=0):
    return num1+num2

def subtract(num1=0, num2=0):
    return num1-num2

def multiply(num1=0, num2=0):
    return num1*num2

def divide(num1=0, num2=0):
    return num1/num2

def power(num1=1, num2=0):
    return num1**num2

while question not in operations:
    print("Please input a math operation")
    question = input("What would you like to do? ")
if question in operations == "add" or operations == "+":
    print(add(value1_float, value2_float))
elif question in operations =="subtract" or operations =="-":
    subtract(value1_float, value2_float)
elif question in operations =="divide" or operations =="/":
    divide(value1_float, value2_float)
elif question in operations =="multiply" or operations=="*":
    multiply(value1_float, value2_float)
else:
    power(value1_float, value2_float)
