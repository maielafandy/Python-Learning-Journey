# ---------------------------------
# This file is for learning
# creator: Mai Mohamed
# creation date : 5/30/2026
# -------------------------------
password = "0101"
task_list = []
while True:
    input_password = str(input("Enter the password"))
    if input_password == password:
        password_status = True
        print("Welcome Mai ,")
        while password_status == True:
            try:
                User_ask = int(input(
                    " choose from the menu \n1-add task \n2-view tasks \n3-delet task\n4-change the password\n5-exit"))
                if User_ask == 1:
                    try:
                        task_to_be_added = str(
                            input("Enter the task you want to add"))
                        task_list.append(task_to_be_added)

                        print("task is successfully added")

                    except:
                        print("invalid task name ")
                        continue
                elif User_ask == 2:
                    print("------------------------------------------------------")

                    for index, task in enumerate(task_list):
                        print(f"{index+1} .{task}")

                    print("------------------------------------------------------")

                elif User_ask == 3:
                    print("------------------------------------------------------")

                    for index, task in enumerate(task_list):
                        print(f"{index+1} .{task}")
                    print("------------------------------------------------------")
                    try:
                        Task_to_be_deleted = int(
                            input("enter the no.of task you want to deleted"))
                        task_index = Task_to_be_deleted-1
                        task_list.pop(task_index)
                        print("task is successfully removed")
                    except:
                        print("invalid choise ")
                        continue

                elif User_ask == 4:
                    New_password = str(input("enter the new password"))
                    password = New_password
                elif User_ask == 5:
                    password_status = False
                    break

            except:
                print("unvaild choise please try again")
                continue
    else:
        print("wong pass  try again")
        password_status = False
        continue
