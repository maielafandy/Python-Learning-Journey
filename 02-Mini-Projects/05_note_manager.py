import os


def menu():
    try:
        choice = int(input(
            "choose from the menu : \n1-add note \n2-display note \n3-clear note \n4-exit\n"))
        return choice
    except ValueError:
        print("invalid choice")


def clear():
    with open("note.txt", "w") as f:
        f.write(" "+"\n")


def add_note():
    added_note = input("enter the note you want to add"+"\n")
    with open("note.txt", "a") as f:
        f.write(added_note+"\n")


def display_note():
    with open("note.txt") as f:
        display_note = f.read()
    print(display_note + "\n")


while True:
    choice = menu()
    if choice == 1:
        add_note()
    elif choice == 2:
        display_note()
    elif choice == 3:
        clear()
    elif choice == 4:
        break
    else:
        print("not existed choice")
