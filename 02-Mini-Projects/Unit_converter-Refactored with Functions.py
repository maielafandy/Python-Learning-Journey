# ---------------------------------
# This file is for learning
# creator: Mai Mohamed
# creation date : 6/26/2026
# ---------------------------------


def Celisuis_to_fehinrhiet(value):
    return (value*9/5)+32


def fehinrhiet_to_Celisuis(value):
    return (value-32)*5/9


def meter_to_centimeter(value):
    return value*100


def centimeter_to_meter(value):
    return value/100


def take_type_of_units():

    try:
        type_of_units = int(
            input("choose the type of units \n1-tempreture \n2-length\n3-exit"))

    except ValueError:
        print("invalid input\n")
    return type_of_units


def take_the_conversion():

    if type_of_units == 1:

        try:
            type_of_coversion = int(input(
                "choose the type of unit\n1- Celisuis --> fehinrhiet \n2-fehinrhiet --> Celisuis\n "))
        except ValueError:
            print("invalid input\n")
        return type_of_coversion

    elif type_of_units == 2:

        try:
            type_of_coversion = (int(
                input("choose the type of unit\n1- m-->cm\n2- cm-->m\n")))

        except ValueError:
            print("invalid input\n")
        return type_of_coversion
    else:
        print("invalid choice")
        return None


def take_the_value():

    try:
        value = float(input("enter a number:\n"))
    except ValueError:
        print("invalid input\n")
    return value


def choose_the_operation(type_of_units, type_of_coversion, value):

    if (type_of_units == 1):
        if (type_of_coversion == 1):
            return Celisuis_to_fehinrhiet(value)
        elif (type_of_coversion == 2):
            return fehinrhiet_to_Celisuis(value)
        else:
            print("invalid choice")
            return None
    elif (type_of_units == 2):
        if (type_of_coversion == 1):
            return meter_to_centimeter(value)
        elif (type_of_coversion == 2):
            return centimeter_to_meter(value)
        else:
            print("invalid choice")
            return None


while True:
    type_of_units = take_type_of_units()
    if type_of_units == 3:
        break
    type_of_coversion = take_the_conversion()
    if type_of_coversion == 3:
        break
    value = take_the_value()
    result = choose_the_operation(type_of_units, type_of_coversion, value)
    print(f'the result is {result}')
