# ---------------------------------
# This file is for learning
# creator: Mai Mohamed
# creation date : 5/30/2026
# Student Records System
# -------------------------------
Password = "0000"
Students_dictionary = [{'Name': "Mai", 'Grade': 100},
                       {'Name': "Ahmad", 'Grade': 80}]
logedin = False
while True:
    entered_password = str(input("Enter the password"))
    if entered_password == Password:
        logedin = True
        print("Welcome Mayoy")
    else:
        print("wrong Password try again")
        logedin = False

    while logedin:

        try:
            User_choice = int(input(
                "choose from menu :\n1-add student\n2-view students\n3-update Grade\n4-delete student\n5-change password\n6-Exit"))
            if User_choice == 1:
                user_added_student_Name = (str(input("Enter students Name ")))
                try:
                    User_added_student_Grade = (
                        float(input("Enter student Grade")))
                    Students_dictionary.append(
                        {'Name': user_added_student_Name, 'Grade': User_added_student_Grade})
                    print("Student is added successfully")

                except ValueError:
                    print("the grade you entered is not valid Please try agian")
                    continue
            elif User_choice == 2:
                print(
                    "-----------------------------------------------------------------")
                for index, student in enumerate(Students_dictionary):
                    print(
                        f"{index+1}- Name :{student['Name']} || Grade: {student['Grade']} ")
                    print(
                        "-----------------------------------------------------------------")
            elif User_choice == 3:
                print(
                    "-----------------------------------------------------------------")
                for index, student in enumerate(Students_dictionary):
                    print(
                        f"{index+1}- Name :{student['Name']} || Grade: {student['Grade']} ")
                    print(
                        "-----------------------------------------------------------------")
                try:
                    User_choosed_student = int(
                        input("Choose student you want to update his grad "))
                    User_updated_grade = float(input("enter the new grade"))
                    try:
                        index = User_choosed_student-1
                        Students_dictionary[index]['Grade'] = User_updated_grade
                    except ValueError:
                        print("unvalid Grade")
                        continue
                except ValueError:
                    print("your choice is not valid please try again")
                    continue
            elif User_choice == 4:
                print(
                    "-----------------------------------------------------------------")
                for index, student in enumerate(Students_dictionary):
                    print(
                        f"{index+1}- Name :{student['Name']} || Grade: {student['Grade']} ")
                    print(
                        "-----------------------------------------------------------------")
                try:
                    User_choosed_student = int(
                        input("Choose student you want to delet "))
                    index = User_choosed_student-1
                    Students_dictionary.pop(index)
                    print("Student deleted successfully")
                except ValueError:
                    print("your choice is not valid please try again")
                    continue
            elif User_choice == 5:
                New_password = str(input("Enter the New password"))
                Password = New_password
                print("Password changed successfully")
            elif User_choice == 6:
                logedin = False
                break
            else:
                print("unvaild choice Please try again")
        except ValueError:
            print("your choice is not valid please try again")
            continue
