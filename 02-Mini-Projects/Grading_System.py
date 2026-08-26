# ---------------------------------
# This file is for learning
# Grading System
# creator: Mai Mohamed
# creation date : 5/30/2026
# ---------------------------------

while True:

    Grade_input = input("Enter Your score (or type 'exit to quit')\n")

    if Grade_input.lower() == "exit":
        break

    try:
        Grade = float(Grade_input)
        if 0 <= Grade <= 100:
            if 90 <= Grade:
                print("Congratulations! Your grade is A")
            elif 80 <= Grade:
                print("Your grade is B")
            elif 70 <= Grade:
                print("Your grade is C")
            elif 60 <= Grade:
                print("Your grade is D")
            elif Grade < 60:
                print("Sorry... you have faild your grade is F ")

        else:
            print("invalid input Please enter number for 0-100\n")
            continue
    except ValueError:
        print("invalid input please enter a score\n")
        continue
