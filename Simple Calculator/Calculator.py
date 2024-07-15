import time

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if ( y != 0):
        return x/y
    else:    
        return "Not Allowed to be divided by 0"
def calculator():
    print("Welcome to the Calculator")
    time.sleep(2)
    print("Select Operation")
    print("1. ADD")
    print("2. SUB")
    print("3. MUL")
    print("4. DIV")

    choice = input("Enter Choice (1/2/3/4)")

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if(choice == '1'):
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif(choice == '2'):
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif(choice == '3'):
        print(f"{num1} * {num2} = {mul(num1, num2)}")
    elif(choice == '4'):
        print(f"{num1} / {num2} = {div(num1, num2)}")
    else:
        print("Please enter Valid Input")
    
while True:
    calculator()
    another_calculation = input ("Do you want to perform another calculation (y/n)")
    if another_calculation != 'y':
        print("Have a Nice Day!")
        break
