todo_list = ["shopping", "exercising", "studying"]

def my_list():
    while True:
        try:

            x = int(input("Press 1 to add, press 2 to remove, and press 3 to exit: "))
            if x == 1:
                print("What do you need to add to the list?:")
                y = input()
                todo_list.append(y)
                print(todo_list)

            elif x == 2:
                print("What do you need to remove from the list?:")
                z = input()
                if z in todo_list:
                    todo_list.remove(z)
                    print(todo_list)
                else:print(f"{z} is not in the list")
            elif x == 3:
                print("Exiting the program")
                break
            else:
                print("That is not a valid number")
        except ValueError:
            print("Try again, it is not a number")




my_list()































