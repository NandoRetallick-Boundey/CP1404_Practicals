name = str(input("Enter your name: "))

in_file = open("name.txt", mode='w')

in_file.write(name)
in_file.close()
