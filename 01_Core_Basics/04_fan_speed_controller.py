# ---------------------------------
# This file is for learning
# creator: Mai Mohamed
# creation date: 5/30/2026
# --------------------------------- 

while True:
    Temperature_input = input(
        "Enter the Temperature (or type 'exit' to quit)\n ")
    if Temperature_input.lower() == "exit":
        break
    else:
        try:
            Temperature = float(Temperature_input)

        except ValueError:
            print("invalid input\n")
            continue

        if Temperature < 20.0:
            print("fan off\n")

        elif 20.0 <= Temperature < 30.0:
            print("fan low\n")

        elif Temperature >= 30.0:
            print("fan high\n")
