# ---------------------------------
# This file is for learning
# creator: Mai Mohamed
# creation date: 5/28/2026
# modification date: 6/26/2026
# ---------------------------------
def add(first_Num, second_Num):

    return first_Num+second_Num


def devision(first_Num, second_Num): 

    if second_Num == 0:
        print("invaild operation")
        return None
    else:
        return first_Num/second_Num


def multiplication(first_Num, second_Num):

    return first_Num*second_Num


def subtraction(first_Num, second_Num):

    return first_Num-second_Num


while True:

    # Getting the inputs

    first_Num = input("Enter first number (or type exit):\n ")

    if first_Num.lower() == "exit":
        break
     # checking for error
    try:
        first_Num = float(first_Num)
    except ValueError:
        print("Invalid Input")
        break
    operator = str(input("enter the Operator :\n"))
    second_Num = input("enter the Second number :\n")
    # checking for error
    try:
        second_Num = float(second_Num)
    except ValueError:
        print("Invalid Input")
        break


# Makinf the operations
    if operator == "+":
        result = add(first_Num, second_Num)
    elif operator == "*":
        result = multiplication(first_Num, second_Num)
    elif operator == "/":
        result = devision(first_Num, second_Num)

    elif operator == "-":
        result = subtraction(first_Num, second_Num)

    elif operator == "exit":
        break
    else:
        print("Invalid operator")
    print(f'the Result is {result}')
