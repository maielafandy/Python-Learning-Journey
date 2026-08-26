# ---------------------------------
# This file is for learning
# creator: Mai Mohamed
# creation date : 5/28/2026
# ---------------------------------
while True:

    # Getting the inputs
    First_Num = input("Enter first number (or type exit):\n ")

    if First_Num.lower() == "exit":
        break
     # checking for error
    try:
        First_Num = float(First_Num)
    except:
        print("Invalid Input")
        break
    Operator = str(input("enter the Operator :\n"))
    Second_Num = input("enter the Second number :\n")
    # checking for error
    try:
        Second_Num = float(Second_Num)
    except:
        print("Invalid Input")
        break


# Makinf the operations
    if Operator == "+":
        Result = str(First_Num + Second_Num)
        print("The result =" + Result)
    elif Operator == "*":
        Result = str(First_Num * Second_Num)
        print("The result =" + Result)
    elif Operator == "/":
        if Second_Num == 0:
            print("invalid Operation")
        else:
            Result = str(First_Num / Second_Num)
            print("The result =" + Result)
    elif Operator == "-":
        Result = str(First_Num - Second_Num)
        print("The result =" + Result)
    elif Operator == "exit":
        break
    else:
        print("Invalid operator")
