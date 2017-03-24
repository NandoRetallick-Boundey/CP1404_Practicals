MIN_CHARACTER_CODE = 33
MAX_CHARACTER_CODE = 127


def main():
    value = int(get_number(MIN_CHARACTER_CODE, MAX_CHARACTER_CODE))
    character_to_convert = str(input("Enter a character: "))
    character_code = ord('{}'.format(character_to_convert))

    print("The ASCII code for {} is {}".format(character_to_convert, character_code))

    value_character = chr(value)

    print("The character for {} is {}".format(value, value_character))

    # for i in range(33, 127):
    #    print("{:4} {:>4}".format(i, chr(i)))


def get_number(lower, upper):
    while True:
        try:
            number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
            while number < lower or number > upper:
                print("Invalid number")
                number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
            else:
                return number
        except ValueError:
            print("Invalid input, must be a number")


main()
