# ---------------------------------
# This file is for learning
# creator: Mai Mohamed
# creation date : 5/28/2026
# ---------------------------------

while True:
    try:
        type_of_unit = int(
            input("choose the type of unit\n1-length\n2-tempreture\n3-exit\n"))
        if type_of_unit == 3:
            break
        elif type_of_unit == 1:
            try:
                Conversion = int(
                    input("choose the type of unit\n1- m-->cm\n2- cm-->m\n3-km-->m\n"))
                if Conversion == 1:
                    try:
                        Num = float(input("enter a number:\n"))
                        Result = Num*100
                    except:
                        print("the input not valid ")
                        break

                elif Conversion == 2:

                    try:
                        Num = float(input("enter a number:\n"))
                        Result = Num/100
                    except:
                        print("the input not valid ")
                        break

                elif Conversion == 3:
                    try:
                        Num = float(input("enter a number:\n"))
                        Result = Num*1000
                    except:
                        print("the input not valid ")
                        break

            except:
                print("your choice is not valid ")
                break
        elif type_of_unit == 2:
            try:
                Conversion = int(input(
                    "choose the type of unit\n1- Celisuis --> fehinrhiet \n2-fehinrhiet --> Celisuis\n "))
                if Conversion == 1:
                    try:
                        Num = float(input("enter a number:\n"))
                        Result = (Num*9/5)+32
                    except:
                        print("the input not valid ")
                        break

                elif Conversion == 2:

                    try:
                        Num = float(input(("enter a number:\n")))
                        Result = (Num-32)*5/9
                    except:
                        print("the input not valid ")
                        break
            except:
                print("your choice is not valid ")
                break
        else:
            print("your choice is not valid ")
            break
        print(Result)
        print("\n")
    except:
        print("your choice is not valid ")
        break
