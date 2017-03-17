def main():

    users_name = str(input("What is your name??"))

    menu()

    menu_choice = str(input("Your Response?? "))

    while menu_choice != "Q":
        if menu_choice == "H":
            print("Hello {}".format(users_name))
        elif menu_choice == "G":
            print("Goodbye {}".format(users_name))
        else:
            print("Invalid Choice")
        menu()
        menu_choice = str(input("Your Response?? "))


def menu():

    print("Hello")
    print("Goodbye")
    print("Quit")

main()
